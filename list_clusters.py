import boto3
import json
client = boto3.client("ecs", region_name="us-east-1")
paginator = client.get_paginator('list_clusters')
response_iterator = paginator.paginate(
    PaginationConfig={
        'PageSize':100
})
for each_page in response_iterator:
    for each_arn in each_page['clusterArns']:
        print(each_arn)
