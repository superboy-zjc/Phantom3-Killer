<h1 align="center">Welcome to Phantom3 Killer 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
</p>

> An automated attacking script for taking over Dji Phantom3 drone with seemless experience.

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

![render1709853175528](https://api.2h0ng.wiki:443/noteimages/2024/03/07/18-15-33-10b52aa60e6a17562f30ff20970e0ee4.gif)

## Author

👤 **zhong**

* Website: https://blog.2h0ng.wiki/
* Github: [@superboy-zjc](https://github.com/superboy-zjc)

## Show your support

Give a ⭐️ if this project helped you!
