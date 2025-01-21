import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.client.query_api import QueryApi
import subprocess
import datetime

def getsensorvals():
    token = os.environ.get("INFLUXDB_TOKEN")
    org = "home"
    url = "http://192.168.1.136:8086"
    vals = [0,0,0]
    #write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

    #for value in range(5):
    #  point = (
    #    Point("measurement1")
    #    .tag("tagname1", "tagvalue1")
    #    .field("field1", value)
    #  )
      #write_api.write(bucket=bucket, org="home", record=point)
    #  time.sleep(1) # separate points by 1 second

    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

    query_api = QueryApi(client)

    query = """from(bucket: "garden")
     |> range(start: -5m)
     |> filter(fn: (r) => r._measurement == "prometheus")
     |> filter(fn: (r) => r._field == "analoga")
     |> mean()"""

    tables = query_api.query(query, org="home")
    for table in tables:
      for record in table.records:
        vals[0] = record['_value']


    query = """from(bucket: "garden")
     |> range(start: -5m)
     |> filter(fn: (r) => r._measurement == "prometheus")
     |> filter(fn: (r) => r._field == "analogb")
     |> mean()"""

    tables = query_api.query(query, org="home")
    for table in tables:
      for record in table.records:
        vals[1] = record['_value']

    query = """from(bucket: "garden")
     |> range(start: -5m)
     |> filter(fn: (r) => r._measurement == "prometheus")
     |> filter(fn: (r) => r._field == "analogc")
     |> mean()"""

    tables = query_api.query(query, org="home")
    for table in tables:
      for record in table.records:
        vals[2] = record['_value']
    return vals

def main():
    while (True):
        svalues = getsensorvals()
        print ("Sensor a: ", svalues[0])
        print ("Sensor b: ", svalues[1])
        print ("Sensor c: ", svalues[2])
        average = (svalues[0] + svalues[1] + svalues[2])/3
        if (average > 250):
            print("Time to water. Average is:" + str(average))
            subprocess.run(["/home/stephen/garden/push.sh","Watering Average: " +str(average)])
            now = datetime.datetime.now()
            print (now)
            #subprocess.run(["/home/stephen/garden/water-garden.sh"])
        else:
            print("Not watering, average is: " + str(average))
            subprocess.run(["/home/stephen/garden/push.sh","Not watering. Average: " +str(average)])
        now = datetime.datetime.now()
        print(now)
        print("Waiting for one hour")
        time.sleep(60*60) 


if __name__ == "__main__":
    main()
