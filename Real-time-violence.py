import boto3
import time
from boto.s3.key import Key
import sys
import cv2

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
file_name1 = "violent-webcame2.jpeg"
#"violent-webcame2.jpeg"
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
        if label['Name'] == 'Violence' or label['Name']=='Weapon Violence' or label['Name']=='Physical Violence' or label['Name']=='Weapons' or label['ParentName']=='Violence':
            print('Violence detected with a confidence of' + ' : ' + str(label['Confidence'])+'\n')
            s3.Object(bucket2, file_name2).copy_from(CopySource=bucket + '/' + file_name1)
            s3.Object(bucket, file_name2).copy_from(CopySource=bucket + '/' + file_name1)
            break
    return len(response['ModerationLabels'])


def main():
    photo = file_name1
    #photo = 'gun-violent-2.jpeg'
    bucket = 'host-s3-static'
    label_count=moderate_image(photo, bucket)
    #print("Labels detected: " + str(label_count))


if __name__ == "__main__":
    while True:
        start = time.time()
        main()
        end = time.time()
        print('Took',end-start,'seconds to analyze image\n')

