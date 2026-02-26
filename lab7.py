import requests
import json 



# №1
print("№1 Реализуйте программу, которая показывает погоду, влажность и давление в указанном городе.")


WEATHER_API_KEY = "3ab9cf79a11ef582d526620ee8eac09c"


def weather_loc(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={WEATHER_API_KEY}"

    response = requests.get(url)
    data = response.json()

    return data["weather"][0]["description"], data["main"]["pressure"], data["main"]["humidity"]


if __name__ == '__main__':
    city_name = input('Enter city name:')
    weather, pressure, humidity = weather_loc(city_name)

    print(f' Weather in {city_name}: \n Weather - {weather} \n Atmospheric pressure - {pressure} Hectopascal  \n Humidity - {humidity}%')




# №2
print("№2 Реализуйте программу, которая показывает список праздников в указанной стране и году.")


API_KEY = "e2547e57-4f08-4619-8624-6bc109ea3c8c"


def holidays_info(country_index, year):
    url = f"https://holidayapi.com/v1/holidays?pretty&key={API_KEY}&country={country_index}&year={year}"

    response = requests.get(url)
    data = response.json()
    
    print(f'Total in {data["holidays"][0]["country"]} {len(data["holidays"])} holidays in {year}:')
    for i in range(len(data["holidays"])):
        print(f'№{i+1} - "{data["holidays"][i]["name"]}"  \n    Date - {data["holidays"][i]["date"]} ({data["holidays"][i] ["weekday"]["date"]["name"]})')
    

if __name__ == '__main__':
    country_index = input('Enter country index: ')
    year = input('Enter desired year: ')
    
    holidays_info(country_index, year)