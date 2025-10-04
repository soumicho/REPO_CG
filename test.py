import validators
import urllib.request

x=urllib.request.urlopen("http://prosapppdci:51000/startPage").getcode()
print(x)