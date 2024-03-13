import boto3
import json
client = boto3.client("ecs", region_name="us-east-1")
response = client.delete_cluster(cluster="WebServices")
print(json.dumps(response, indent=4))

