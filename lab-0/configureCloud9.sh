#!/bin/bash

sudo yum update -y

sudo pip uninstall aws-sam-cli -y
sudo pip uninstall awscli -y
sudo python -m pip uninstall pip -y

sudo alternatives --set python /usr/bin/python3.6

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python get-pip.py

sudo /usr/local/bin/pip install awscli
sudo /usr/local/bin/pip install aws-sam-cli
sudo /usr/local/bin/pip install cfn-lint
