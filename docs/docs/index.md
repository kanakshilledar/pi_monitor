# Pi Monitor 
Pi Monitor is a simple fablab epquipment monitoring device which helps in managing the epquipments effectively.
This project is inspired from [fabman](https://fabman.io).

## Bill of Materials
This project requires the following components:

- Raspberry Pi 3b+ with raspbian
- MFRC522 RFID Reader
- Push Button
- Relay Module

## Connection diagram
**TODO: add circuit diagram**
I am using GPIO mode as Board which means the RPi pin represents the physical board pin numbering.

### Wiring Connections:

| Component    | Pin    | RPi Pin |
| ------------ | ------ | ------- |
| RFID Reader  | SDA    | 24      |
| RFID Reader  | SCK    | 23      |
| RFID Reader  | MOSI   | 19      | 
| RFID Reader  | MISO   | 21      |
| RFID Reader  | RST    | 22      |   
| RFID Reader  | GND    | 6       | 
| RFID Reader  | 3v3    | 1       |
| Push Button  | A      | 40      |
| Push Button  | B      | 39      |
| Relay Module | Signal | 38      |
| Relay Module | PWR    | 2       | 
| Relay Module | GND    | 39      |

## Build Instructions
Once the connections are done follow the below steps to install the software

First step is to enable SPI Interface on Raspberry Pi
```commandline
$ sudo raspi-config
```
It will be inside the Interfaces option. Once enabled reboot Raspberry Pi to proceed further.

**Library Dependencies:**

- spidev
- mfrc522
- google-api-python-client 
- oauth2client


```commandline
$ git clone https://github.com/kanakshilledar/pi_monitor
$ cd pi_monitor
$ source fabenv/bin/activate
$ python3 main.py
```
You can see the realtime updates on this [spreadsheet](https://docs.google.com/spreadsheets/d/1BrL5Otvrh-FoOBY85auZIQjPN3vux14J4V3oUd4Tpfk/).

Your Pi Monitor is up and running!