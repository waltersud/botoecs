import boto3
import json
client = boto3.client("ecs", region_name="us-east-1")
response = client.register_task_definition(
        containerDefinitions=[
            {
                "name": "pre-paideia-cursos",
                "image": "484256395366.dkr.ecr.us-east-1.amazonaws.com/pre_paideia_cursos:v24",
                "cpu": 0,
                "portMappings": [
                     {
                        "containerPort": 80,
                        "hostPort": 80,
                        "protocol": "tcp"
                     },
                     {
                        "containerPort": 443,
                        "hostPort": 443,
                        "protocol": "tcp"
                     }
                    ],
                "essential": True,
                "environment": [],
                "mountPoints": [
                     {
                        "sourceVolume": "PRE-PAIDEIA-CURSOS",
                        "containerPath": "/var/moodledata/cursos/",
                        "readOnly": False
                     }
                    ],
                "volumesFrom":[],
                "readonlyRootFilesystem": False,
                "ulimits": [],
                "logConfiguration": {
                    "logDriver": "awslogs",
                    "options": {
                         "awslogs-create-group": "true",
                         "awslogs-group": "/ecs/PRE-PAIDEIA-CURSOS",
                         "awslogs-region": "us-east-1",
                         "awslogs-stream-prefix": "ecs"
                    }
                }
            }
        ],
        executionRoleArn="arn:aws:iam::484256395366:role/ecsTaskExecutionRole",
        family= "AWSSampleApp2",
        networkMode="awsvpc",

        requiresCompatibilities= [
            "FARGATE"
        ],
        cpu= "256",
        memory= "512")
print(json.dumps(response, indent=4, default=str))
