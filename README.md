# README.md
## Objective
This script can register logs to the AWS Dynamo DB. Uploading event will be triggered by uploading log files to s3 bucket.


## Setup Steps
You need to perform following steps to run this script.

1. Create a s3 bucket.
2. Create an IAM role for a lambda function.
3. Create a DynamoDB table.
4. Create a lambda function.
5. Uploading a log file to the s3 bucket.

In this readme, we assume following name and age data, sample.txt, to register.

'''sample.txt
alice 20
bob 31
'''


## 1. Create a s3 bucket.
You need to create a s3 bucket, say my-log-bucket, that will store original log data.

## 2. Create an IAM role.
Prepare a new IAM role, say my-iam-role, with following policies.

- AmazonDynamoDBFullAccess
- AmazonS3ReadOnlyAccess
- CloudWatchLogsFullAccess

## 3. Create a DynamoDB table.
Next, you should create a DynamoDB table, say my-log-table, that will eventually store logs.

## 4. Create a lambda function
Then, you can create a lambda function with following options.

- Function Name: your-function-name
- Runtime: Python 3.6
- IAM Role: my-iam-role

This function will be triggered by uploading a log file to the s3 bucket, so you should choose the s3 for trigger event with following options.

 - Bucket Name: my-log-bucket
 - Trigger: PUT

For lambda function, you may can the s32dynamo.py in this repository. Please make sure to substitute the value of the variable "YOUR_DYNAMO_TABLE_NAME" to your table name.

Now we are ready, save this function.

## 5. Uploading a log file to the s3 bucket.
You can test the function by uploading the log file "sample.txt" in this repository to your s3 bucket.
If the function works correctly, the data will be added to your dynamo table.

