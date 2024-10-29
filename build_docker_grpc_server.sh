docker build -t grpc_server -f grpc_server/Dockerfile .
docker tag grpc_server:latest jaivigneshvenugopal/grpc_server:latest
docker push jaivigneshvenugopal/grpc_server
docker run -p 50551:50551 jaivigneshvenugopal/grpc_server