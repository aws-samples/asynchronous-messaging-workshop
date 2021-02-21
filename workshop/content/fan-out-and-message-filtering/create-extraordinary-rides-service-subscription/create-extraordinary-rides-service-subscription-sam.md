+++
title = "SAM"
disableToc = true
hidden = true
+++

#### 1. Update the AWS SAM template

In your Cloud9 IDE for this workshop, open the SAM template file 'wild-rydes-async-messaging/lab-1/template.yaml'. In the **Resources** section, add the definition for the Amazon SNS subscription for the **ExtraordinaryRidesService**. You can find the AWS CloudFormation documentation to do so **[here](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html)**.  
Don't forget to provide the subscription filter policy!  

{{%expand "Cheat Sheet" %}}
```yaml
  ExtraordinaryRidesServiceSubscription:
    Type: AWS::SNS::Subscription
    Properties:
      TopicArn: !Ref RideCompletionTopic
      Protocol: http
      Endpoint: !Sub "http://${ExtraordinaryRidesLoadBalancer.DNSName}"
      FilterPolicy: { "fare": [{"numeric": [">=", 50]}], "distance": [{"numeric": [">=", 20]}] }
```
{{% /expand%}}

{{%expand "Detailed description" %}}
![Step 1](step-1-sam.png)
{{% /expand%}}


#### 2. Deploy the updated AWS SAM template

Run the following command to build the lab again, after we have added the Amazon SNS subscription:

{{< highlight bash >}}
cd ~/environment/wild-rydes-async-messaging/lab-1
sam build

{{< /highlight >}}


Now we are ready to update the application, by running the following command to deploy the change:  

{{< highlight bash >}}
sam deploy \
    --guided \
    --stack-name wild-rydes-async-msg-1 \
    --capabilities CAPABILITY_IAM
{{< /highlight >}}

Confirm the first 4 proposed arguments by hitting **ENTER**. When you get asked **SubmitRideCompletionFunction may not have authorization defined, Is this okay? [y/N]:**, enter `y` and hit **ENTER** again 2 times.  

Because AWS SAM will only deploy/update/delete resources which are changed, it only takes a couple of seconds to deploy the new Amazon SNS subscription.
