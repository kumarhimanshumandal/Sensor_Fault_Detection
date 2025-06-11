# Here, we will keep all those constants>> we will create this as package.

import os # helps to interact with the operating system.

# These all are variables with random names.
AWS_S3_BUCKET_NAME = "wafer-fault"
MONGO_DATABASE_NAME = "pwskills"
MONGO_COLLECTION_NAME = "waferfault"


TARGET_COLUMN = "quality"
MONGO_DB_URL="mongodb+srv://imran:TdPLW9Ad0OzpSSD2@cluster0.fv0lm61.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder =  "artifacts" # iske andr it'll fetch the data from MongoDB and convert that into a csv file and ek feature file path banega and uske 
# andr we have all the csv file which has bwwn extracted from MongoDB >> This is DataIngestion Process.