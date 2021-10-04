+++
title = "SAM"
disableToc = true
hidden = true
+++

#### 1. Update the AWS SAM template

In your Cloud9 IDE for this workshop, open the SAM template file `wild-rydes-async-messaging/lab-1/template.yaml`. In the **Resources** section, uncomment the Amazon SNS event source for the **CustomerNotificationFunction**. You can find the AWS SAM documentation to do so **[here](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-sns.html)**.

{{%expand "Cheat Sheet" %}}
```yaml
Events:
  SNSEvent:
    Type: SNS
    Properties:
      Topic: !Ref RideCompletionTopic
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
sam deploy
{{< /highlight >}}

**Note:** you do not need to provide the arguments for the deployment, because AWS SAM saved the parameter values in a configuration file called **samconfig.toml**. See the **[documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-config.html)** more information on the AWS SAM CLI configuration file.

Because AWS SAM will only deploy/update/delete resources which are changed, it only takes a couple of seconds to deploy the new Amazon SNS topic.
