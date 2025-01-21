# Autogarden
## A few scripts for auto watering a garden when the soil moisture gets too low

This project uses InfluxDB, a time series database to store moisture values from three sensors connected to an arduino in my garden.
As the ground becomes dry, the values rise, and the script turns on a Kasa smart switch that enables a pump to pump water into a rain barrel that waters the garden.
