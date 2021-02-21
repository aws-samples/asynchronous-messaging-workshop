+++
title = "Cleanup"
weight = 43
pre = "3 "
+++


In this step, we will clean up all resources, we created during this lab, so that no further cost will occur.

#### 1. Delete the AWS SAM template

In your Cloud9 IDE, run the following command to delete the resources we created with our AWS SAM template:

{{< highlight bash >}}
cd ~/environment/wild-rydes-async-messaging/code/lab-3
aws cloudformation delete-stack \
    --stack-name wild-rydes-async-msg-3

{{< /highlight >}}


#### 2. Delete the AWS Lambda created Amazon CloudWatch Log Group

Run the following command to delete all the log groups associated with the labs.

```
aws logs describe-log-groups --query 'logGroups[*].logGroupName' --output table | awk '{print $2}' | \
    grep ^/aws/lambda/wild-ryde | while read x; \
    do  echo "deleting $x" ; aws logs delete-log-group --log-group-name $x; \
done 
```

#### 3. Delete S3 bucket used to upload code package
You can delete the S3 bucket by going to the console or using the CLI. Please follow one of the options below to delete the bucket.

{{< tabs name="Style" >}}
{{< tab name="Console" include="clean-up-console" />}}
{{< tab name="SAM" include="clean-up-sam" />}}
{{< /tabs >}}


