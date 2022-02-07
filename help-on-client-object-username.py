import boto3
aws_mag_con=boto3.session.Session(profile_name="root")
#iam,ec2 and s3
iam_con_cli=aws_mag_con.client(service_name="iam",region_name="us-west-2")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-west-2")
s3_con_cli=aws_mag_con.client(service_name="s3",region_name="us-west-2")
'''
#List all iam users using client object
response=iam_con_cli.list_users()
for each_item in response['Users']:
    print(each_item['UserName'])
    ''''
# list all ec2 instances
