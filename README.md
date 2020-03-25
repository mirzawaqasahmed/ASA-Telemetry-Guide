# ASA VPN Health Monitoring 
### Example VPN health monitoring dashboard on Grafana for ASA devices [BETA]

With recent events, home working and VPN access have became a priority for many IT organisations, the often forgotten about ASA has became a mission critical part of our IT infrastructure. The challenge however is how do we monitor these devices on an ongoing basis to look for trends in usage, peaks and spot any potential issues with dashboards like below.

![](./images/dashboard-1.png)

In this short lab guide we'll explore the process of collecting data that exists in the command line however is very difficult to collect and monitor on an ongoing basis much as we'd do with Model Driven Telemetry[Link to MDT lab]. In this example we will take CLI output from the firewall using pyATS and parse the output to create a standard JSON output. From this standard JSON output we can use open source data stacks such as TIG (Telegraf, InfluxDB and Grafana) to collect, store and visualise data from ASA devices.

![](./images/dashboard.png)

```
Note: This lab uses beta parsers from the pyATS project, they have not been throughly tested in all environments so please proceed with caution, much of what we're going to do here will just be connecting to a device via SSH and reading the show command output so risk is limited but please take this into account.
```

To run these exercises you will need an instance of an ASA. dCloud has an ASA instance configured for remote that you can reserve and use in this. We'll be using the "Cisco AnyConnect Posture with ASA, ISE, and AMP v1.2" demo. Alternatively you can also use your own ASA if you have one available. This has been tested against ASA Version 9.5(2)203.

# Step 1 - Configuring your environment

```

ALL
THE
APT
GET
INSTALLS
```

```
mkdir /opt/telegraf
cd /opt/telegraf
```

```
git clone https://github.com/sttrayno/ASA-Telemetry-Guide.git
python3 -mvenv env3
source env3/bin/activate
```

```pip install -U pip
pip install -r scripts/requirements.txt
```

```Note: I am using the TIG stack container from Jeremy Cohoe, I am planing on rewriting parts of this lab with a fresh TIG stack install however for ease of use today we will be using Jeremy's container which I've also used in other labs.
```


