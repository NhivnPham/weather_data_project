# main.py
from scr.api_handler import get_weather_data_for_cities
from scr.data_processor import extract_weather_info, save_to_csv, load_data_from_csv
from scr.data_analyzer import analyze_weather_data, visualize_data
import pandas as pd

def run_weather_data_project():
    """
    Chạy toàn bộ quy trình: lấy dữ liệu, xử lý, lưu, phân tích và trực quan hóa.
    """
    cities = ["Ho Chi Minh City", "Hanoi", "Da Nang", "Can Tho", "Hue", "Vung Tau", "Ca Mau", "Bac Lieu"] # Thêm/bớt các thành phố bạn muốn
    print("--- Bắt đầu lấy dữ liệu thời tiết ---")
    raw_weather_data = get_weather_data_for_cities(cities)

    if raw_weather_data:
        print("\n--- Đang xử lý dữ liệu ---")
        extracted_data = extract_weather_info(raw_weather_data)
        if extracted_data:
            df = pd.DataFrame(extracted_data)
            print("\nDữ liệu đã trích xuất:")
            print(df.head())

            print("\n--- Lưu dữ liệu vào CSV ---")
            save_to_csv(df, "data/weather_data.csv")

            print("\n--- Đang tải dữ liệu từ CSV để phân tích ---")
            df_loaded = load_data_from_csv("data/weather_data.csv")
            if not df_loaded.empty:
                # Đảm bảo cột Timestamp là datetime để phân tích theo thời gian nếu cần
                df_loaded['Timestamp'] = pd.to_datetime(df_loaded['Timestamp'])

                print("\n--- Bắt đầu phân tích dữ liệu ---")
                analyze_weather_data(df_loaded)

                print("\n--- Bắt đầu trực quan hóa dữ liệu ---")
                visualize_data(df_loaded)
            else:
                print("Không có dữ liệu để phân tích và trực quan hóa sau khi tải từ CSV.")
        else:
            print("Không có dữ liệu được trích xuất từ phản hồi API.")
    else:
        print("Không thể lấy dữ liệu thời tiết từ API.")

if __name__ == '__main__':
    run_weather_data_project()