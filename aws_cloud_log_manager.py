import boto3

class AWSCloudLogManager:
  """
  A class for saving logs to AWS S3 with different filenames based on date.
  """
  def __init__(self, aws_access_key_id, aws_secret_access_key):
    """
    Initializes the AWSCloudLogManager with AWS credentials.

    Args:
      aws_access_key_id: Your AWS access key ID.
      aws_secret_access_key: Your AWS secret access key.
    """
    self.client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    self.bucket_name = "your-bucket-name"  # Replace with your bucket name

  def save_log(self, log_message):
    """
    Saves a log message to AWS S3 with a filename based on the current date.

    Args:
      log_message: The log message to be saved.
    """
    from datetime import datetime

    # Generate filename with current date (YYYY-MM-DD)
    now = datetime.utcnow().strftime("%Y-%m-%d")
    filename = f"logs/{now}.log"

    self.client.put_object(Body=log_message, Bucket=self.bucket_name, Key=filename)
