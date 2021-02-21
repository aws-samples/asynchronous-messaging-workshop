+++
title = "SAM"

disableToc = true
hidden = true
+++


#### 3. Delete the Amazon S3 bucket

In your Cloud9 IDE, run the following command to delete the Amazon S3 bucket we created earlier:

{{< highlight bash >}}
aws s3 rb s3://${BUCKET_NAME} —-force
{{< /highlight >}}

You are done!
