+++
title = "Topic-Queue Chaining & Load Balancing"
weight = 30
pre = "Lab-2: "
+++

{{% notice info %}}
Make sure you executed the **[Workshop Prerequisites](/prerequisites.html)** first, before you start with this lab!
{{% /notice %}}

Let’s look once more at the publish/subscribe channel between the unicorn management service and all 3 backend services on the right hand side that are interested in getting notified about ride completions.

One of these services could happen to be taken offline for maintenance. Or the code that processes messages coming in from the ride completion topic could run into an exception. These are two examples where a subscriber service could potentially miss topic messages. A good pattern to apply here is **topic-queue-chaining**. That means that you add a queue, in our case an Amazon SQS queue, between the ride completion Amazon SNS topic and each of the subscriber services.  
As messages are buffered in a persistent manner in an SQS queue, no message will get lost should a subscriber process run into problems for many hours or days, or has exceptions or crashes.

But there is even more to it. By having an Amazon SQS queue in front of each subscriber service, we can leverage the fact that a queue can act as a **buffering load-balancer**. Due to nature that every queue message is delivered to one of potentially many consumer processes, you can easily scale your subscriber services out & in and the message load will be distributed over the available consumer processes. Furthermore, since messages are buffered in the queue, also a scaling event, for instance when you need to wait until an additional consumer process becomes operational, will not make you lose messages.

In this lab, we will develop the architecture below:

![Module 2](topic-queue-chaining-and-load-balancer/module-2.png)

## Lab Objectives

In this lab, you will acquire the following skills:  

+ **How to create an Amazon SQS queue?**
+ **How to leverage Amazon SQS as event source for AWS Lambda?**
+ **How to add an Amazon SQS subscription to an Amazon SNS topic?**
+ **How to define a subscription filter in an Amazon SNS subscriptions?**
+ **How to call Amazon SNS from AWS Lambda?**


{{% notice tip %}}
**Lab source code**  
If you are curious and would like to dive into the lab's source code, you are more than welcome to do so. You will find the source code of this lab in our Github repo **[here](https://github.com/aws-samples/asynchronous-messaging-workshop/tree/master/code/lab-2)**.
{{% /notice %}}
