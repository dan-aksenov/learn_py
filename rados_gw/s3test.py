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
def s3connect( config_file ):
    "Connect to given s3 gateway using config file."
    try:
        with open( config_file ) as cfg_file:    
            conn_data = json.load(cfg_file)
    except:
        print "Error: Unable to read config file. "
        return 1

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
    buck = conn.create_bucket( buck_name )
    print 'Uploading %s to bucket %s' % \
    (file_name, buck)

    def percent_cb(complete, total):
        sys.stdout.write('.')
        sys.stdout.flush()

    k = Key(buck)
    k.key = file_name
    k.set_contents_from_filename(file_name,
        cb=percent_cb, num_cb=10)

# Got from http://docs.ceph.com/docs/master/radosgw/s3/python/
def buck_cont( buck_name ):
    "View bucket contents. Create bucket if not exists."
    # buck = conn.create_bucket( buck_name ) # not need to create one more time. thus commented out.
    for key in buck.list():
        print "{name}\t{size}\t{modified}".format(
            name = key.name,
            size = key.size,
            modified = key.last_modified,
        )

def buck_dump( buck_name, dump_path ):
    "Retreive bucket  contents and  store it as  files."
    for key in buck.list():
        bucket.get_key( 'key' )
        key.get_contents_to_filename( dump_path  + key)


# Access rights.
# Got from http://boto.cloudhackers.com/en/latest/s3_tut.html
'''
bucket = conn.get_bucket('my-new-container')
acl = bucket.get_acl()
acl
bucket.set_acl('public-read')
bucket.set	_acl('public-read','hello.txt')
'''