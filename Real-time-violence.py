import boto3
import time
from boto.s3.key import Key
import sys
import cv2

AWS_ACCESS_KEY_ID = 'AKIA2GBIZGFHR4NG7Y6G'
AWS_SECRET_ACCESS_KEY = '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'
file_name1 = "violent-webcame2.jpeg"
file_name2 = "detected-violence.jpeg"
bucket = 'host-s3-static'
bucket2 = 'violence-bucket'

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

def moderate_image(photo, bucket):
    s3 = boto3.resource('s3')

    client=boto3.client('rekognition')

    response = client.detect_moderation_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}}, MinConfidence = 18.9)

    print('Detected labels for ' + photo)
    for label in response['ModerationLabels']:
        if label['Name'] == 'Violence' or label['Name']=='Weapon Violence':
            print(label['Name'] + ' : ' + str(label['Confidence']))
            print(label['ParentName'])
            s3.Object(bucket2, file_name2).copy_from(CopySource=bucket + '/' + file_name1)
            s3.Object(bucket, file_name2).copy_from(CopySource=bucket + '/' + file_name1)
    return len(response['ModerationLabels'])


def main():
    photo='violent-webcame2.jpeg'
    bucket = 'host-s3-static'
    label_count=moderate_image(photo, bucket)
    #print("Labels detected: " + str(label_count))


if __name__ == "__main__":
    while True:
        start = time.time()
        main()
        end = time.time()
        print('Took',end-start,'seconds to analyze image\n')
