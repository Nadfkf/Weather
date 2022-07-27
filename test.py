# # http://api.openweathermap.org/data/2.5/weather?q={msg.text}&lang=ru&appid={WEATHER_TOKEN}&units=metric
# import requests

# city = input('Enter the name of city')
# token = input("Enter the token")
# link = f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&appid={token}&units=metric"

# req = requests.get(link).json()
# print(req)


dict_ = {'1234': {'5678' : 90123}}
print(dict_['1234']['5678'])