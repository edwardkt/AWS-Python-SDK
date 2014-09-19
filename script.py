#!/usr/bin/python

import boto.ec2

ec2 = boto.ec2.connect_to_region('us-west-2')
ec2.run_instances('ami-8799d9b7')

