+++
title = "Console"
disableToc = true
hidden = true
+++

#### 1. Create a new subscription

After selecting the topic **RideCompletionTopic**, click the **Create subscription** button in the bottom right corner.

{{%expand "Detailed description" %}}
![Step 1](step-1-console.png)
{{% /expand%}}

#### 2. Configure the subscription

In the next page, select **HTTP** as the subscription protocol.  

To look-up the subscription endpint, navigate back to your CloudFormation console, select the stack **wild-rydes-async-msg-1** and select the **Outputs** tab. Select the value, corresponding to the key **CustomerNotificationServiceLBURL**. It should look similar like **http://cnslb-...elb.amazonaws.com**.  
You can also look-up the value by running the following command:  
```bash
aws cloudformation describe-stacks \
    --stack-name wild-rydes-async-msg-1 \
    --query 'Stacks[].Outputs[?OutputKey==`CustomerNotificationServiceLBURL`].OutputValue' \
    --output text
```

Click **Create subscription** to create the subscription.

{{%expand "Detailed description" %}}
![Step 2](step-2-console.png)
{{% /expand%}}


#### 3. Confirm the subscription

**Amazon SNS** require a confirmation of a subscription, before it publishes messages to that endpoint, as described **[here](https://docs.aws.amazon.com/sns/latest/dg/sns-http-https-endpoint-as-subscriber.html#SendMessageToHttp.confirm)**.  
Our provided Customer Notification Service handles this automatically for us. The **Status** will change to **Confirmed** immediately (may refresh the page a couple of times). There is nothing to do for you in this step.  

{{%expand "Detailed description" %}}
![Step 3](step-3-console.png)
{{% /expand%}}

But if you are curious how this can be done, keep reading...

{{% notice tip %}}
**How to confirm a subscription to Amazon SNS via HTTP(S) automatically?**  
Amazon SNS will send an HTTP(S) POST request to the subscription endpoint. The request payload is a JSON document as described **[here](https://docs.aws.amazon.com/sns/latest/dg/sns-http-https-endpoint-as-subscriber.html#SendMessageToHttp.confirm)**. It contains a 'SubscribeURL' attribute with an URL you have to request, to confirm the subscription. If you are using Python, this can be done in the following way:  

```python
def confirm_subscription(data):
    request_body = json.loads(data)
    subscribe_url = request_body['SubscribeURL']
    # issue a GET request to the subscribe confirmation url
    requests.get(subscribe_url)
    app.logger.info("subscription confirmed")
    return
```
{{% /notice %}}

Now you are may wondering how to verify, the request is really coming from Amazon SNS and not somebody else, as your endpoint is publicly available. If this is the case, keep reading...

{{% notice tip %}}
**How to verify the HTTP(S) request is really coming from Amazon SNS?**  
As your endpoint is publicly available, it can be call by everyone. To verify the request is really coming from Amazon SNS, you can validate the request signature which is part of the request payload as described **[here](https://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.verify.signature.html)**. In case you are using Python, you can do it in the following way:  

```python
def is_invalidate_sns_signature(request):
    # TODO: implement the sns signature verification to make sure the message comes from Amazon SNS
    return False
```
{{% /notice %}}
