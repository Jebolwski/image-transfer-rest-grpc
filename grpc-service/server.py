"""gRPC servisi: görüntüyü ham bayt olarak (unary veya akış) alır.

REST servisiyle aynı işi yapar: boyut + SHA-256 hesaplar.
"""
import hashlib
import os
from concurrent import futures

import grpc

import image_pb2
import image_pb2_grpc

PORT = int(os.environ.get("GRPC_PORT", "50051"))
MAX_WORKERS = int(os.environ.get("GRPC_MAX_WORKERS", "10"))
# Unary için 10 MB'lık görüntü + başlık payı sığmalı (varsayılan alma limiti 4 MB).
MAX_MESSAGE_BYTES = int(os.environ.get("GRPC_MAX_MESSAGE_MB", "16")) * 1024 * 1024


class ImageService(image_pb2_grpc.ImageServiceServicer):
    def UploadUnary(self, request, context):
        return image_pb2.ImageReply(
            size_bytes=len(request.data),
            sha256=hashlib.sha256(request.data).hexdigest(),
        )

    def UploadStream(self, request_iterator, context):
        digest = hashlib.sha256()
        size = 0
        for chunk in request_iterator:
            size += len(chunk.data)
            digest.update(chunk.data)
        return image_pb2.ImageReply(size_bytes=size, sha256=digest.hexdigest())


def serve():
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=MAX_WORKERS),
        options=[
            ("grpc.max_receive_message_length", MAX_MESSAGE_BYTES),
            ("grpc.max_send_message_length", MAX_MESSAGE_BYTES),
        ],
    )
    image_pb2_grpc.add_ImageServiceServicer_to_server(ImageService(), server)
    server.add_insecure_port(f"0.0.0.0:{PORT}")
    server.start()
    print(f"gRPC server listening on :{PORT} (max message {MAX_MESSAGE_BYTES // 1024 // 1024} MB)", flush=True)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
