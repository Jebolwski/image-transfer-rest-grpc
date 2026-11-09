import requests
import base64
import time
import os

# Scriptin bulunduğu konuma göre ana dizindeki data klasörünü buluyoruz
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGE_PATH = os.path.join(BASE_DIR, "data", "image_1mb.jpg")

URL = "http://localhost:8000/upload"

def send_rest_request():
    if not os.path.exists(IMAGE_PATH):
        print(f"Hata: {IMAGE_PATH} bulunamadı!")
        return

    with open(IMAGE_PATH, "rb") as f:
        image_bytes = f.read()
    
    base64_encoded = base64.b64encode(image_bytes).decode('utf-8')
    
    payload = {
        "filename": "image_1mb.jpg",
        "image_data": base64_encoded
    }

    print(f"REST (Base64) isteği gönderiliyor ({IMAGE_PATH})...")
    start_time = time.time()
    
    try:
        response = requests.post(URL, json=payload)
        end_time = time.time()

        print(f"Durum Kodu: {response.status_code}")
        print(f"Yanıt: {response.json()}")
        print(f"REST Aktarım Süresi: {end_time - start_time:.4f} saniye")
    except Exception as e:
        print(f"İstek Hatası: {e}")

if __name__ == "__main__":
    send_rest_request()