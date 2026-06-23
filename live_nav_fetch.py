import requests
import pandas as pd

schemes = {
    "HDFC_Top_100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():
    try:
        url = f"https://api.mfapi.in/mf/{code}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            if "data" in data:
                df = pd.DataFrame(data["data"])
                df.to_csv(f"data/{name}.csv", index=False)
                print(f"{name} downloaded")

    except Exception as e:
        print(e)