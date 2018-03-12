import boto3

iam = boto3.client('iam')

#creating a service linked role
#aws iam create-service-linked-role --aws-service-name lex.amazonaws.com
try:
	role =  iam.create_service_linked_role(AWSServiceName='lex.amazonaws.com')
	print('Role created.')
except:
	print('Role is already created.')
finally:
	print('Below are the details: \n')
	print(iam.get_role(RoleName='AWSServiceRoleForLexBots'))
