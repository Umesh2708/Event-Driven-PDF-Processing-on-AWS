import boto3
import json
import datetime
import urllib.parse

# Initialize AWS clients
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

# DynamoDB table name
table = dynamodb.Table('PASTE-YOUR-DynamoDB-TABLE-NAME')

def lambda_handler(event, context):
    try:
        # Get source bucket name
        source_bucket = event['Records'][0]['s3']['bucket']['name']

        # Decode file key (fix NoSuchKey error)
        object_key = urllib.parse.unquote_plus(
            event['Records'][0]['s3']['object']['key']
        )

        # Destination bucket (CHECK NAME CAREFULLY)
        destination_bucket = "PASTE-DESTINATION-BUCKET-NAME"

        # Output file name
        processed_key = f"processed-{object_key}"

        # Get file from S3 (binary safe)
        response = s3.get_object(
            Bucket=source_bucket,
            Key=object_key
        )

        file_content = response['Body'].read()

        # Upload file to destination bucket (no decoding)
        s3.put_object(
            Bucket=destination_bucket,
            Key=processed_key,
            Body=file_content,
            ContentType='application/pdf'
        )

        # Store metadata in DynamoDB
        table.put_item(
            Item={
                'fileName': object_key,    #Add name of partition key name for enter at place of fileName
                'processedFileName': processed_key,
                'sourceBucket': source_bucket,
                'destinationBucket': destination_bucket,
                'uploadTime': str(datetime.datetime.utcnow()),
                'fileSize': response['ContentLength']
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps('File processed and metadata stored successfully.')
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
