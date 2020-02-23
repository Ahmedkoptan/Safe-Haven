import boto3
import json


def lambda_handler(event, context):
    # dt = event['Records'][0]['s3']['object']['key']
    # for i in event['Records']:
    #     action = i['eventname']
    #     ip = i['requestParameters']['sourceIPAddress']
    #     bucketname = i['s3']['bucket']['name']

    client = boto3.client('ses')

    subject = "Violence detected"
    # str(action) + 'Event from '+ bucketname
    body = "https://host-s3-static.s3-us-west-2.amazonaws.com/webapp.html"
    # """
    #     <br>
    #     This email is to notify you regarding {} event.
    #     Source IP: {}
    #     """.format(action,ip)

    message = {'Subject': {"Data": subject}, "Body": {"Html": {"Data": body}}}

    response = client.send_email(Source='egundabo@asu.edu', Destination={"ToAddresses": ["akdeyes@asu.edu"]},
                                 Message=message)
    """
    s3 = boto3.resource('s3')
    test_img = "detected-violence.jpeg"    

    tosend='https://host-s3-static.s3-us-west-2.amazonaws.com/webapp.html'
    message=client.publish(TargetArn='arn:aws:sns:us-west-2:700165206351:violent',Message=tosend,Subject="Uploaded Violent Image Label")
    #file_name = "violence.jpg"
    #s3.Object('violence-bucket',file_name).copy_from(CopySource='host-s3-static/'+test_img)
    """

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }