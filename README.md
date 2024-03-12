<h1 align="center">Welcome to Phantom3 Killer 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
</p>

> An automated attacking script for taking over Dji Phantom3 drone with seemless experience.

## Install

**Docker (Only appliable for Linux OS):**

```
docker pull zhong8/phantom3-killer:1.0
```

**Terminal:**

```sh
# MAC OS
brew install nmap
pip install -r requirements.txt

# Linux OS
apt-get install nmap
pip install -r requirements.txt
```

## Usage

1️⃣  Login into the DJI Phantom3's wifi network with your phone, and open up the DJI GO App waiting for taking over control of the drone.

2️⃣  Disable the packet forwarding configuration by `sudo sysctl net.ipv4.ip_forward=0`

3️⃣  Execute the phantom3-killer:

**Docker (Only appliable for Linux OS):**

```bash
# Make ture enable host network mode sharing the interfaces with docker container
sudo docker run --network="host" zhong8/phantom3-killer:1.0 -a [ATTACKER_IP] -i [YOUR_INTERFACE_NAME]
```

**Terminal:**

```sh
python3 main.py -a [ATTACKER_IP] -i [YOUR_INTERFACE_NAME]
```

![render1709853175528](./image/usage.gif)

## Author

👤 **zhong**

* Website: https://blog.2h0ng.wiki/
* Github: [@superboy-zjc](https://github.com/superboy-zjc)

## Show your support

Give a ⭐️ if this project helped you!
