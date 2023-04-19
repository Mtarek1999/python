import boto3
import schedule

client = boto3.client('ec2')
resource = boto3.resource('ec2')

def check_instance_status():
    statuses = client.describe_instance_status(
        IncludeAllInstances=True
    )
    for status in statuses['InstanceStatuses']:
        ins_status = status['InstanceStatus']['Status']
        sys_status = status['SystemStatus']['Status']
        state = status['InstanceState']['Name']
        print(f"Instance {status['InstanceId']} is {state} with instance status {ins_status} and system status {sys_status}")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")


schedule.every(5).seconds.do(check_instance_status)

while True:
    schedule.run_pending()

