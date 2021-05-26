+++
title = "Bootstrap AWS Cloud9"
weight = 11
pre = ""
hidden = false
+++


{{% notice warning %}}
**Running the workshop at an AWS Event**  
If you are running this workshop at an AWS hosted event, such as re:Invent,
Loft, Immersion Day, or any other event hosted by an AWS employee, you skip this section, as the AWS Cloud9 IDE is already created for you. You can go straight to the next step and configure AWS Cloud9 by clicking the **orange arrowheads** on the right!
{{% /notice %}}

We will leverage **[AWS CloudFormation](https://aws.amazon.com/cloudformation/)** which allows us to codify our infrastructure. In addition, we use **[AWS SAM](https://aws.amazon.com/serverless/sam/)** to build serverless applications in simple and clean syntax.  

### 1. Create the AWS CloudFormation stack in your closest region

{{% notice note %}}
The Cloud9 workspace should be built by an IAM user with Administrator privileges,
not the root account user. Please ensure you are logged in as an IAM user, not the root
account user.
{{% /notice %}}

{{< tabs name="Region" >}}
{{< tab name="Frankfurt" include="eu-central-1" />}}
{{< tab name="Ireland" include="eu-west-1" />}}
{{< tab name="Oregon" include="us-west-2" />}}
{{< tab name="Ohio" include="us-east-2" />}}
{{< tab name="Singapore" include="ap-southeast-1" />}}
{{< tab name="Sydney" include="ap-southeast-2" />}}
{{< /tabs >}}


### 2. Launch the AWS CloudFormation stack

Just click the **Create Stack** button to launch the template.

{{%expand "Detailed description" %}}
![Step 1](prerequisites-1/step-1.png)
{{% /expand%}}


### 3. Wait until the AWS CloudFormation stack launched

It takes usually less than 2 minutes until the stack launched. When the stack is launched, the status will change from **CREATE_IN_PROGRESS** to **CREATE_COMPLETE**.

{{%expand "Detailed description" %}}
![Step 2](prerequisites-1/step-2.png)
{{% /expand%}}
