"""REST (FastAPI) servisi: görüntüyü JSON içinde Base64 metni olarak alır.

Yapılan iş gRPC servisiyle birebir aynıdır:
  1) veriyi (Base64 ise önce çözerek) ham bayta çevir
  2) boyutunu ve SHA-256 özetini hesapla
  3) { size_bytes, sha256 } 
"""
import base64
import hashlib

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="REST Base64 Image Service")


class ImageUpload(BaseModel):
    filename: str
    image_base64: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/upload")
def upload(payload: ImageUpload):
    raw = base64.b64decode(payload.image_base64)
    return {
        "filename": payload.filename,
        "size_bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
    }
