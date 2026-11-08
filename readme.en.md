<p align="right">

[![Türkçe Oku](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-Oku-red?style=for-the-badge)](readme.md)

</p>

# Image/Media Transfer in a Microservice Architecture: REST (Base64) vs. gRPC Comparison

**Course:** Fundamental Network Protocols
**Team:**

- Sabir Süleymanlı (502531019)
- Mert Gökmen (502631009)

## Project Summary

This project aims to compare the REST and gRPC protocols in terms of network performance and resource consumption when transferring large image files (1 MB, 5 MB and 10 MB tiger photos) between microservices. The size increase and the extra CPU/memory load caused by converting images to Base64 in REST will be compared against gRPC's ability to send raw binary data directly as a stream.

## Technologies Used

- **REST Service:** Python, FastAPI
- **gRPC Service:** Python, gRPC, Protocol Buffers
- **Infrastructure:** Docker & Docker Compose
- **Load Testing and Analysis:** k6, Wireshark

## Planned Folder Structure

- `rest-service/`: FastAPI code and the REST API Dockerfile
- `grpc-service/`: gRPC code, Protobuf definitions and Dockerfile
- `load-tests/`: k6 load test scenarios
- `data/`: the 1 MB, 5 MB and 10 MB images used in the tests
- `scripts/`: Python scripts that generate the test data at exact byte sizes
- `docs/`: Wireshark .pcap captures and final reports

## Work Plan

| Week | Activity                                                                                                  |
| :--- | :-------------------------------------------------------------------------------------------------------- |
| 1    | Literature review; learning gRPC and Protocol Buffers; preparing the 1, 5 and 10 MB test images           |
| 2    | Setting up the Docker Compose skeleton; finalizing the measurement protocol and metrics                   |
| 3-4  | Developing the REST (Base64) service and the k6 scenario; early pilot Wireshark capture                   |
| 5-6  | Developing the gRPC services (unary and streaming); message size limit and chunk size tuning              |
| 7-8  | Running the full load tests; collecting pcap files and docker stats data                                  |
| 9    | Analyzing the data; preparing charts and comparison tables                                                |
| 10   | Completing the final report, the presentation and the GitHub repository                                   |
