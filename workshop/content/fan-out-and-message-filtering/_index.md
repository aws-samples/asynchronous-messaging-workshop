+++
title = "Fan-Out & Message Filtering"
weight = 20
pre = "Lab-1: "
+++

{{% notice info %}}
Make sure you executed the **[Workshop Prerequisites](/prerequisites.html)** first, before you start with this lab!
{{% /notice %}}

As a registered customer, when you need a ride, you can use the Wild Rydes customer app to request a unicorn and manage everything around it.
As a registered unicorn, you can use the Wild Rydes unicorn app to manage everything around your business.  

In particular, unicorns are interested to use the app to submit a ride completion after they have successfully delivered a customer to their destination.
This is the use case we will now have a closer look at.  

At Wild Rydes, end-user clients typically communicate via REST APIs with the backend services. For our use case, the Wild Rydes unicorn app interacts with the API exposed by the unicorn management service. It uses the submit-ride-completion resource to send the relevant details of the ride to the backend. In response to that, the backend creates a new completed-ride resource and returns the respective status code, the location, and a representation of the new resource to the client.

It’s probably not a surprise that there are other services in the Wild Rydes microservices landscape, that are also interested in a new completed ride:  

+ **Customer notification service**: Customers should get a notification into their app about their latest completed ride.
+ **Customer accounting service**: After all, Wild Rydes is a business, so this service would be responsible to collect the fare from the customer.
+ **Extraordinary rides service**: This is special service that is interested in rides with fares or distances above certain thresholds - preparing the respective data for marketeers and success managers.

This use case obviously cries for making use of publish/subscribe messaging, which can comfortably done using Amazon SNS in a serverless and scalable manner. It decouples both sides as much as possible. Services on the right hand side can autonomously subscribe to the topic, transparent to the left hand side.

![Module 1](fan-out-and-message-filtering/module-1.png)

## Lab Objectives

In this lab, you will acquire the following skills:  

+ **How to create an Amazon SNS topic?**
+ **How to add an HTTP(S) subscription to an Amazon SNS topic?**
+ **How to define a subscription filter in an Amazon SNS subscriptions?**
+ **How to confirm an HTTP(S) subscription automatically in your application?**
+ **How to verify, the published message is really coming from Amazon SNS?**
+ **How to call Amazon SNS from AWS Lambda?**


{{% notice tip %}}
**Lab source code**  
If you are curious and would like to dive into the lab's source code, you are more than welcome to do so. You will find the source code of this lab in our Github repo **[here](https://github.com/aws-samples/asynchronous-messaging-workshop/tree/master/code/lab-1)**.
{{% /notice %}}
