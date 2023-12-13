import requests

def get_api_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        print("Bilinmeyen bir hata oluştu.")

# Özel API endpoint
ozel_api_url = "http://colormind.io/list/"

# Özel API'ye sorgu at ve çıktıyı al
ozel_api_veri = get_api_data(ozel_api_url)
print(ozel_api_veri)
