import boto3
import json
client = boto3.client("ecs", region_name="us-east-1")
clusters = client.list_clusters()
cluster_name = clusters['clusterArns'][0]
paginator = client.get_paginator('list_services')
response_iterator = paginator.paginate(
    cluster=cluster_name,
    PaginationConfig={
        'PageSize':100
    }
)
for each_page in response_iterator:
    for each_arn in each_page['serviceArns']:
        response = client.describe_services(
            services=[
                each_arn
            ]
        )
        print(json.dumps(response, indent=4, default=str))
