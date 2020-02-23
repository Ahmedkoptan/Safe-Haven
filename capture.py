import cv2
import boto
import boto.s3
import sys
from boto.s3.key import Key
from boto.s3.connection import S3Connection
import time
import datetime

AWS_ACCESS_KEY_ID = 'AKIA2GBIZGFHR4NG7Y6G'
AWS_SECRET_ACCESS_KEY = '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'

bucket_name = 'host-s3-static'

conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)

bucket = conn.get_bucket(bucket_name)

m,n = 390,280


def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()


cv2.namedWindow('detect-violence')
video_capture = cv2.VideoCapture(0)
file_name = "violent-webcame2.jpeg"

while True:
    dt = datetime.datetime.now()
    #file_name = dt.strftime("%d_%m_%Y__%H_%M_%S") + '.jpg'

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    frame = cv2.resize(frame,(m,n))
    cv2.imwrite(file_name,frame)

    k = Key(bucket)
    k.key = file_name
    k.set_contents_from_filename(file_name,
                                 cb=percent_cb, num_cb=10)

    time.sleep(0.5)

    cv2.imshow('detect-violence', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()