#!/bin/python
import os
# Originally made to relink postgresql tablespaces after restore.
# Path to restored tablespace folder.
path = "/usr/local/pgsql/basebackup/db-09-22-2017_09/pg_tblspc/"
print path
input("Press Enter to continue...")
# Get link names
links = os.listdir( path )
print links
input("Press Enter to continue...")
#['181171', '129717', '129725', '129718', '129719', '181170', '129723', '129720', '129722', '181172', '129724', '181169', '129721']

# Rename every link in loop.
for link in links:
   #link = '129723'
   # Create full path to link.
   #fullpath = os.path.abspath(link)
   fullpath = path + link
   print fullpath
   input("Press Enter to continue...")
   # Validation if object is link can be added in future.
   #os.path.islink( fullpath )
   #True

   # Get existing link destination, which needs to be ranamed.   
   old_link_dest = os.path.realpath( fullpath )	
   print old_link_dest
   input("Press Enter to continue...")
   #'/usr/local/pgsql/basebackup/tablespace/fdc_ods_geo_ind'
   # Set new link destination.
   new_link_dest = old_link_dest.replace( '/usr/local/pgsql/tablespace','/usr/local/pgsql/basebackup/tablespace' )
   print new_link_dest
   input("Press Enter to continue...")
   #'/usr/local/pgsql/data/pg_tblcpc/tablespace/fdc_ods_geo_ind'
   # Recreate link.
   if os.path.lexists(fullpath):
      os.remove(fullpath)
   os.symlink( new_link_dest, fullpath )
   input("Press Enter to continue...")