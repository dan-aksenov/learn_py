# Simple python script to connect to radosgw(ceph in my setup). Create bucket and insert some dummy data to in.
import boto
import boto.s3
import sys
import boto.s3.connection
from boto.s3.key import Key

# Connect.
# Got from http://docs.ceph.com/docs/master/install/install-ceph-gateway
access_key = '434A2UHTCPKYJOTUFFOL'
secret_key = 'QZfwhMffQ7knQ7xwKUlvAx4b3wapKCZkgnHxpLpE'
conn = boto.connect_s3(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        host='rados-gw.my.ru', port=7480,
        is_secure=False, calling_format=boto.s3.connection.OrdinaryCallingFormat(),
       )

# Create bucket.
bucket = conn.create_bucket('my-new-bucket')
for bucket in conn.get_all_buckets():
    print "{name} {created}".format(
        name=bucket.name,
        created=bucket.creation_date,
    )

# Insert file to bucket.
# Got from https://stackoverflow.com/questions/15085864/how-to-upload-a-file-to-directory-in-s3-bucket-using-boto
testfile = "test.file"
print 'Uploading %s to bucket %s' % \
   (testfile, bucket)

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

k = Key(bucket)
k.key = 'my test file'
k.set_contents_from_filename(testfile,
    cb=percent_cb, num_cb=10)

# View bucket contents.	
# Got from http://docs.ceph.com/docs/master/radosgw/s3/python/
for key in bucket.list():
        print "{name}\t{size}\t{modified}".format(
                name = key.name,
                size = key.size,
                modified = key.last_modified,
                )