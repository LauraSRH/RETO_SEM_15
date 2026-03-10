#RETO SEMANA 15. Uso de la API de OpenWeather: https://openweathermap.org/api/2.5/weather
# Se usa la versión 2.5, ya que la versión 3.0 no tiene el endpoint de clima 
# actual, sino el de One Call, que es de paga.

import requests

# 1. API Key y coordenadas
LAT = 26.9190
LON = -101.4170
API_KEY = "c7a06f4bb4f833b4e1c76305cd457da4"

# 2. URL correcta (Weather API v2.5)
url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}"

# 3. Hacer la petición GET
response = requests.get(url)

# 4. Verificar si la petición fue exitosa
if response.status_code == 200:
    data = response.json()
    
    print("\n=== CLIMA ACTUAL ===")
    print(f"Ciudad: {data['name']}")
    
    temp_kelvin = data["main"]["temp"]
    temp_celsius = temp_kelvin - 273.15
    print(f"Temperatura actual: {temp_celsius:.2f} °C")
    
    descripcion = data["weather"][0]["description"]
    print(f"Descripción: {descripcion.capitalize()}")
else:
    print("Error al hacer la petición:")
    print(response.status_code, response.text)

# === PRONÓSTICO PARA EL DIA EN INTERVALOS DE 3 HORAS ===
url_forecast = f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={API_KEY}"
response_forecast = requests.get(url_forecast)

if response_forecast.status_code == 200:
    forecast_data = response_forecast.json()
    print("\n=== PRONÓSTICO PARA EL DÍA (cada 3 horas) ===")
    
    # Mostrar solo las primeras 5 entradas (aprox. 15 horas)
    for item in forecast_data["list"][:5]:
        dt_txt = item["dt_txt"]
        temp_kelvin = item["main"]["temp"]
        temp_celsius = temp_kelvin - 273.15
        desc = item["weather"][0]["description"]
        print(f"{dt_txt} | {temp_celsius:.1f} °C | {desc.capitalize()}")
else:
    print("Error al obtener pronóstico:", response_forecast.status_code, response_forecast.text)

