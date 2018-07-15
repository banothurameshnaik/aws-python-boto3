#!/usr/bin/python

import boto3

ec2 = boto3.resource('ec2')

print("Getting the instances")

instances = ec2.instances.all()

print("Completed the listing of EC2 instances with response of below")

for instance in instances:
	print("\t", instance.id, instance.state['Name'], instance.instance_type)

print("All Jobs Completed")