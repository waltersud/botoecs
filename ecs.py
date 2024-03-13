import boto3

client = boto3.client('ecs',region_name='us-east-1')



response = client.list_task_definitions()

print(response)


