+++
title = "Clean up"
weight = 56
pre = "7 "
+++

In this step, we will clean up all resources we created during the lab to prevent further cost.

#### 1. Delete the AWS SAM template

In your Cloud9 IDE, run the following command to delete the resources we created with our AWS SAM template:

{{< highlight bash >}}
cd ~/environment/wild-rydes-async-messaging/code/lab-4
sam delete --stack-name wild-rydes-async-msg-4
{{< /highlight >}}

Enter (Y)es for each confirmation of the resources that SAM will delete. This includes the resources created explicitly by the SAM template as well as the supporting resources that SAM uses, such as the resources S3 bucket.

#### 2. Delete the AWS Lambda created Amazon CloudWatch Log Group

Follow **[this deep link](https://console.aws.amazon.com/cloudwatch/home?#logs:prefix=/aws/lambda/wild-rydes)** to list the **Amazon CloudWatch Log Groups** with the name `/aws/lambda/wild-rydes`, AWS Lambda created during this lab. Select the Amazon CloudWatch Log Group and choose **Delete log group** from the **Actions** menu. Repeat for remaining Log Groups.

{{%expand "Detailed description" %}}
![Step 1](lab-4-step-1.png)

{{% /expand%}}
