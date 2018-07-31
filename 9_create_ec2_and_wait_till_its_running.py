#!/usr/bin/env python
import boto3
import time

ec2 = boto3.resource('ec2')

print "Creating EC2 instance"

response = ec2.create_instances(
	ImageId='ami-d783a9b8',
	InstanceType='t2.micro',
	MaxCount=1,
	MinCount=1
)

print response

instance_id = response[0].id

print "Get the state of EC2 instance"

instance = response[0]
notRunning=True
while (notRunning):
	if(instance.state["Name"] == 'running'):
		notRunning=False
	else:
		print "Instance not yet running"
	time.sleep(10)
	instance.update()

print "Instance is now running0"
