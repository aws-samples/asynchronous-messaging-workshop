+++
title = "Test Topic-Queue Chaining & Load Balancing"

weight = 37
pre = "7 "
+++

In this step, we will validate that the Amazon SNS topic is publishing all messages to all subscribers. Because a subscriber can also fail processing a message, we also want to validate that Amazon SNS is redelivering the message, so that we will not miss a single message.

#### 1. Look up the API Gateway endpoint

To look-up the API Gateway endpoint URL for the submit-ride-completion function, run the following command:  

```bash
aws cloudformation describe-stacks \
    --stack-name wild-rydes-async-msg-2 \
    --query 'Stacks[].Outputs[?OutputKey==`UnicornManagementServiceApiSubmitRideCompletionEndpoint`].OutputValue' \
    --output text
```


#### 2. Send a couple requests to the Unicorn Management Service

Let's store this API Gateway endpoint URL in an environment variable, so we don't have to repeat it all the time:

```bash
export ENDPOINT=$(aws cloudformation describe-stacks \
    --stack-name wild-rydes-async-msg-2 \
    --query 'Stacks[].Outputs[?OutputKey==`UnicornManagementServiceApiSubmitRideCompletionEndpoint`].OutputValue' \
    --output text)
```

To send a couple requests to the **submit ride completion endpoint**, execute the command below 5 or more times and change the request payload to test the filter criteria for the **Extraordinary Rides Service**:  

```bash
curl -XPOST -i -H "Content-Type:application/json" -d '{ "from": "Berlin", "to": "Frankfurt", "duration": 420, "distance": 600, "customer": "cmr", "fare": 256.50 }' $ENDPOINT
```

{{%expand "Detailed description" %}}
![Step 1](step-1.png)
{{% /expand%}}


#### 3. Validate the message reception

Go to your [Amazon CloudWatch Log console](https://console.aws.amazon.com/cloudwatch/home?#logs:prefix=/aws/lambda/wild-rydes-async-msg-2) and lookup all **Log Groups** with the prefix `/aws/lambda/wild-rydes-async-msg-2`.

{{%expand "Detailed description" %}}
![Step 2](step-2.png)
{{% /expand%}}

Click one the name of the Log Groups to see all **Log Streams** available for this Log Group.

{{%expand "Detailed description" %}}
![Step 3](step-3.png)
{{% /expand%}}

Browse the most recent Log Streams to validate, that it could successfully process the message. You should also see some log entries, indicating a failed message processing. Shortly after, you should see the message redelivery from Amazon SNS and the successful message processing log entry.  

{{%expand "Detailed description" %}}
![Step 4](step-4.png)
{{% /expand%}}

Browse all Log Groups to validate, that each of our 5 backend service could successfully process the message. 
