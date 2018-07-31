#!/usr/bin/env python

import boto3
import json

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

print response

#res = json.dumps(response, sort_keys=True, indent=4)

#print res

