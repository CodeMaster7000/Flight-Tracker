import requests
params = {
    "access_key": "*API KEY*" # Paste API key here
}
try:
    flight_data = rq.get("http://api.aviationstack.com/v1/flights", params).json()
    json = flight_data["data"]
    for route in json:
        date = route["flight_date"]
        status = route["flight_status"]
        arrival = route["arrival"]["airport"]
        dep = route["departure"]["airport"]
        flight = route["airline"]["name"]
        data = route["flight"]["iata"]
        print(f"Flight number: {flight} {data}")
        print(f"Flight date: {date}")
        print(f"Flight status: {status}")
        print(f"Flight arrival time: {arrival}")
        print(f"Flight departure time: {dep}")
        print("")
except:
    print("Error: could not fetch data. Please check again.")
