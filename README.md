# Meraki BSSID List

This project, dubbed "Meraki BSSID Dump", creates a simple but powerful Python script that generates a list of enabled BSSIDs across an organization's Meraki wireless networks. With a few simple commands, Network Administrators can retrieve detailed information of all the BSSIDs in their wireless networks, facilitating effective network management and troubleshooting.

## Technology Stack

The script is written in Python and utilizes the Meraki DashboardAPI to interact with the Meraki cloud. Python was chosen due to the language's user-friendly syntax and the comprehensive support provided by Meraki's Python SDK.

## Status

The current version is a stable release (1.0). However, subsequent updates and improvements are expected as and when necessary.

## Use Case

The primary function of this script is to scour through every organization, network, and device registered under the Meraki cloud and fetch pertinent details about every active BSSID. Consequently, it streamlines the process of gathering this data, which would otherwise require network administrators to implement convoluted solutions or perform manual data collection, a cumbersome and time-intensive process.

## Installation

Follow these steps to install and setup the script:

1. Clone the [repo](https://github.com/shantarsecurity/meraki-bssid-dump)

```bash
git clone https://github.com/shantarsecurity/meraki-bssid-dump.git
cd meraki-bssid-dump
```

2. Install the `meraki` package:

```bash
pip install meraki
```

## Configuration

You will have to replace `'Your Meraki API Key'` in the script with your actual Meraki Dashboard API key. 

## Usage

To run the script, use the following command:

```bash
python3 bssid_list.py
```

The script generates a CSV output file (`bssid.csv`) within the same directory from which the script is run.

## Known Issues

The script may run for an extended period if your network houses numerous devices since it would have to make API requests for every single device. This delay is unavoidable due to Meraki's API rate limit, so it is advisable to schedule the script execution during off-peak times or periods of low network traffic.

## Future Ideas

Future enhancements to the script could include a progress display feature to show the fetching operation's status, options to specify particular organizations/networks/devices, and additional output filtering or formatting.

## Contributions

Your contributions are most welcome. Please fork this project and submit your Pull Requests!

## License

This project is licensed under the terms of the GPL-3.0 license. For more information, please refer to the [LICENSE](LICENSE) file.
