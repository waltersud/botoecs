import boto3
import json
client = boto3.client("ecs", region_name="us-east-1")
clusters = client.list_clusters()
cluster_name = clusters['clusterArns'][1]
print(cluster_name)
response = client.create_service(cluster=cluster_name, 
                serviceName="SimpleWebServer",
                taskDefinition='AWSSampleApp2',
                desiredCount=1,
                networkConfiguration={
                    'awsvpcConfiguration': {
                        'subnets': [
                            'subnet-3ae3685f',
                        ],
                        'assignPublicIp': 'ENABLED',
                        'securityGroups': ["sg-9be2d6e7"]
                    }
                },
                launchType='FARGATE',
            )
print(json.dumps(response, indent=4, default=str))
