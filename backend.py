import requests

API_KEY = "884ca8a3b79da35ccfe2131a7b160423"


def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    return content


if __name__ == "__main__":
    print(get_data(place="Tokyo"))