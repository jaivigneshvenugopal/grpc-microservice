FROM python:3.10-slim

WORKDIR /app

EXPOSE 50051

COPY . .

WORKDIR /app/grpc_server

RUN python -m pip install --upgrade pip
RUN python -m pip install -r ./requirements.txt

CMD ["python", "-u", "server.py"]