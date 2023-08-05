# Meraki BSSID List

This project creates a simple program to generate a list of enabled BSSID from your organization's Meraki networks. It's a script that allows Network Administrators to easily retrieve the details of the BSSID in their wireless networks. This helps the organization by providing a simple method to collect BSSID, aiding network troubleshooting and management.

## Technology Stack

This script is written in Python and uses the Meraki DashboardAPI to interact with the Meraki networks. Python was chosen due to the availability of Meraki's advanced API package and simplicity of the syntax. 

## Status

The current version of this script is a stable release, 1.0. 

## Use Case

The primary use case of this code is to retrieve and store information about BSSID in a CSV file. It loops through every organization, network and device registered under Meraki to fetch BSSID details. 

It offers a solution to network administrators having to manually gather this data or implementing more complex solutions. 

## Installation

To install this script:

1. Clone the [repo](<your repo link here>)

```bash
git clone https://github.com/<yourGithubUsername>/<yourRepoName>.git
cd <yourRepoName>
```

2. Install the `meraki` package:

```bash
pip install meraki
```

## Configuration

In the script you must replace `'Your Meraki API Key'` with your actual Meraki API key. 

## Usage

To execute the script, run:

```bash
python3 bssid_list.py
```

The output will be written to `bssid.csv` in the same directory where you run the script from.

## Known issues

If there are many devices in your network, the script will be running for a while as it needs to make requests to the Meraki API for each device. This is a known issue due to rate limit, so plan accordingly when running this script.

## Future Ideas

For future versions, we're considering adding a feature to display the progress of the fetching, options to specify organizations / networks / devices to fetch from, and additional options to filter or format the output. 

## Contributions

We're welcome to the contributions, please fork the project and submit your Pull Requests! 

## License

This project is licensed under the terms of the MIT license. For more details, see the [LICENSE](LICENSE) file.
