#!/bin/python
import os
'''
Script to edit simlinks enmasse.
Originally made to relink postgresql tablespaces after restore.
'''

'''
Path to directory containing tablespace links.
Presumed to be like $PG_DATA/pg_tblspc/
Last slash "/" required!
'''
links_location = "/usr/local/pgsql/basebackup/db-09-22-2017_09/pg_tblspc/"

'''
Path part to be changed. IE if we are replacing 
/usr/local/pgsql/tablespace/fdc_ods_big_ind
with
/usr/local/pgsql/basebackup/tablespace/fdc_ods_big_ind
orig_part shold be like 
   /usr/local/pgsql/tablespace 
and
final_part like 
   /usr/local/pgsql/basebackup/tablespace
'''
orig_part = '/usr/local/pgsql/tablespace'
final_part = '/usr/local/pgsql/basebackup/tablespace'

# Get link names.
links = os.listdir( links_location )

# Rename links in a loop.
for link in links:
   # Create full path to link.
   link_path = links_location + link
      
   # Validation: if object is link can be added in future.
   #os.path.islink( link_path )
   #True

   # Get existing link destination, which needs to be renamed.   
   old_link_dest = os.path.realpath( link_path )	
   print old_link_dest
   
   # Set new link destination.
   new_link_dest = old_link_dest.replace( orig_part, final_part )
   print new_link_dest
   
   # Recreate link. Drop old fi exist.
   if os.path.lexists( link_path ):
      os.remove( link_path )
   os.symlink( new_link_dest, link_path )