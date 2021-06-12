#!/bin/bash
sudo yum update -y

# Install cf-lint
sudo pip install cfn-lint

#cleanup
rm -fr ~/environment/wild-rydes-async-messaging/workshop/
rm -fr ~/environment/wild-rydes-async-messaging/.git
mv ~/environment/wild-rydes-async-messaging/code/lab-* ~/environment/wild-rydes-async-messaging/
rm -fr ~/environment/wild-rydes-async-messaging/code/