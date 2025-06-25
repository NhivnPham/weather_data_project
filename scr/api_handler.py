# api_handler.py
import requests
import json
from config.config import OPENWEATHER_API_KEY

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_current_weather(city_name):
    """
    Lấy dữ liệu thời tiết hiện tại cho một thành phố cụ thể.
    """
    params = {
        "q": city_name,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"  # Lấy nhiệt độ theo độ C
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Ném lỗi cho các mã trạng thái HTTP xấu (4xx hoặc 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi lấy dữ liệu thời tiết cho {city_name}: {e}")
        return None

def get_weather_data_for_cities(city_list):
    """
    Lấy dữ liệu thời tiết hiện tại cho một danh sách các thành phố.
    """
    all_weather_data = []
    for city in city_list:
        data = get_current_weather(city)
        if data:
            all_weather_data.append(data)
            print(f"Đã lấy dữ liệu thời tiết cho: {city}")
        else:
            print(f"Không thể lấy dữ liệu cho: {city}")
    return all_weather_data

if __name__ == '__main__':
    # Ví dụ sử dụng
    city_example = "Ho Chi Minh City"
    weather_data = get_current_weather(city_example)
    if weather_data:
        print(json.dumps(weather_data, indent=4))