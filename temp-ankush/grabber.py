import urllib2
import re

def grabber(url):
    """ Takes a URL string as input, returns a list containing all URLs in that site """
    URLs = []
    if not url.startswith('http'):
        url = 'http://' + url
    handle = urllib2.urlopen(url)
    data = handle.read()
    r = re.findall('href=\"(.*?)\"', data)
    for i in r:
        if i is None:
            pass
        if not i.startswith('http'):
            if not i.startswith('/'):
                i = '/' + i
            i = url + i
            URLs.append(i)
    return URLs

if __name__ == "__main__":
    TEST_URL = "intranet.iiit.ac.in"
    output = grabber(TEST_URL)
    print output
