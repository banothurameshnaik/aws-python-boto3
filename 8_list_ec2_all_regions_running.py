#!/usr/bin/env python
import boto3
import sys
import types

ec2 = boto3.client('ec2')

regions = ec2.describe_regions()

for region in regions["Regions"]:
	print "Running for region : ", region["RegionName"]
	ec2 = boto3.resource("ec2", region_name=region["RegionName"])
	instances = ec2.instances.filter(
		Filters=[
			{
				"Name":"instance-state-name",
				"Values": ["running", "stopped"]
			}
		])

	for instance in instances:
		print "\tInstance ID : ", instance.id
		print "\t\tState : " ,instance.state['Name']
		print "\t\tPublic IP : ", instance.public_ip_address
		print "\t\tPrivate IP : ", instance.private_ip_address
		nameFound = False
		if isinstance(instance.tags, types.ListType): 
			for tag in instance.tags:
				if "Name" in tag['Key']:
					print "\t\tName : ", tag['Value']
					nameFound=True
		if(nameFound is False):
			print "\t\tName : Not found" 
