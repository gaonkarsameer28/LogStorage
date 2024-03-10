from azure_cloud_log_manager import AzureCloudLogManager
from aws_cloud_log_manager import AWSCloudLogManager
from gcp_cloud_log_manager import GCPCloudLogManager

class CloudStorageManager:
  """
  A wrapper class for interacting with different cloud storage providers for log saving.
  """
  def __init__(self, provider, connection_string):
    """
    Initializes the CloudStorageManager with the specified provider and connection string.

    Args:
      provider: The cloud provider (e.g., "azure", "aws", "gcp").
      connection_string: A string containing connection details specific to the provider.
    """
    if provider == "azure":
      self.manager = AzureCloudLogManager(connection_string)
    elif provider == "aws":
      self.manager = AWSCloudLogManager(connection_string)  # Replace with actual connection string for AWS
    elif provider == "gcp":
      self.manager = GCPCloudLogManager(connection_string)  # Replace with actual connection string for GCP
    else:
      raise ValueError("Unsupported cloud provider:", provider)

  def save_log(self, log_message, filename):
    """
    Saves a log message to the chosen cloud storage with the specified filename.

    Args:
      log_message: The log message to be saved.
      filename: The filename for the log file in cloud storage.
    """
    self.manager.save_log(log_message, filename)
