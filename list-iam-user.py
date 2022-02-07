import boto3
aws_mag_con_root=boto3.session.Session(profile_name='root')
#aws_mag_con_root=boto3.sesion.Session(profile_name='ec2_developer')

iam_con_re=aws_mag_con_root.resource(service_name='iam', region_name="us-west-2")
iam_con_cli=aws_mag_con_root.client(service_name='iam', region_name="us-west-2")

#listing iam user with resource object:

for each_user in iam_con_re.users.all():
    print(each_user.name)
    

