import boto3
class s3bucket:
    pass

    def attack(self, bucket_name, key, secret):
        session = boto3.Session(
            aws_access_key_id=key,
            aws_secret_access_key=secret,
        )

        s3 = session.resource('s3')

        object = s3.Object(bucket_name, 'vuln_file_name.txt')

        txt_data = b'This is a test file to check for misconfiguration'

        try:
            result = object.put(Body=txt_data)
            res = result.get('ResponseMetadata')

            if res.get('HTTPStatusCode') == 200:
                print('File Uploaded Successfully')
            else:
                print('File Not Uploaded')
        except:
            print("Either the bucket does not exist or Access Denied")
