import csv
import boto3


# read access credentials
with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

photo = 'detect-analyze-faces-rekognition-sample1.jpg'

# Create client
client = boto3.client('rekognition', aws_access_key_id = access_key_id, aws_secret_access_key = secret_access_key,  region_name="eu-north-1")

# Read image as bytes
with open(photo, 'rb') as source_image:
    source_bytes = source_image.read()

response = client.detect_labels(Image={'S3Object': {
            'Bucket': 'bt-bilder',
            'Name': 'detect-analyze-faces-rekognition-sample1.jpg'
        }}, MaxLabels=5, MinConfidence=95)

print(response)