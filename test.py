import requests
resultado = requests.get('https://www.google.com')  
print(f"Status Code: {resultado.status_code}")