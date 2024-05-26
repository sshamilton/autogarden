import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.client.query_api import QueryApi

def getsensorvals(sa, sb, sc):
    token = os.environ.get("INFLUXDB_TOKEN")
    org = "home"
    url = "http://192.168.1.136:8086"

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
        print("5 minute average moisture on sensor A: ")
        vals[1] = record['_value']


    query = """from(bucket: "garden")
     |> range(start: -5m)
     |> filter(fn: (r) => r._measurement == "prometheus")
     |> filter(fn: (r) => r._field == "analogb")
     |> mean()"""

    tables = query_api.query(query, org="home")
    for table in tables:
      for record in table.records:
        print("5 minute average moisture on sensor B: ")
        vals[2] = record['_value']

    query = """from(bucket: "garden")
     |> range(start: -5m)
     |> filter(fn: (r) => r._measurement == "prometheus")
     |> filter(fn: (r) => r._field == "analogc")
     |> mean()"""

    tables = query_api.query(query, org="home")
    for table in tables:
      for record in table.records:
        print("5 minute average moisture on sensor C: ")
        vals[3] = record['_value']


def main():
    print("Begin")
    svalues = getsensorvals()
    print ("Sensor a: ", svalues[1])
    if (svalues[3] > 250):
        print("Time to water")
    


if __name__ == "__main__":
    main()
