#!/usr/bin/env python

import boto3
import sys
from botocore.exceptions import ClientError

instance_id = sys.argv[1]
monitor_state = sys.argv[2]

ec2 = boto3.client('ec2')

print "Operation : ", instance_id , " ", monitor_state

# START INSTANCE

if monitor_state == "ON":
	# Doing Try catch method
	try:
		response = ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
	except ClientError as e:
		#print e
		if 'DryRunOperation' not in str(e):
			print e
			raise
	
	# Dry run was successed
	
	try:
		response = ec2.start_instances(InstanceIds=[instance_id],DryRun=False)
		print response
	except ClientError as e:
		print e
		raise
else:
	# Doing try catch method by dry run
	try:
		response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
	except ClientError as e:
		#response = ec2.stop_instances(InstanceIds=[instance_id])
		#print e
		if 'DryRunOperation' not in str(e):
			print e
			raise	
	
	# Dry run successed 

	try:
		response = ec2.stop_instances(InstanceIds=[instance_id], DryRun = False)
		print response
	except ClientError as e:
		print e
		raise


print "All Jobs Completed"
