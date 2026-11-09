FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Proto dosyasını doğrudan konteyner içindeki kütüphane sürümleriyle derliyoruz
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. image.proto

EXPOSE 50051

CMD ["python", "server.py"]