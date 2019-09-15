import os
import requests
import urllib2
import gzip
import xml.etree.ElementTree as ET

__ADDONS__ = []

for addon in os.listdir(os.curdir):
    if 'plugin' in addon or 'script' in addon or 'repository' in addon:
        __ADDONS__.append(addon)
# this function asks our repository and returns addons with different versions than in our local repo = candidates to be
# released
def find():
    response = urllib2.urlopen('https://raw.githubusercontent.com/lama18/repository/master/repo/addons.xml.gz').read()
    print response
    #gunzip_response = gzip.GzipFile(fileobj=response)
    #released_addons = gunzip_response.read()
    #print content
    #f=gzip.open(requests.get('https://raw.githubusercontent.com/lama18/repository/master/repo/addons.xml.gz').text,'rb')
    #released_addons=f.read()
    try:
        root = ET.XML( released_addons.encode('utf-8') )
    except: # initially there are no addons.xml
        print 'Failed to parse remove addons.xml - releasing everything'
        return __ADDONS__
    to_release = []
    for id in __ADDONS__:
        released = root.find('addon[@id=\"%s\"]' % id)
        if released == None:
            to_release.append(id)
            continue
        released_version = released.get('version')
        xmldoc = ET.parse(os.path.join(id,'addon.xml'))
        new_version =xmldoc.getroot().get('version')
        if not released_version == new_version:
            to_release.append(id)
    return to_release

if __name__ == "__main__":
    for id in find():
        print "Addon %s " % id
