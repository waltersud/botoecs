import boto3
import json
client = boto3.client("ecs", region_name="us-east-1")
response = client.create_cluster(clusterName="WebServices")
print(json.dumps(response, indent=4))
