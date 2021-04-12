
```bash
sam build
```

Next, run the following command to package our Lambda function to S3:

```bash
sam package \
    --output-template-file packaged.yaml \
    --s3-bucket <BUCKET_NAME>
```

Next, the following command will create a Cloudformation Stack and deploy your SAM resources.

```bash
sam deploy \
    --template-file packaged.yaml \
    --stack-name reinvent-2019-ARC314-R-lab-3 \
    --capabilities CAPABILITY_IAM
```

> **See [Serverless Application Model (SAM) HOWTO Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-quick-start.html) for more details in how to get started.**

After deployment is complete you can run the following command to retrieve the API Gateway Endpoint URL:

```bash
aws cloudformation describe-stacks \
    --stack-name reinvent-2019-ARC314-R-lab-3 \
    --output table
```

To look up the <api-gateway-submit-instant-ride-rfq-url> to send some sample requests, execute the following command to query the RideBookingApiSubmitInstantRideRfqEndpoint parameter in Amazon CloudFormation via the CLI (or use the AWS CloudFormation Console):

```bash
aws cloudformation describe-stacks \
    --stack-name reinvent-2019-ARC314-R-lab-3 \
    --query 'Stacks[].Outputs[?OutputKey==`RideBookingApiSubmitInstantRideRfqEndpoint`][OutputValue]' \
    --output text
```

Execute the following command to send a sample request:

```bash
curl -XPOST -i -v -H "Content-Type:application/json" -d @event.json <api-gateway-submit-instant-ride-rfq-url>
``` 

Before we can query the quotes, we have to lookup the <api-gateway-query-instant-ride-rfq-url>. Execute the following command to query the RideBookingApiQueryInstantRideRfqEndpoint parameter in Amazon CloudFormation via the CLI (or use the AWS CloudFormation Console):

```bash
aws cloudformation describe-stacks \
    --stack-name reinvent-2019-ARC314-R-lab-3 \
    --query 'Stacks[].Outputs[?OutputKey==`RideBookingApiQueryInstantRideRfqEndpoint`][OutputValue]' \
    --output text
```

From the returned endpoint, replace {id} with a 'rfq-id', returned in a previous successful submit instant ride rfq request. Execute the following command to query the responses from a previous request.:

```bash
curl -i -v -H "Accept:application/json" <api-gateway-query-instant-ride-rfq-url>
``` 