import csv
import boto3


# read access credentials
with open('/Users/herman/Documents/UIB/6. semester/Git/MIX250/Facial_recognition_test_1.0/credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]


#photo = 'detect-analyze-faces-rekognition-sample1.jpg'
photo = 'bt3.jpeg'

# Read image as bytes
#with open(photo, 'rb') as source_image:
#   source_bytes = source_image.read()


# Create client
client = boto3.client('rekognition', aws_access_key_id = access_key_id, aws_secret_access_key = secret_access_key, region_name="eu-west-1")

# run rekogniton on image in S3 bucket
## recognize labels
response_labels = client.detect_labels(Image={'S3Object': {
            'Bucket': 'mix250-bt',
            'Name': photo
        }}, MaxLabels=10, MinConfidence=90)

## recognize faces
response_faces = client.detect_faces(
    Image={
        'S3Object': {
            'Bucket': 'mix250-bt',
            'Name': photo
            }
    },
    Attributes=[
        'ALL',
    ]
    )


#print response for labels
for key, value in response_labels.items():
    if key == 'Labels':
        for label__att in value:
            if label__att["Name"] == 'Human':
                print("-   -   -")
                print('Person DETECTED')
                print("-   -   -")


#print response for each face, seperated by "- - -"
for key, value in response_faces.items():
    if key == 'FaceDetails':
        for people__att in value:
            counter = 1
            print(people__att['Gender'])
            print(people__att['AgeRange'])
            print('-')
