#!/usr/bin/python

import boto.ec2

# Creating Connection to Service
conn = boto.ec2.connect_to_region("us-west-2")
print conn

# Launch AWS EC2 instance 
conn.run_instances('ami-id')

# Command to start instances
reservations = conn.get_all_reservations()
print reservations

# See which instances are associated with reservation
instances = reservations[0].instances
print instances
