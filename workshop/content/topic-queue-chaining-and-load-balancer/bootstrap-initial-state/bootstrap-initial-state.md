+++
title = "Bootstrap the Initial State"
weight = 31
pre = "1 "
+++


First, we will setup the initial state, including the integrating of the **Unicorn Management Service** (leveraging [Amazon API Gateway](https://aws.amazon.com/api-gateway/) and [AWS Lambda](https://aws.amazon.com/lambda/)), the **Rides Store** (leveraging [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)) and all **3 backend services** (leveraging [AWS Lambda](https://aws.amazon.com/lambda/)).

![Step 1](step-1.png)

#### 1. Browse to your AWS Cloud9 IDE

Browse to your [AWS Cloud9 Console](https://console.aws.amazon.com/cloud9/home) and select the environment called **WildRydesAsyncMessaging**.

{{%expand "Detailed description" %}}
![Step 2](step-2.png)
{{% /expand%}}

#### 2. Build the lab artifacts from source

We provide you with an [AWS SAM](https://aws.amazon.com/serverless/sam/) template which we will use to bootstrap the initial state. In the **bash tab** (at the bottom) in you **AWS Cloud9 IDE**, run the following commands to build the lab code:  

{{< highlight bash >}}
cd ~/environment/wild-rydes-async-messaging/code/lab-2
sam build

{{< /highlight >}}

{{%expand "Detailed description" %}}
![Step 4](step-4.png)
{{% /expand%}}

#### 3. Deploy the application

Now we are ready to deploy the application, by running the following command in the **lab-2** directory:  

{{< highlight bash >}}
export AWS_REGION=$(aws --profile default configure get region)
sam deploy \
    --stack-name wild-rydes-async-msg-2 \
    --capabilities CAPABILITY_IAM \
    --region $AWS_REGION \
    --guided
{{< /highlight >}}

Confirm the first 4 proposed arguments by hitting **ENTER**. When you get asked **SubmitRideCompletionFunction may not have authorization defined, Is this okay? [y/N]:**, enter `y` and hit **ENTER** again 2 times.  

#### 4. Wait until the stack is successfully deployed

It takes usually 4 minutes until the stack launched. You can monitor the progress of the **wild-rydes-async-msg-2** stack in your SAM CLI or your [AWS CloudFormation Console](https://console.aws.amazon.com/cloudformation). When the stack is launched, the status will change from **CREATE_IN_PROGRESS** to **CREATE_COMPLETE**.

{{%expand "Detailed description" %}}
![Step 7](step-7.png)
{{% /expand%}}

In the meantime while your waiting, you may want to have a look at the AWS SAM template to make yourself familiar with the stack we launched. Just click on the **template.yaml** attachment below to see the content.

{{%attachments title="Related files" pattern="/*.*(yaml)"/%}}
