#!/usr/bin/env python
import boto3
ec2 = boto3.resource('ec2')

# All instances
print "\nAll Instances and theris status"

for instance in ec2.instances.all():
	print "\t",instance.id, instance.state['Name'] , instance.state['Code']


# Get only running instances

print "\nGet only running instances"

for instance in ec2.instances.filter(
		Filters = [
			{
				'Name' : 'instance-state-name',
				'Values' : ['running']
			}
		]):
	print "\t" ,instance.id, instance.state['Name'], instance.instance_type

print "\nGet only stopped instances"

for instance in ec2.instances.filter(
                Filters = [{'Name' : 'instance-state-name', 'Values' : ['stopped']}]):
        print "\t", instance.id, instance.state['Name'], instance.instance_type


print "\nAll Jobs completed"
