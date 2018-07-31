#!/usr/bin/env python
import boto3
ec2 = boto3.resource('ec2')

# Creating instance
instance = ec2.create_instances(
	ImageId='ami-d783a9b8',
	MinCount=1,
	MaxCount=1,
	InstanceType='t2.micro',
	TagSpecifications=[
		{
			'ResourceType' : 'instance',
			'Tags' : [
				{
					'Key' : 'Name',
					'Value' : 'Prodcution EC2'
				}
			]
		}
	]
)
# Printing results
print instance[0].id
