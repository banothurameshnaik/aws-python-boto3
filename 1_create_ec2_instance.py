#!/usr/bin/python

import boto3

#Creat ec2 resource object

ec2 = boto3.resource('ec2')

print("Creating EC2 Instance")

response = ec2.create_instances(
	ImageId='ami-d783a9b8',
	MinCount=1,
	MaxCount=1,
	InstanceType="t2.micro"
	)

print("Completed the EC2 instance creation")

print(response)

print("All Jobs Completed")