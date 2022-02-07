import boto3
'''
aws_mag_con=boto3.session.Session(profile_name='root')
iam_con=aws_mag_con.resource("iam")
'''
iam_con = boto3.resource(service_name="iam", region_name="us-west-2")

for each_user in iam_con.users.all():
    print(each_user.name)
