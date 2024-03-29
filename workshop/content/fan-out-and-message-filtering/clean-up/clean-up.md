+++
title = "Clean up"
weight = 28
pre = "8 "
+++

In this step, we will clean up all resources, we created during this lab, so that no further cost will occur.

#### 1. Delete the previously created IAM Inline Policies

In your Amazon IAM console, select **[Roles](https://console.aws.amazon.com/iamv2/home#/roles)** in the left navigation. In the search field, enter "async-msg". Open all matching roles and delete the previously created inline policies by clicking the "x" right to the policy name.

#### 2. Delete the AWS SAM template

In your Cloud9 IDE, run the following command to delete the resources we created with our AWS SAM template:

{{< highlight bash >}}
cd ~/environment/wild-rydes-async-messaging/lab-1
aws cloudformation delete-stack \
    --stack-name wild-rydes-async-msg-1

{{< /highlight >}}


#### 3. Delete the AWS Lambda created Amazon CloudWatch Log Group

Follow **[this deep link](https://console.aws.amazon.com/cloudwatch/home?#logs:prefix=/aws/lambda/wild-rydes)** to list the **Amazon CloudWatch Log Groups** with the name `/aws/lambda/wild-rydes`, AWS Lambda created during this lab. Select the Amazon CloudWatch Log Group and choose **Delete log group** from the **Actions** menu.

