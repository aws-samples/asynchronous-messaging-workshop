+++
title = "Scatter-Gather"
weight = 40
pre = "Lab-3: "
+++

{{% notice info %}}
Make sure you executed the **[Workshop Prerequisites](/prerequisites.html)** first, before you start with this lab!
{{% /notice %}}

As Wild Rydes business has grown in its popularity,  it has opened its platform for various unicorn providers to partner with Wild Rydes. Customers of Wild Rydes app will be able to submit a request for a ride from their mobile app. Behind the scenes, Wild Rydes service will talk to multiple service providers who will submit quotes for the customer. The platform will receive all the responses and stage it in a database. The app will then periodically poll for the response quotes using a REST API and present them to the customer. The end user app will keep updating the dashboard of the quotes as new providers keep sending the response. In this architecture queues provide a loose coupling between the producer and consumer systems. In the absence of queues, the client systems would need to know the API endpoints for each of the server systems. It will need to be stored in a central database for any type of changes. It gets further complicated as additional instances are added or removed. In addition to it, client systems will need to implement failure and retry logic in their code. Queues help alleviate lot of such issues by decoupling the systems and providing a store and forward mechanism.
<br />

The service can be enhanced further to notify customers once all the service providers have responded or have exceeded the time for them to respond.

![Module 3](scatter-gather/module-3.png)

## Lab Objectives

In this lab, you will acquire the following skills:  

+ **How to implement a scatter pattern by sending messages through multiple channels?**
+ **How to implement a request response flow in asynchronous manner?**
+ **How to stage responses from multiple sources?**
+ **How to create a gather pattern by querying responses based on a request id?**


{{% notice tip %}}
**Lab source code**  
If you are curious and would like to dive into the lab's source code, you are more than welcome to do so. You will find the source code of this lab in our Github repo **[here](https://github.com/aws-samples/asynchronous-messaging-workshop/tree/master/code/lab-3)**.
{{% /notice %}}



