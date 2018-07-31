#!/usr/bin/env python
import sys
import boto3

ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():
	print instance.id, instance.state

	print "Status Name : ", instance.state["Name"]; 
	print "Status Code : ", instance.state["Code"];
	instance_id = instance.id
	instance_ter = ec2.Instance(instance_id)
	
	#print instance_ter
		
	print 'Terminating Instance of ID ', instance_id
	response = instance_ter.terminate()
	print response


