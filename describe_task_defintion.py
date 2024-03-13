import boto3
import json
client = boto3.client("ecs", region_name="us-east-1")
paginator = client.get_paginator('list_task_definitions')
response_iterator = paginator.paginate(
    PaginationConfig={
        'PageSize':100
    }
)
for each_page in response_iterator:
    for each_task_definition in each_page['taskDefinitionArns']:
        response = client.describe_task_definition(taskDefinition=each_task_definition)
        print(json.dumps(response, indent=4, default=str))
