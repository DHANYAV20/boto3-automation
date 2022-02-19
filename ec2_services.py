#https://boto3.amazonaws.com/v1/documentation/api/1.9.42/reference/services/ec2.html#client
import boto3
from pprint import pprint
aws_con = boto3.session.Session(profile_name= "root")
ec2_aws_cli=aws_con.client(service_name="ec2", region_name="us-west-2")

response = ec2_aws_cli.describe_instances()['Reservations']
for each_item in response:
    pprint(each_item['Instances'])