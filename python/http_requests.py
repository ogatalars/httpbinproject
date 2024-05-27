import requests

def get_public_ip():
    response = requests.get('https://httpbin.org/ip')
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': f"Falha na requisição: {response.status_code}"}
