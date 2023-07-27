import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_flight_details(airline_code, flight_number, date, month, year):
   def get_data(url):
      response = requests.get(url)
      return response.text
   url = f"https://www.flightstats.com/v2/flight-tracker/{airline_code}/{flight_number}?year={year}&month={month}&date={date}"
   html_data = get_data(url)
   soup = BeautifulSoup(html_data, 'html.parser')
   return soup
def get_airport_names(soup):
   airport_names = [
      i.get_text()
      for i in soup.find_all(
         "div", class_="text-helper__TextHelper-sc-8bko4a-0"
      )
   ]
   print("Flight number:", airport_names[0])
   print("Flight name:", airport_names[1])
   print("From:", airport_names[2], airport_names[3])
   print("To:", airport_names[4], airport_names[5])
def get_flight_status(soup):
   gates = [
      data.get_text()
      for data in soup.find_all(
         "div",
         class_="ticket__TGBLabel-s1rrbl5o-15 gcbyEH text-helper__TextHelper-sc-8bko4a-0 efwouT",
      )
   ]
   gate_numbers = [
      data.get_text()
      for data in soup.find_all(
         "div",
         class_="ticket__TGBValue-sc-1rrbl5o-16 hUgYLc text-helper__TextHelper-sc-8bko4a-0 kbHzdx",
      )
   ]
   statuses = [
      i.get_text()
      for i in soup.find_all(
         "div", class_="text-helper__TextHelper-sc-8bko4a-0 feVjck"
      )
   ]
   time_statuses = [
      i.get_text()
      for i in soup.find_all(
         "div", class_="text-helper__TextHelper-sc-8bko4a-0 kbHzdx"
      )
   ]
   print("Gate number:", gate_numbers[0])
   print("Status:", statuses[0])
   print(f"Flight timings: {time_statuses[0]} to {time_statuses[2]}")
airline_code = 'BA' # Input parameters
flight_number = '257' # Input parameters
current_date = datetime.now()
date = str(current_date.day+1)
month = str(current_date.month)
year = str(current_date.year)
soup = get_flight_details(airline_code, flight_number, date, month, year)
get_airport_names(soup)
get_flight_status(soup)
