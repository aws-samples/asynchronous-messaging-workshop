+++
title = "Build Guide"
weight = 51
pre = "2 "
+++

The bootstrap script provisions the AWS resources required for the workflow, including the Lambda functions to execute transactions, Amazon DynamoDB table to store Fare items, and an Amazon SNS topic for notifications with Amazon SQS subscriptions for success and failures.

The bootstrapping process also provisions two Step Functions State Machines:

* `wild-rydes-async-msg-4-start-here` - A starting point for your state machine.

* `wild-rydes-async-msg-4-completed` - A completed state machine to use as a reference if you get stuck.

{{% notice tip %}}
See the Output for the CloudFormation stack for ARN for the bootstrapped AWS resources. Alternatively, you can run the CloudFormation command below.
{{% /notice %}}

{{< highlight bash >}}
aws cloudformation describe-stacks \
    --stack-name wild-rydes-async-msg-4 \
    --query 'Stacks[].Outputs'
{{< /highlight >}}

The primary task in this lab is to use **`wild-rydes-async-msg-4-start-here`** as the starting point to create a Saga workflow using **Step Functions Workflow Studio**.

{{%expand "Completed State Machine Diagram" %}}
The completed state machine should look like the following:
![State Machine](lab-4-statemachine.png)
{{% /expand%}}

{{% notice note %}}
Your task is to create a state machine that integrates these services and deals with any failures by providing compensating transactions that leave the system, and the simulated customer's bank account, in a semantically consistent state.
{{% /notice %}}

## AWS Step Functions Workflow Studio

Workflow Studio for AWS Step Functions is a low-code visual workflow designer that enables you to create serverless workflows by orchestrating AWS services. You can use a drag and drop interface to create and edit workflows, control how input and output is filtered or transformed for each state, and configure error handling. As you create a workflow, Workflow Studio validates your work and auto-generates code. When you are finished, you can save your workflow, run it, then examine the results in the Step Functions console.

Step Functions has optimized integrations with a number of AWS services and can also directly integrate with the AWS SDK. In addition to service integrations which form the basis for **Action** states, Step Functions supports **Flow** states that enable error handling, conditional branching and parallel operations.

Here are some of the available flow states:

* Choice: Adds if-then-else logic.
* Parallel: Adds parallel branches.
* Map: Adds a for-each loop.
* Wait: Delays for a specific time.

 Consult the [Worflow Studio Documentation](https://docs.aws.amazon.com/step-functions/latest/dg/workflow-studio-components.html) for further information and the video below provides a short, high-level overview of the main visual components of Workflow Studio.
 
{{< youtube HfTucfkIwhs >}}

The following sections in this lab provides a step-by-step guide to implementing a complete state machine using Workflow Studio for AWS Step Functions. You can choose to build the Saga state machine using the step-by-step guide or build the state machine yourself and use the guides in this lab to help align your state machine to the completed example.

{{% notice note %}}
Step Functions supports calling the AWS SDK directly which enables integration in a State Machine to over 200 AWS services. However for the purpose of this lab, we will only use the **optimized** action types.
{{% /notice %}}
