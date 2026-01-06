# GPU 테스트용 간단한 HTTP 서버
FROM nvidia/cuda:12.2.0-base-ubuntu22.04

RUN apt-get update && apt-get install -y python3 && rm -rf /var/lib/apt/lists/*

COPY server.py /app/server.py
WORKDIR /app
EXPOSE 8080

CMD ["python3", "server.py"]
