import argparse

def main():
    """Main function"""
    print('''
          _______ _                     _            _____ _                 _ 
         |__   __| |                   | |          / ____| |               | |
            | |  | |__  _   _ _ __   __| | ___ _ __| |    | | ___  _   _  __| |
            | |  | '_ \| | | | '_ \ / _` |/ _ \ '__| |    | |/ _ \| | | |/ _` |
            | |  | | | | |_| | | | | (_| |  __/ |  | |____| | (_) | |_| | (_| |
            \_/  |_| |_|\__,_|_| |_|\__,_|\___|_|   \_____|_|\___/ \__,_|\__,_|

    ''')
    parser = argparse.ArgumentParser(description='Attack modules of cloud AWS')
    parser.add_argument('-ce', '--cognito_endpoint', help='to verify if cognito endpoint is vulnerable '
                                                          'and to extract credentials')
    parser.add_argument('-reg', '--region',help='AWS region of the resource')
    parser.add_argument('-accid', '--aws_account_id', help='AWS account of the victim')
    parser.add_argument('-aws_key', '--aws_access_key', help= 'AWS access keys of the victim account')
    parser.add_argument('-aws_secret', '--aws_secret_key', help='AWS secret key of the victim account')
    parser.add_argument('-bdrole', '--backdoor_role', help='Name of the backdoor role in victim role')
    parser.add_argument('-sso', '--sso_url', help='AWS SSO URL to phish for AWS credentials')
    parser.add_argument('-enum_roles', '--enumerate_roles', help='To enumerate and assume account roles in victim AWS roles')
    parser.add_argument('-s3', '--s3_bucket_name', help='Execute upload attack on S3 bucket')
    parser.add_argument('-conn_string', '--connection_string', help='Azure Shared Access key for reading'
                                                                  'servicebus/queues/blobs etc')
    parser.add_argument('-blob', '--blob', help='Azure blob enumeration')
    parser.add_argument('-shared_access_key', '--shared_access_key', help='Azure shared key')
    args = parser.parse_args()
    if args.cognito_endpoint:
        from clouds.aws.cognito import Cognito
        attack_cognito = Cognito()
        attack_cognito.attack(args.cognito_endpoint, args.region)
    elif args.sso_url:
        from clouds.aws.sso import AWSSSO
        attack_sso = AWSSSO()
        attack_sso.attack(args.sso_url, args.region)
    elif args.enumerate_roles:
        from clouds.aws.enum import EnumRoles
        attack_roles = EnumRoles()
        attack_roles.attack(args.enumerate_roles, args.aws_access_key, args.aws_secret_key)
    elif args.s3_bucket_name:
        from clouds.aws.s3 import s3bucket
        attack_s3 = s3bucket()
        attack_s3.attack(args.s3_bucket_name, args.aws_access_key, args.aws_secret_key)
    elif args.backdoor_role:
        from clouds.aws.iambackdoor import backdoor
        attack_role = backdoor()
        attack_role.attack(args.backdoor_role, args.aws_access_key, args.aws_secret_key, args.aws_account_id)
    elif args.blob:
        from clouds.azure.blob import Blob
        attack_blob = Blob()
        attack_blob.attack()



if __name__ == '__main__':
    main()
