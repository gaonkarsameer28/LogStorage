from azure.storage.blob import BlobServiceClient

class AzureCloudLogManager:
  """
  A class for saving logs to Azure Blob Storage with different filenames based on date.
  """
  def __init__(self, connection_string):
    """
    Initializes the AzureCloudLogManager with the connection string.

    Args:
      connection_string: A string containing the connection details for Azure Blob Storage.
    """
    self.client = BlobServiceClient.from_connection_string(connection_string)
    self.container_name = "applogs"  # Replace with your container name

  def save_log(self, log_message,filename):
    """
    Saves a log message to Azure Blob Storage with a filename based on the current date.

    Args:
      log_message: The log message to be saved.
    """
    from datetime import datetime

    # Generate filename with current date (YYYY-MM-DD)
    #now = datetime.utcnow().strftime("%Y-%m-%d")
    #filename = f"logs/{now}.log"

    container_client = self.client.get_container_client(self.container_name)
    blob_client = container_client.get_blob_client(filename)
    blob_client.upload_blob(log_message, overwrite=True)  # Overwrites existing file
