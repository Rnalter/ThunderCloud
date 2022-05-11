# ThunderCloud
Cloud Exploit Framework

## Usage
```
python3 tc.py -h

          _______ _                     _            _____ _                 _
         |__   __| |                   | |          / ____| |               | |
            | |  | |__  _   _ _ __   __| | ___ _ __| |    | | ___  _   _  __| |
            | |  | '_ \| | | | '_ \ / _` |/ _ \ '__| |    | |/ _ \| | | |/ _` |
            | |  | | | | |_| | | | | (_| |  __/ |  | |____| | (_) | |_| | (_| |
            \_/  |_| |_|\__,_|_| |_|\__,_|\___|_|   \_____|_|\___/ \__,_|\__,_|


usage: tc.py [-h] [-ce COGNITO_ENDPOINT] [-reg REGION] [-accid AWS_ACCOUNT_ID] [-aws_key AWS_ACCESS_KEY] [-aws_secret AWS_SECRET_KEY] [-bdrole BACKDOOR_ROLE] [-sso SSO_URL] [-enum_roles ENUMERATE_ROLES] [-s3 S3_BUCKET_NAME]
             [-conn_string CONNECTION_STRING] [-blob BLOB] [-shared_access_key SHARED_ACCESS_KEY]

Attack modules of cloud AWS

optional arguments:
  -h, --help            show this help message and exit
  -ce COGNITO_ENDPOINT, --cognito_endpoint COGNITO_ENDPOINT
                        to verify if cognito endpoint is vulnerable and to extract credentials
  -reg REGION, --region REGION
                        AWS region of the resource
  -accid AWS_ACCOUNT_ID, --aws_account_id AWS_ACCOUNT_ID
                        AWS account of the victim
  -aws_key AWS_ACCESS_KEY, --aws_access_key AWS_ACCESS_KEY
                        AWS access keys of the victim account
  -aws_secret AWS_SECRET_KEY, --aws_secret_key AWS_SECRET_KEY
                        AWS secret key of the victim account
  -bdrole BACKDOOR_ROLE, --backdoor_role BACKDOOR_ROLE
                        Name of the backdoor role in victim role
  -sso SSO_URL, --sso_url SSO_URL
                        AWS SSO URL to phish for AWS credentials
  -enum_roles ENUMERATE_ROLES, --enumerate_roles ENUMERATE_ROLES
                        To enumerate and assume account roles in victim AWS roles
  -s3 S3_BUCKET_NAME, --s3_bucket_name S3_BUCKET_NAME
                        Execute upload attack on S3 bucket
  -conn_string CONNECTION_STRING, --connection_string CONNECTION_STRING
                        Azure Shared Access key for readingservicebus/queues/blobs etc
  -blob BLOB, --blob BLOB
                        Azure blob enumeration
  -shared_access_key SHARED_ACCESS_KEY, --shared_access_key SHARED_ACCESS_KEY
                        Azure shared key
```

## Requirements
```
* python 3
* pip
* git
```

## Installation
```
 - get project `git clone https://github.com/Rnalter/ThunderCloud.git && cd ThunderCloud/`   
 - install [virtualenv](https://virtualenv.pypa.io/en/latest/) `pip install virtualenv`
 - create a python 3.6 local enviroment `virtualenv -p python3.6 venv`  
 - activate the virtual enviroment `source venv/bin/activate` 
 - install project dependencies `pip install -r requirements.txt`
 - run the tool via `python tc.py --help`
```

## Running ThunderCloud

Examples
```
python3 tc.py -sso <sso_url> --region <region>
python3 tc.py -ce <cognito_endpoint> --region <region>
```

