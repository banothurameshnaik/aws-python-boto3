#!/usr/bin/env python

import boto3

import sys

print sys.argv

instance_id = sys.argv[1]
state = sys.argv[2].upper()

ec2 = boto3.client('ec2')


if sys.argv[2].upper() == "ON":
	response = ec2.monitor_instances(InstanceIds=[instance_id])
else:
	response = ec2.unmonitor_instances(InstaceIds=[instance_id])

