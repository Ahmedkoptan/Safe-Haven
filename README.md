# Safe-Haven
The aim of this project is to detect violence (whether with weapon or physical violence) in order to prevent as much as possible from tragic events in public places such as mass shootings and acts of hate by automatically notifying the authorities onceany aggression is detected. The project is implemented in Python and HTML, and AWS Rekognition API was used to recognize the violent content.
Run locally capture.py to capture live stream from web cam
Then run Real-time-violence.py locally to detect violence from stream. The lambda function is run automatically from AWS via upload trigger. The webapp Html script should be uploaded on the s3 bucket, where detected violent feed will be displayed on it.
