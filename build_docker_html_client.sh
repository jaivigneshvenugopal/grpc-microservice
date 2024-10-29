docker build -t html_client -f html_client/Dockerfile .
docker tag html_client:latest jaivigneshvenugopal/html_client:latest
docker push jaivigneshvenugopal/html_client
docker run --name html_client -p 80:80 jaivigneshvenugopal/html_client