'''
S3 Testing module.
Simple python script to connect to radosgw(ceph in my setup). Create bucket and insert some dummy data to in.
'''
import boto
import boto.s3
import sys
import boto.s3.connection
import json
from boto.s3.key import Key

# Got from http://docs.ceph.com/docs/master/install/install-ceph-gateway
def s3connect():
   "Connect to given s3 gateway."
   # Read gateway name and access keys from json conf file. do this with try, except.
   with open('s3conf.json') as config_file:    
      conn_data = json.load(config_file)
   
   s3gw = conn_data['gateway']   
   access_key = conn_data['access_key']
   secret_key = conn_data['secret_key']
   global conn
   conn = boto.connect_s3(
      aws_access_key_id=access_key,
      aws_secret_access_key=secret_key,
      host=s3gw, port=7480,                                                      	
      is_secure=False, calling_format=boto.s3.connection.OrdinaryCallingFormat(),
      )
   return conn; 

def buck_list():
   "Get avaliable buckets."
   print "Available buckets are:"
   for bucket in conn.get_all_buckets():
       print "{name} {created}".format(
           name=bucket.name,
           created=bucket.creation_date,
       )

def buck_add( buck_name ):
    "Create bucket"
    buck = conn.create_bucket( buck_name )
    return buck;

# Got from https://stackoverflow.com/questions/15085864/how-to-upload-a-file-to-directory-in-s3-bucket-using-boto
def put_file( buck_name, file_name ):
   "Insert file to bucket. Create bucket if not exists."
   buck = buck = conn.create_bucket( buck_name )
   print 'Uploading %s to bucket %s' % \
   (file_name, buck)

   def percent_cb(complete, total):
      sys.stdout.write('.')
      sys.stdout.flush()

   k = Key(buck)
   k.key = 'my_test_file.txt'
   k.set_contents_from_filename(file_name,
      cb=percent_cb, num_cb=10)

# Got from http://docs.ceph.com/docs/master/radosgw/s3/python/
def buck_cont( buck_name ):
    "View bucket contents. Create bucket if not exists."
    buck = conn.create_bucket( buck_name )
    for key in buck.list():
        print "{name}\t{size}\t{modified}".format(
            name = key.name,
            size = key.size,
            modified = key.last_modified,
        )

# Access rights.
# Got from http://boto.cloudhackers.com/en/latest/s3_tut.html
'''
bucket = conn.get_bucket('my-new-container')
acl = bucket.get_acl()
acl
bucket.set_acl('public-read')
bucket.set	_acl('public-read','hello.txt')
'''