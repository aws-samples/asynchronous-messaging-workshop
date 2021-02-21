+++
title = "Decoupled Microservices"
weight = 1
pre = "1. "
+++

![Intro](/images/wild-rydes.png)

# Welcome Builders!
 
Extend the existing and successful Wild Rydes service with asynchronous messaging for our microservices to allow us to scale reliable into new dimensions.

One of the implications of applying the microservices architectural style in Wild Rydes is that a lot of communication between components is done over the network. In order to be able to individually scale, operate, and evolve each service, this communication needs to happen in a loosely coupled manner. One option that our initial architect have in mind here is that all services expose an API following the REST architectural style.

Using REST APIs for communications between a set of systems can decouple them to a certain degree, but only if applied properly - which is often not the case. Additionally, REST APIs tend to be designed with synchronous communications, which limits the potential for decoupling when you think about request paths through a landscape of microservices. However, there is another option that provides even looser coupling: asynchronous messaging.

Asynchronous messaging is a fundamental approach for integrating independent systems, or building up a set of loosely coupled systems that can operate, scale, and evolve independently and flexibly. One could also quote our colleague Tim Bray on this:  

> **If your application is cloud-native, or large-scale, or distributed, and doesn’t include a messaging component, that’s probably a bug.**  

Within this workshop, we will introduce asynchronous messaging into Wild Rydes to support the ever growing demand of our business.

{{< youtube UJxog8pDydU >}}
