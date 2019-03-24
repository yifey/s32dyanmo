### This lambda function parses text data for each s3 put event
### and register these to assigned dynamo db.
### Runtime: python 3.6

import boto3
import json
import urllib.parse
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.client('dynamodb')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    #target dynamo table name
    dynamotable = 'YOUR_DYNAMO_TABLE_NAME'

    #get bucket name and file name by s3 put event
    bucket = event['Records'][0]['s3']['bucket']['name']
    filename = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    #get uploaded text file contents
    try:
        res = s3.get_object(Bucket=bucket, Key=filename)
    except Exception as e:
         return logger.error("Failed to get uploaded file: {}".format(e))

    # file type check
    if (res['ContentType'] == 'text/plain'):
        # get body
        body = res['Body'].read()
        bodystr = body.decode('UTF-8')
        lines = bodystr.split('\r\n') # for windows line endings

        #get items of each line
        for item in lines:
            data = item.split(' ')
            name = data[0]
            age = data[1]

            #register data to the dynamo db
            try:
                dynamodb.put_item(
                TableName = dynamotable,
                Item = {'name':{'S':name},'age':{'N':age}},
                Expected = {'name':{'Exists':False}}
                )
            except Exception as e:
                print(e)
    else:
        logger.error('Invalid File Type: ' + res['ContentType'])