import boto3
import json

def get_ec2_products(instance_type, region='us-east-1'):
    client = boto3.client('pricing', region_name='us-east-1')
    filters = [
        {'Type':'TERM_MATCH','Field':'instanceType','Value':instance_type},
        {'Type':'TERM_MATCH','Field':'operatingSystem','Value':'Linux'},
    ]
    resp = client.get_products(ServiceCode='AmazonEC2', Filters=filters, MaxResults=100)
    return resp
