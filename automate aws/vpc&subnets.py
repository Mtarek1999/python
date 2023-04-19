import boto3

client = boto3.client('ec2')
resource = boto3.resource('ec2')

#creat vpc & subnets
new_vpc = resource.create_vpc(
    CiderBlock="10.0.0.0/16"
)
new_vpc.create_subnet(
     CiderBlock="10.0.1.0/24"   
)
new_vpc.create_subnet(
     CiderBlock="10.0.2.0/24"   
)

#list current vpcs
avaliable_vpcs = client.describe_vpcs()
print(avaliable_vpcs)

# Terraform is much better for this task 