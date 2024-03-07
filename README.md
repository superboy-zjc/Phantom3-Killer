<h1 align="center">Welcome to Phantom3 Killer 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
</p>

> A automated attacking script for taking over Dji Phantom3 drone with seemless experience.

## Install

```sh
pip install -r requirements.txt
```

## Usage

1️⃣  Login into the DJI Phantom3's wifi network with your phone, and open up the DJI GO App waiting for taking over control of the drone.

2️⃣  Disable the packet forwarding configuration by `sudo sysctl net.ipv4.ip_forward=0`

3️⃣  Execute the phantom3-killer:

```sh
python3 main.py -a [ATTACKER_IP] -i [YOUR_INTERFACE_NAME]
```

![Screen Recording 2024-03-07 at 17.29.48](https://api.2h0ng.wiki:443/noteimages/2024/03/07/17-35-48-e4207eef704f09388649d0e25e4d106e.gif)

## Author

👤 **zhong**

* Website: https://blog.2h0ng.wiki/
* Github: [@superboy-zjc](https://github.com/superboy-zjc)

## Show your support

Give a ⭐️ if this project helped you!
