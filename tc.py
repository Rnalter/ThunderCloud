import argparse

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Attack modules of cloud AWS')
    parser.add_argument('-ce', '--cognito_endpoint', help='to verify if cognito endpoint is vulnerable '
                                                          'and to extract credentials')
    parser.add_argument('-sso', '--sso_url', help='AWS SSO URL to phish for AWS credentials')
    parser.add_argument('-enum-roles', '--enumerate_roles', help='To enumerate account roles in victim AWS roles')
    parser.add_argument('-s3', '--s3_bucket_name', help='Execute 7 attacks on S3 bucket')
    parser.add_argument('-asum_role', '--assume_role', help='Privilege escalation for assuming roles')
    parser.add_argument('-conn_string', '--connection_string', help='Azure Shared Access key for reading'
                                                                  'servicebus/queues/blobs etc')
    parser.add_argument('-blob', '--blob', help='Azure blob enumeration')
    parser.add_argument()
    args = parser.parse_args()
    if args.cognito_endpoint:
        from clouds.aws.cognito import Cognito
        attack_cognito = Cognito()
        attack_cognito.attack()
    elif args.sso_url:
        from clouds.aws.sso import AWSSSO
        attack_sso = AWSSSO()
        attack_sso.attack()
    elif args.enumerate_roles:
        from clouds.aws.enum import EnumRoles
        attack_roles = EnumRoles()
        attack_roles.attack()
    elif args.s3_bucket_name:
        from clouds.aws.s3 import S3
        attack_s3 = S3()
        attack_s3.attack()
    elif args.assume_role:
        from clouds.aws.assume import AsumRole
        attack_roles = AsumRole()
        attack_roles.attack()
    elif args.shared_access_key:
        from clouds.azure.keys import ConnectionString
        attack_keys = ConnectionString()
        attack_keys.attack()
    elif args.blob:
        from clouds.azure.blob import Blob
        attack_blob = Blob()
        attack_blob.attack()



if __name__ == '__main__':
    main()
