#-------------------------------------------------------------------------------
# Name:        rishabh
# Purpose:
#
# Author:      Rishabh Roy
#
# Created:     30/01/2014
# Copyright:   (c) kiit 2014
# Licence:     <all right reserved to rishabh roy you can visit my code repository on rishabhsixfeet@gmail.com>
#-------------------------------------------------------------------------------
import Tkinter

import requests
payload ={
'txtRoll' :'1205064',
'txtEnroll':'12148423623',
'btnSubmit':'Submit'
}
import urllib2
import urllib
import cookielib

# Store the cookies and create an opener to hold them
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

# Add our headers
opener.addheaders = [('User-agent', 'Tester')]

# Install the opener, changes the global opener to the one we just made
urllib2.install_opener(opener)

# URL for authentification
auth_url = 'http://59.145.203.105'
data = urllib.urlencode(payload)
import BeautifulSoup
from BeautifulSoup import BeautifulSoup

# Build request object (supplying 'data' makes it a POST)
req = urllib2.Request(auth_url, data)


# Make request and store in resp
resp = urllib2.urlopen('http://59.145.203.105/printform.asp').read()

# Print out the resp from server
soup= BeautifulSoup(resp)
print soup



