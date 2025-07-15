

print("\nImportação e uso de módulos de terceiros\n")
import requests

url = "https://www.example.com"
response = requests.get(url)
print(f"Solicitação HTTP para {url} retornou o status: {response.status_code}")