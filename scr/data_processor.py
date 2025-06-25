# data_processor.py
import pandas as pd
from datetime import datetime
import os

def extract_weather_info(raw_data):
    """
    Trích xuất thông tin thời tiết quan trọng từ dữ liệu JSON thô.
    """
    extracted_data = []
    for data in raw_data:
        if data:
            try:
                city_name = data['name']
                country = data['sys']['country']
                temperature = data['main']['temp']
                feels_like = data['main']['feels_like']
                temp_min = data['main']['temp_min']
                temp_max = data['main']['temp_max']
                humidity = data['main']['humidity']
                pressure = data['main']['pressure']
                weather_description = data['weather'][0]['description']
                wind_speed = data['wind']['speed']
                cloudiness = data['clouds']['all']
                timestamp = datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')

                extracted_data.append({
                    'Timestamp': timestamp,
                    'City': city_name,
                    'Country': country,
                    'Temperature_C': temperature,
                    'FeelsLike_C': feels_like,
                    'MinTemp_C': temp_min,
                    'MaxTemp_C': temp_max,
                    'Humidity_percent': humidity,
                    'Pressure_hPa': pressure,
                    'WeatherDescription': weather_description,
                    'WindSpeed_mps': wind_speed,
                    'Cloudiness_percent': cloudiness
                })
            except KeyError as e:
                print(f"Lỗi khi trích xuất dữ liệu: Thiếu khóa '{e}' trong dữ liệu: {data}")
    return extracted_data

def save_to_csv(data_frame, file_path="data/weather_data.csv"):
    """
    Lưu DataFrame vào tệp CSV. Nếu tệp tồn tại, sẽ nối thêm dữ liệu.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    if os.path.exists(file_path):
        data_frame.to_csv(file_path, mode='a', header=False, index=False, encoding='utf-8')
        print(f"Dữ liệu đã được nối thêm vào {file_path}")
    else:
        data_frame.to_csv(file_path, index=False, encoding='utf-8')
        print(f"Dữ liệu đã được lưu vào {file_path}")

def load_data_from_csv(file_path="data/weather_data.csv"):
    """
    Tải dữ liệu từ tệp CSV vào DataFrame.
    """
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        print(f"Tệp {file_path} không tồn tại.")
        return pd.DataFrame()

if __name__ == '__main__':
    # Ví dụ cách sử dụng (cần dữ liệu thô từ api_handler)
    # Đây chỉ là ví dụ minh họa, bạn cần chạy api_handler trước
    sample_raw_data = [
        {
            "coord": {"lon": 106.6667, "lat": 10.75},
            "weather": [{"id": 801, "main": "Clouds", "description": "few clouds", "icon": "02n"}],
            "base": "stations",
            "main": {"temp": 28.99, "feels_like": 33.37, "temp_min": 28.99, "temp_max": 28.99, "pressure": 1011, "humidity": 83},
            "visibility": 10000, "wind": {"speed": 2.57, "deg": 190}, "clouds": {"all": 20}, "dt": 1700000000,
            "sys": {"type": 1, "id": 7984, "country": "VN", "sunrise": 1699991200, "sunset": 1700034400},
            "timezone": 25200, "id": 1566083, "name": "Ho Chi Minh City", "cod": 200
        }
    ]
    extracted = extract_weather_info(sample_raw_data)
    if extracted:
        df = pd.DataFrame(extracted)
        print("Dữ liệu đã trích xuất:")
        print(df)
        save_to_csv(df, "data/sample_weather_data.csv")