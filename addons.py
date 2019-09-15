__ADDONS__ = [
    "plugin.video.dmd-czech.aktualne",
    "plugin.video.dmd-czech.novaplus",
    "plugin.video.dmd-czech.stream",
    "plugin.video.ivysilani",
    "plugin.video.primaplay",
    "script.module.stream.resolver",
    "script.module.demjson",
<<<<<<< Updated upstream
=======
    "repository.kodi",
>>>>>>> Stashed changes
    "plugin.video.stream-cinema",
    "plugin.video.mall.tv",
    "plugin.video.dmd-czech.xtv",
    "plugin.video.seznam.zpravy",
    "repository.kodi"
    ]

import os
import requests
import xml.etree.ElementTree as ET
from addons import __ADDONS__

# this function asks our repository and returns addons with different versions than in our local repo = candidates to be
# released
def find():
    released_addons = requests.get('https://raw.githubusercontent.com/lama18/repository/master/repo/addons.xml').text
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
