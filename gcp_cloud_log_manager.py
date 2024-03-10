from google.cloud import storage

class GCPCloudLogManager:
  """
  A class for saving logs to Google Cloud Storage with different filenames based on date.
  """
  def __init__(self, service_account_json):
    """
    Initializes the GCPCloudLogManager with a service account JSON file path.

    Args:
      service_account_json: Path to a JSON file containing your GCP service account credentials.
    """
    self.client = storage.Client.from_service_account_json(service_account_json)
    self.bucket_name = "your-bucket-name"  # Replace with your bucket name

  def save_log(self, log_message):
    """
    Saves a log message to Google Cloud Storage with a filename based on the current date.

    Args:
      log_message: The log message to be saved.
    """
    from datetime import datetime

    # Generate filename with current date (YYYY-MM-DD)
    now = datetime.utcnow().strftime("%Y-%m-%d")
    filename = f"logs/{now}.log"

    bucket = self.client.bucket(self.bucket_name)
    blob = bucket.blob(filename)
    blob.upload_from_string(log_message)
