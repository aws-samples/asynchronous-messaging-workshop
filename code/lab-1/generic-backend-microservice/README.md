# Build & Tag the Docker image and upload it to Amazon ECR

``` bash
$(aws ecr get-login --no-include-email --region <<REPLACE_WITH_REGION>>)

aws ecr create-repository \
    --repository-name wild-rydes/generic-backend-microservice

docker build -t wild-rydes/generic-backend-microservice .

docker tag wild-rydes/generic-backend-microservice <<REPLACE_WITH_AWS_ACCOUNT_ID>>.dkr.ecr.<<REPLACE_WITH_AWS_REGION>>.amazonaws.com/wild-rydes/generic-backend-microservice:latest

docker push <<REPLACE_WITH_AWS_ACCOUNT_ID>>.dkr.ecr.<<REPLACE_WITH_AWS_REGION>>.amazonaws.com/wild-rydes/generic-backend-microservice:latest
```

# Run und test it locally.

``` bash
docker run -it --rm -p 80:80 -e SERVICE_NAME=generic-backend-microservice wild-rydes/generic-backend-microservice
```