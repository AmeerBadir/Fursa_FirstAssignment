import numpy as np
import matplotlib.pyplot as plt
import requests
import pandas as pd
import  datetime as dt
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

def get_lat_lon(location):
    lat_lon_url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=5&appid={API_KEY}"
    response = requests.get(lat_lon_url)
    data = response.json()
    return data[0]["lat"], data[0]["lon"]


def getCurrentWeatherTemperature(data):
    current_dt = dt.datetime.fromtimestamp(data["current"]["dt"],dt.UTC).today()
    current_temp = data["current"]["temp"]
    timezone_offset = dt.datetime.fromtimestamp(data["timezone_offset"],dt.UTC).time()
    taple = ({'current dt': [current_dt],'current_temp': [current_temp],'lat':[data["lat"]],'lon':[data["lon"]],
              'timezone':[data["timezone"]],'timezone offset':[timezone_offset] })
    pf_current =pd.DataFrame(taple)
    # pf_current.plot()
    pf_current.plot(marker = 'o')
    plt.show()
    return pf_current


def getDailyWeatherTemperature(data):
    daily_days = []
    dayily_temp = []
    for i  in data["daily"] :
        daily_days.append(str(dt.datetime.fromtimestamp(i['dt'],dt.UTC).day))
        dayily_temp.append(i["temp"]["day"])
    return daily_days,dayily_temp


def getHourlyWeatherTemperature(data):

    hourly_hour = []
    hourly_temp = []
    for i  in data["hourly"] :
        hourly_hour.append(str(dt.datetime.fromtimestamp(i['dt'],dt.UTC).hour))
        hourly_temp.append(i["temp"])
    hourly_hour =hourly_hour[:24]
    hourly_temp = hourly_temp[:24]
    return hourly_hour,hourly_temp


#
# plt.plot(hourly_hour, hourly_temp)
# plt.show()
# print(pf)
# for i in data["current"]:
#     print(i)
# print(data["current"])
# print(data["current"][0].keys())
# print(data["daily"][0].keys())
# print(data["hourly"][0].keys())
#
if __name__ == '__main__':
    city = input("Enter City:")
    # city = "london"
    API_KEY = "3501a5c58cd41d6c889ab196d5561c15"
    lat,lon = get_lat_lon(city)
    URL = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
    data = requests.get(URL).json()
    currentWeather = getCurrentWeatherTemperature(data)
    hourly_hour,hourly_temp = getHourlyWeatherTemperature(data)
    daily_days,dayily_temp = getDailyWeatherTemperature(data)
    plt.subplot(1, 2, 1)
    plt.plot( np.array(daily_days),np.array(dayily_temp))
    plt.xlabel("Days",fontdict = font2)
    plt.ylabel("Days Temperatures",fontdict = font2)
    plt.title("Daily Temperatures",fontdict = font1)
    plt.subplot(1, 2, 2)
    plt.plot(hourly_hour, hourly_temp)
    plt.xlabel("Hours",fontdict = font2)
    plt.ylabel("Hours Temperatures",fontdict = font2)
    plt.title("Hourly Temperatures",fontdict = font1)
    plt.show()


