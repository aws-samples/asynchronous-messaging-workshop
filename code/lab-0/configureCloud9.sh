#!/bin/bash
sudo yum update -y

# Install cf-lint
pip install cfn-lint --use-feature=2020-resolver

#cleanup
rm -fr ~/environment/wild-rydes-async-messaging/workshop/
rm -fr ~/environment/wild-rydes-async-messaging/.git
mv ~/environment/wild-rydes-async-messaging/code/lab-* ~/environment/wild-rydes-async-messaging/
rm -fr ~/environment/wild-rydes-async-messaging/code/