import os
from macos.currentinfo import show_current_wifi
from macos.installer.initscript import place_xml

base_command = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport"
result = show_current_wifi(base_command)
# print result

xml_path = "/System/Library/LaunchDaemons/zerop"
place_xml(xml_path)
# change permissin of the file
os.chmod(xml_path, 0777)
# cahnge owner/group of the file

print ("writing succedded")
