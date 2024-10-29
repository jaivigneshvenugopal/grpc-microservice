docker build -t grpc_client -f grpc_client/Dockerfile .
docker tag grpc_client:latest jaivigneshvenugopal/grpc_client:latest
docker push jaivigneshvenugopal/grpc_client
docker run -p 8080:8080 jaivigneshvenugopal/grpc_client