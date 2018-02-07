#Script to Stop EC2 Instances with tag-key AutoStartStop and tag-value TRUE
import boto3
from datetime import *
import boto3.session
import logging; logging.basicConfig(level=logging.INFO)

def lambda_handler(event, context):
	client = boto3.resource('ec2' , region_name='us-east-1')
	instances = client.instances.filter(Filters=[{'Name': 'tag-key', 'Values': ['AutoStartStop']}, {'Name': 'tag-value', 'Values': ['TRUE']}])
	for instance in instances:
		print instance
		if instance.state["Name"] == 'stopped':
			logging.info("Instance started")
			action = "Instance %s" % instance.id, "is stopped; starting it now"
			instance.start()
		else:
			logging.info("Instance stopped")
			action = "Instance %s" % instance.id, "is running; stopping it gracefully"
			instance.stop()
	return action

