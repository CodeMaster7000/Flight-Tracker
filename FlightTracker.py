import requests
def get_flight_status(api_key, airline_code, flight_number, date):
    base_url = "http://api.aviationstack.com/v1/flights"
    params = {
        "access_key": api_key,
        "flight_data": f"{airline_code}{flight_number}",
        "flight_date": date
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if "data" in data:
            flight_data = data["data"][0]
            status = flight_data["flight_status"]
            departure_airport = flight_data["departure"]["airport"]
            arrival_airport = flight_data["arrival"]["airport"]
            departure_time = flight_data["departure"]["estimated"]
            arrival_time = flight_data["arrival"]["estimated"]
            print(f"Flight number: {airline_code}{flight_number}")
            print(f"Status: {status}")
            print(f"Departing from: {departure_airport}")
            print(f"Arriving at: {arrival_airport}")
            print(f"Estimated departure time: {departure_time}")
            print(f"Estimated arrival time: {arrival_time}")
        else:
            print("Flight data could not be found. Please check the flight number and try again.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
if __name__ == "__main__":
    api_key = "YOURAPIKEY"  # Paste your aviationstack API key here.
    airline_code = input("Enter airline code (e.g. BA): ").strip().upper()
    flight_number = input("Enter your flight number (e.g. 257): ").strip()
    date = input("Enter your flight date (YYYY-MM-DD: ").strip()
    get_flight_status(api_key, airline_code, flight_number, date)
