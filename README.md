# Autogarden
## A few scripts for auto watering a garden when the soil moisture gets too low

This project uses InfluxDB, a time series database to store moisture values from three sensors connected to an arduino in my garden.
As the ground becomes dry, the values rise, and the script turns on a Kasa smart switch that enables a pump to pump water into a rain barrel that waters the garden.

A sample of the Arduino web data (this gets scraped by InfluxDB):
```
#HELP analoga Analog Read from Arduino
#TYPE analoga gauge
analoga 302.0
#HELP analogb Analog Read from Arduino
#TYPE analogb gauge
analogb 216.0
#HELP analogc Analog Read from Arduino
#TYPE analogc gauge
analogc 250.0
#HELP analogd Analog Read from Arduino
#TYPE analogd gauge
analogd 301.0
#HELP temperature Temperature in Celsius
#TYPE temperature gauge
temperature 2.72
#HELP perssure Pressure in Hg
#TYPE pressure gauge
pressure 1023.72
#HELP humidity Humidity in %
#TYPE humidity gauge
humidity 45.86
}
