+++
title = "Test Scatter-Gather"
weight = 42
pre = "2 "
+++

### 1. Get API Gateway endpoint to send request for quotes
The lab 3 SAM template created two separate API gateway endpoints. They will be shown under the outputs tab of the cloudformation stack once deployment is completed. **RideBookingApiSubmitInstantRideRfqEndpoint** is the API endpoint to submit request for quotes and **RideBookingApiQueryInstantRideRfqEndpoint** is used to query the response from various ride operators. You can run the following command to retrieve the **RideBookingApiSubmitInstantRideRfqEndpoint** API Gateway Endpoint URL.

{{< highlight bash >}}
aws cloudformation describe-stacks \
    --stack-name wild-rydes-async-msg-3 \
    --query 'Stacks[].Outputs[?OutputKey==`RideBookingApiSubmitInstantRideRfqEndpoint`][OutputValue]' \
    --output text
{{< /highlight >}}

Let's store this request API Gateway endpoint URL in an environment variable, so we don't have to repeat it all the time:

```bash
export REQ_ENDPOINT=$(aws cloudformation describe-stacks \
    --stack-name wild-rydes-async-msg-3 \
    --query 'Stacks[].Outputs[?OutputKey==`RideBookingApiSubmitInstantRideRfqEndpoint`].OutputValue' \
    --output text)
```
### 2. Send the request for quotes

The trigger point of the flow is a request message that is sent to get the quote. The following is the structure of the request event message.
{{< highlight bash >}}
{
    "from": "Frankfurt",
    "to": "Las Vegas",
    "customer": "cmr"
}
{{< /highlight >}}


The from tag represents the starting point and to indicates the destination. The customer is an id for the end ussr. 
Execute the below commands to send a request for quote.

{{< highlight bash >}}

curl -XPOST -i -v -H "Content-Type:application/json" -d @event.json $REQ_ENDPOINT
{{< /highlight >}}

The output will have a **rfq-id** parameter. Save the value in a notepad as it will be used later to query the responses.

{{%expand "Screenshot" %}}
![Step 4](lab-3-step-8.png)
{{% /expand%}}

### 3. Get API Gateway endpoint to query responses
Before we can query the quotes, we have to lookup the response query endpoint. Execute the following command to query the **RideBookingApiQueryInstantRideRfqEndpoint** output in Amazon CloudFormation stack via the CLI:

{{< highlight bash >}}
aws cloudformation describe-stacks \
    --stack-name wild-rydes-async-msg-3 \
    --query 'Stacks[].Outputs[?OutputKey==`RideBookingApiQueryInstantRideRfqEndpoint`][OutputValue]' \
    --output text
{{< /highlight >}}

Let's store this request API Gateway endpoint URL in an environment variable, so we don't have to repeat it all the time:

```bash
export RES_ENDPOINT=$(aws cloudformation describe-stacks \
    --stack-name wild-rydes-async-msg-3 \
    --query 'Stacks[].Outputs[?OutputKey==`RideBookingApiQueryInstantRideRfqEndpoint`].OutputValue' \
    --output text | cut -d'{' -f 1)
```


### 4. Query the RFQ response endpoint
Replace the **<<rfq-id>>** in the below command with the value that was received in step 2. This is the correlation id to get the response quotes for the request that was sent. Execute the following command to query the responses:

{{< highlight bash >}}

curl -i -v -H "Accept:application/json" ${RES_ENDPOINT}<<rfq-id>>
{{< /highlight >}}

The above call invokes a lambda function via API gateway end point. It queries the DynamoDB table to get the responses corresponding to the request id. The response will be a json payload showing the response quotes from different providers. A sample response is shown below:
{{< highlight bash >}}
{
  "quotes": [
    {
      "responder": "UnicornManagementResource10",
      "quote": "45"
    },
    {
      "responder": "UnicornManagementResource2",
      "quote": "100"
    }
  ],
  "rfq-id": "8b095f9e-cffc-4790-91a6-28353fa30e42",
  "from": "Frankfurt",
  "to": "Las Vegas",
  "customer": "cmr"
}
{{< /highlight >}}
It shows the response quotes from two service providers. The function will need to be called in regular intervals if the service providers send responses at different times. You can also check the responses in the DynamoDB directly by querying based on the request id.
{{% notice tip %}}
**How to verify the data is actually coming from DynamoDB?**  
All responses for the quotes are received in a SQS queue. A lambda function receives the messages and stages them in a DynamoDB table. You can verify the response data by accessing the DynamoDB table in your specific region.
**Oregon** | [Click here](https://us-west-2.console.aws.amazon.com/dynamodb/home?region=us-west-2#tables:) | 
**Ohio** | [Click here](https://us-east-2.console.aws.amazon.com/dynamodb/home?region=us-east-2#tables:) | 
**Singapore** | [Click here](https://ap-southeast-1.console.aws.amazon.com/dynamodb/home?region=ap-southeast-1#tables:) | 
**Sydney** | [Click here](https://ap-southeast-2.console.aws.amazon.com/dynamodb/home?region=ap-southeast-2#tables:) | 
**Frankfurt** | [Click here](https://eu-central-1.console.aws.amazon.com/dynamodb/home?region=eu-central-1#tables:) | 
**Ireland** | [Click here](https://eu-west-1.console.aws.amazon.com/dynamodb/home?region=eu-west-1#tables:) | 
{{% /notice %}}
