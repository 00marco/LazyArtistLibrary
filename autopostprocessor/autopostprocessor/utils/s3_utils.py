import boto3
import logging
logging.basicConfig(format="{levelname: <8}:{asctime}:{name: <30}:{lineno: <4}:{message}", level=logging.DEBUG, style="{")
logger = logging.getLogger(__name__)
import os


class S3Utils:
    def __init__(self, access_key, secret_access_key, bucket_name):
        self.access_key = access_key
        self.secret_access_key = secret_access_key
        self.client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key)
        self.bucket_name = bucket_name
        return
    
    def list_objects(self):
        response = self.client.list_objects(Bucket=self.bucket_name)
        # return [x for x in response.get('Contents', []) if not x.endswith("/")]
        return response.get("Contents", [])

    def download_object(self, remote_filename, local_filename):
        try:
            if os.path.exists(local_filename):
                logging.debug("file already exists, skipping download", local_filename)
                return 
            
            self.client.download_file(self.bucket_name, remote_filename, local_filename)
            logging.debug(f'Downloaded {remote_filename} to {local_filename}')
        except Exception as e:
            import traceback
            logging.error(f"error downloading file -- skipping; {e}")