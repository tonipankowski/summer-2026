import requests
import pandas as pd

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    data = response.json()
    df = pd.json_normalize(data)
    print(df.head())
else:
    print(f"Request failed with status code {response.status_code}")
