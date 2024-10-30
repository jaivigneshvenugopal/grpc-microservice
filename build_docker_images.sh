docker build -t grpc_server -f grpc_server/Dockerfile .
docker tag grpc_server:latest jaivigneshvenugopal/grpc_server:latest
docker push jaivigneshvenugopal/grpc_server
# docker run --name grpc_server -p 50551:50551 jaivigneshvenugopal/grpc_server
# docker run --name grpc_server -p 50551:50551 grpc_server

docker build -t grpc_client -f grpc_client/Dockerfile .
docker tag grpc_client:latest jaivigneshvenugopal/grpc_client:latest
docker push jaivigneshvenugopal/grpc_client
# docker run --name grpc_client -p 8080:8080 jaivigneshvenugopal/grpc_client