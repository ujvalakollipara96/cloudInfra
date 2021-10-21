import boto3
import csv

s3 = boto3.resource('s3',aws_access_key_id='AKIATHB23F4LFAVWDAUI',aws_secret_access_key='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')
print("sent access key and id")

try:
    s3.create_bucket(Bucket='ujju2',CreateBucketConfiguration={'LocationConstraint':'us-east-2'})
except Exception as e:
    print('we entered the exception')
    print (e)

bucket = s3.Bucket("ujju2")
bucket.Acl().put(ACL='public-read')


body = open('/home/parallels/Downloads/exp1.csv', 'rb')
o = s3.Object('ujju2', 'exp1.csv').put(Body=body )
body = open('/home/parallels/Downloads/exp2.csv', 'rb')
o = s3.Object('ujju2', 'exp2.csv').put(Body=body )
body = open('/home/parallels/Downloads/exp3.csv', 'rb')
o = s3.Object('ujju2', 'exp3.csv').put(Body=body )
body = open('/home/parallels/Downloads/experiments.csv', 'rb')
o = s3.Object('ujju2', 'experiments.csv').put(Body=body )
s3.Object('ujju2', 'experiments.csv').Acl().put(ACL='public-read')
s3.Object('ujju2', 'exp1.csv').Acl().put(ACL='public-read')
s3.Object('ujju2', 'exp2.csv').Acl().put(ACL='public-read')
s3.Object('ujju2', 'exp3.csv').Acl().put(ACL='public-read')



dyndb = boto3.resource('dynamodb', region_name='us-east-2',aws_access_key_id='AKIATHB23F4LFAVWDAUI', aws_secret_access_key='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')
try:
    table = dyndb.create_table(
        TableName='DataTable',
        KeySchema=[
            {
                'AttributeName': 'PartitionKey',
                'KeyType': 'HASH'
            }, 
            {
                'AttributeName': 'RowKey',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'PartitionKey',
                'AttributeType': 'S'
            }, 
            {
                'AttributeName': 'RowKey',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
)
except Exception as e:
    print (e)
#if there is an exception, the table may already exist.
    table = dyndb.Table("DataTable")
table.meta.client.get_waiter('table_exists').wait(TableName='DataTable')
print(table.item_count)
import csv
with open('/home/parallels/Downloads/experiments.csv','rb') as csvfile:
    csvf = csv.reader(csvfile, delimiter=',', quotechar='|')
    for item in csvf:
        #print('this is the item')
        print item
        #print('item ends here')
        body = open('/home/parallels/Downloads/experiments.csv', 'rb')
        s3.Object('ujju2',item[3]).put(Body=body )
        md = s3.Object('ujju2', item[3]).Acl().put(ACL='public-read')
        url = "https://ujju2.s3.us-east-2.amazonaws.com/"+item[4]
        #print(url)
        metadata_item = {'PartitionKey':item[0],'RowKey':item[4],'Temp':item[1], 'Conductivity' : item[2], 'Concentration' : item[3], 'url':url}
        #print(metadata_item)
        try:
            table.put_item(Item=metadata_item)
        except:
            print "item may already be there or another failure"
        

response = table.get_item(
    Key={
        'PartitionKey': '3',
        'RowKey': 'exp3.csv'
    }
)
item=response['Item']
print(item)
