+++
title = "Update Unicorn Management Service"

weight = 26
pre = "6 "
+++

After creating the Amazon SNS topic and all the subscriptions, the current architecture looks like the following on:  

![Step 1](step-1.png)

The last missing part to complete the architecture is calling our **Amazon SNS topic** from our **Unicorn Management Service**.

{{< tabs name="Style" >}}
{{< tab name="Console" include="update-unicorn-management-service-console" />}}
{{< tab name="SAM" include="update-unicorn-management-service-sam" />}}
{{< /tabs >}}
