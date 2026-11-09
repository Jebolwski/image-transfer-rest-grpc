import grpc
import time
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import image_pb2
import image_pb2_grpc

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGE_PATH = os.path.join(BASE_DIR, "data", "image_1mb.jpg")

def send_grpc_request():
    if not os.path.exists(IMAGE_PATH):
        print(f"Hata: {IMAGE_PATH} bulunamadı!")
        return

    # gRPC servisine bağlan (Port: 50051)
    channel = grpc.insecure_channel('localhost:50051')
    stub = image_pb2_grpc.ImageServiceStub(channel)

    with open(IMAGE_PATH, "rb") as f:
        image_bytes = f.read()

    request = image_pb2.ImageRequest(
        filename="image_1mb.jpg",
        data=image_bytes
    )

    print(f"gRPC (Binary) isteği gönderiliyor ({IMAGE_PATH})...")
    start_time = time.time()
    
    try:
        response = stub.UploadUnary(request)
        end_time = time.time()

        print(f"Başarılı! Alınan Dosya Boyutu: {response.size_bytes:,} bayt")
        print(f"Görsel SHA256 Hash'i: {response.sha256}")
        print(f"gRPC Aktarım Süresi: {end_time - start_time:.4f} saniye")
    except Exception as e:
        print(f"gRPC İletişim Hatası: {e}")

if __name__ == "__main__":
    send_grpc_request()