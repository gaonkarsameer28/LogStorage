import datetime
from cloud_storage_manager import CloudStorageManager

# Choose the cloud provider
cloud_provider = "azure"  # Options: "azure", "aws", "gcp"

# Replace with your credentials for the chosen provider
if cloud_provider == "azure":
  connection_string = "your connection string"
elif cloud_provider == "aws":
  aws_access_key_id = "your_key_id"
  aws_secret_access_key = "your_access_key"
elif cloud_provider == "gcp":
  service_account_json = "path/to/your/service_account.json"

# Create an instance of CloudStorageManager and call its save_log method
cloud_storage_manager = CloudStorageManager(cloud_provider, connection_string)
log_message = "This is a sample log message."
# Generate filename with current date (YYYY-MM-DD)
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
filename = f"logs/{now}.log"

cloud_storage_manager.save_log(log_message, filename)

print("Log message saved to cloud storage.")
