FROM python:3.10-slim

WORKDIR /app

EXPOSE 8080

COPY . .

WORKDIR /app/grpc_client

RUN python -m pip install --upgrade pip
RUN python -m pip install -r ./requirements.txt

CMD ["python", "-u", "client.py"]