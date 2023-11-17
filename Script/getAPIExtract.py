import requests
import json
from datetime import datetime

api_url = "https://api.tomorrow.io/v4/weather/forecast"
api_key = "JhXdXXNEQoVnVtRemAcisMjl2djZJEUg"

params = {
    "location": "10.7769,106.7009",
    "timesteps": "1d",
    "apikey": api_key
}

response = requests.get(api_url, params=params)

if response.status_code == 200:
    current_date = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    save_directory = r"D:\hk1nam4\warehouse\weatherDataStaging"
    file_name = fr"{save_directory}\weather_forecast_{current_date}.json"
    with open(file_name, "w") as json_file:
        json.dump(response.json(), json_file, indent=4)
    print(f"Dữ liệu đã được lưu vào {file_name}")
else:
    print("Yêu cầu không thành công. Mã trạng thái:", response.status_code)

