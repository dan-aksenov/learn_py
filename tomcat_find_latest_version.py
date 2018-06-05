# find apache latest version
# inspired by https://github.com/galaxyproject/ansible-postgresql/blob/master/files/get_repo_rpm_release.py
# so far tested on tomcat 7,8 and 9

import re
import sys
import urllib2

major_verion = sys.argv[1]

url = "http://apache-mirror.rbc.ru/pub/apache/tomcat/tomcat-" + str(major_verion) + "/"

try:
    distro = urllib2.urlopen(url)
except urllib2.HTTPError, e:
    print >>sys.stderr, "Failed to fetch directory list from %s" % url
    raise

re_match = '[\'"]v' + major_verion +'.*[\'"]'
latest_version = max(re.findall(re_match,distro.read(),flags=re.I))
get_latest_url = "http://apache-mirror.rbc.ru/pub/apache/tomcat/tomcat-" + major_verion + "/" + latest_version.strip('\"') + "bin/apache-tomcat-" + latest_version.strip('\"v/') + "-deployer.tar.gz"

print get_latest_url
sys.exit(0)