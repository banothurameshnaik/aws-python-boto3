#!/usr/bin/env python
import boto3
import sys

ec2 = boto3.client('ec2')

regions = ec2.describe_regions()

#print "Total regions found in AWS ". len(regions["Regions"])
for region in regions["Regions"]:
	#print region
	print "Running for region : ", region["RegionName"]
	ec2 = boto3.resource("ec2", region_name=region["RegionName"])
	instances = ec2.instances.all()
	#print "\t Total EC2 found in this region ", len(instances)
	for instance in instances:
		print "\tInstance ID : ", instance.id, "State : " ,instance.state['Name']

