# para instalar usando o pip
# para usar o modulo requests usa-se o comando pip3 install requests
print("\nImportação e uso de um módulo de terceiro")
from requests import get

url = "https://www.example.com"

response = get(url)
print(f"Solicitacao HTTP para {url} retornou o status {response.status_code}")