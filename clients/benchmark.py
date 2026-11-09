import os
import sys
import time
import base64
import requests
import grpc

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import image_pb2
import image_pb2_grpc

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REST_URL = "http://localhost:8000/upload"

GRPC_OPTIONS = [
    ('grpc.max_send_message_length', 20 * 1024 * 1024),
    ('grpc.max_receive_message_length', 20 * 1024 * 1024),
]

FILES = [
    ("1 MB", "image_1mb.jpg"),
    ("5 MB", "image_5mb.jpg"),
    ("10 MB", "image_10mb.jpg")
]

def test_rest(image_path):
    with open(image_path, "rb") as f:
        image_bytes = f.read()
    
    start_time = time.time()
    base64_encoded = base64.b64encode(image_bytes).decode('utf-8')
    payload = {
        "filename": os.path.basename(image_path),
        "image_base64": base64_encoded  # FastAPI'nin beklediği anahtar ismi
    }
    
    try:
        response = requests.post(REST_URL, json=payload)
        end_time = time.time()
        
        if response.status_code == 200:
            return end_time - start_time
        else:
            print(f"\n[REST Hata - {os.path.basename(image_path)}] Kod: {response.status_code}, Detay: {response.text[:100]}")
            return None
    except Exception as e:
        print(f"\n[REST Bağlantı Hatası]: {e}")
        return None

def test_grpc(image_path):
    channel = grpc.insecure_channel('localhost:50051', options=GRPC_OPTIONS)
    stub = image_pb2_grpc.ImageServiceStub(channel)

    with open(image_path, "rb") as f:
        image_bytes = f.read()

    request = image_pb2.ImageRequest(
        filename=os.path.basename(image_path),
        data=image_bytes
    )

    try:
        start_time = time.time()
        response = stub.UploadUnary(request)
        end_time = time.time()

        if response.size_bytes > 0:
            return end_time - start_time
        else:
            return None
    except Exception as e:
        print(f"\n[gRPC Hata - {os.path.basename(image_path)}]: {e}")
        return None

def main():
    print("=" * 65)
    print(f"{'BOYUT':<10} | {'REST (Base64)':<18} | {'gRPC (Unary)':<18} | {'FARK / HIZ':<12}")
    print("=" * 65)

    for label, filename in FILES:
        image_path = os.path.join(BASE_DIR, "data", filename)
        if not os.path.exists(image_path):
            print(f"{label:<10} | Dosya bulunamadı ({filename})")
            continue

        rest_time = test_rest(image_path)
        grpc_time = test_grpc(image_path)

        rest_str = f"{rest_time:.4f} sn" if rest_time else "HATA"
        grpc_str = f"{grpc_time:.4f} sn" if grpc_time else "HATA"
        
        if rest_time and grpc_time:
            diff_percent = ((rest_time - grpc_time) / rest_time) * 100
            diff_str = f"%{diff_percent:.1f} daha hızlı"
        else:
            diff_str = "-"

        print(f"{label:<10} | {rest_str:<18} | {grpc_str:<18} | {diff_str:<12}")

    print("=" * 65)

if __name__ == "__main__":
    main()