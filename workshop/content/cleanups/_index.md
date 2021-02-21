+++
title = "Clean up"
weight = 60
pre = ""
+++

{{% notice tip %}}
**Running the workshop at an AWS Event**  
If you are running this workshop at an AWS hosted event, such as re:Invent,
Loft, Immersion Day, or any other event hosted by an AWS employee, you skip this section, as we will clean up everything for you.  
{{% /notice %}}

In this step, we will clean up the AWS Cloud9 IDE we have created at the very beginning.

#### 1. Delete the AWS Cloud9 IDE

Follow **[this deep link](https://console.aws.amazon.com/cloudformation/home?#/stacks?filteringText=wild-rydes-async-msg-0)** to list the **AWS CloudFormation** stack with the name `wild-rydes-async-msg-0`. Select the stack and choose **Delete**.

{{%expand "Detailed description" %}}
![Step 1](cleanups/step-1.png)
{{% /expand%}}


1. Open the [AWS CloudFormation Console](https://console.aws.amazon.com/cloudformation/home)
2. Select `wild-rydes-lab-x` stack from the list of Stacks
3. Click the **Delete** button
4. On the confirmation modal screen that appears, click **Delete Stack** button

> Note: You will need to delete the S3 bucket you created for this lab manually.

That's it! All done.
