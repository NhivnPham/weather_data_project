# data_analyzer.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_weather_data(df):
    """
    Thực hiện các phân tích cơ bản trên DataFrame thời tiết.
    """
    if df.empty:
        print("Không có dữ liệu để phân tích.")
        return

    print("\n--- Phân tích dữ liệu thời tiết ---")
    print(f"Tổng số bản ghi: {len(df)}")
    print("\nThống kê mô tả:")
    print(df.describe())

    print("\nNhiệt độ trung bình theo thành phố:")
    print(df.groupby('City')['Temperature_C'].mean().sort_values(ascending=False))

    print("\nĐộ ẩm trung bình theo thành phố:")
    print(df.groupby('City')['Humidity_percent'].mean().sort_values(ascending=False))

    print("\nCác mô tả thời tiết phổ biến nhất:")
    print(df['WeatherDescription'].value_counts())

def visualize_data(df, plot_dir="plots"):
    """
    Tạo các biểu đồ để trực quan hóa dữ liệu.
    """
    if df.empty:
        print("Không có dữ liệu để trực quan hóa.")
        return

    os.makedirs(plot_dir, exist_ok=True)

    print("\n--- Trực quan hóa dữ liệu ---")

    # Biểu đồ nhiệt độ trung bình theo thành phố
    plt.figure(figsize=(12, 6)) # Dòng này sẽ tạo một figure mới
    # Tính toán nhiệt độ trung bình cho mỗi thành phố
    avg_temp_by_city = df.groupby('City')['Temperature_C'].mean().reset_index()
    sns.barplot(x='City', y='Temperature_C', data=avg_temp_by_city)
    plt.title('Nhiệt độ trung bình theo thành phố')
    plt.xlabel('Thành phố')
    plt.ylabel('Nhiệt độ (°C)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(plot_dir, 'average_temperature_by_city.png'))
    plt.show()

if __name__ == '__main__':
    # Ví dụ cách sử dụng (cần DataFrame đã được xử lý)
    # Giả định bạn đã có một tệp CSV được tạo từ data_processor.py
    from data_processor import load_data_from_csv
    df_example = load_data_from_csv("data/sample_weather_data.csv") # Thay đổi nếu tên tệp khác
    if not df_example.empty:
        analyze_weather_data(df_example)
        visualize_data(df_example)
    else:
        print("Không thể tải dữ liệu mẫu để phân tích và trực quan hóa.")