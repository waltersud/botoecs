import boto3
import json
client = boto3.client("ecs", region_name="us-east-1")
clusters = client.list_clusters()
cluster_name = clusters['clusterArns'][0]
print(cluster_name)

paginator = client.get_paginator('list_tasks')
response_iterator = paginator.paginate(
    cluster=cluster_name,    
    PaginationConfig={
        'PageSize':100
    }
)
counter = 1
for each_page in response_iterator:
    for each_task in each_page['taskArns']:
        print(each_task)
