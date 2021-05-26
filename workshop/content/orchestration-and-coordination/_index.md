+++
title = "Orchestration and Coordination"
weight = 50
pre = "Lab-4: "
+++

{{% notice info %}}
Make sure you executed the **[Workshop Prerequisites](/prerequisites.html)** first, before you start with this lab!
{{% /notice %}}

AWS Step Functions is a fully managed Serverless workflow management service for managing long running processes and coordinating the components of distributed applications and microservices using visual workflows. But did you know it can also help you deal with the complexities of dealing with a long lived transaction across distributed components in your microservices architecture? In this Builder session, you will learn how AWS Step Function can help us implement the Saga design pattern.

## What problems are we trying to solve

When building cloud-based distributed architectures, one of the questions we need to ask ourselves is how do we maintain data consistency across microservices that have their own database / persistence mechanism? We do not have support for Distributed Transaction Coordinators (DTC) or two-phase commit protocols responsible for coordinating transactions across multiple cloud resources. We need a mechanism coordinate multiple local transactions.

## What is the Saga Pattern

A Saga is a design pattern for dealing with “long-lived transactions” (LLT), published by Garcia-Molina and Salem in 1987. Their original paper can be found here [https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf](https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf).

  > “LLT is a saga if it can be written as a sequence of transactions that can be interleaved with other transactions.” (Garcia-Molina, Salem 1987)

Fundamentally it is a failure management pattern, that provides us the means to establish semantic consistency in our distributed applications by providing compensating transactions for every transaction where you have more than one collaborating services or functions.

## Why AWS Step Functions

AWS Step Functions provide us with a mechanism for dealing with long-lived transactions, by providing us with the ability to build fully managed state machines that:

* coordinate the components of distributed applications and microservices
* allowing us to build our state machines using visual workflows
* provides us with a way to manage state and deal with failure

## Lab Objective

The core objective for this lab is to **build a state machine** that implements a Saga for the Wild Rydes Fare Collection process.

The process consists of three discrete transactions that need to be treated as a single, distributed transaction.

1. **Register Fare**: register the fare in a DynamoDB table.
1. **Payment Service**: calls a payment gateway for credit card pre-authorisation, and using the pre-authorisation code, completes the payment transaction
1. **Customer Accounting Service**: once the payment has been processed, update the Wild Rydes Customer accounting system with the transaction details.



Let's get started!


{{% notice tip %}}
**Lab source code**  
If you are curious and would like to dive into the lab's source code, you are more than welcome to do so. You will find the source code of this lab in our Github repo **[here](https://github.com/aws-samples/asynchronous-messaging-workshop/tree/master/code/lab-4)**.
{{% /notice %}}
