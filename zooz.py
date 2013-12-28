import urllib2
import urllib
from urlparse import parse_qs


class ZoozClient:
    def __init__(self, unique_id='', app_key='', sandbox=False):
        if sandbox:
            url = 'https://sandbox.zooz.co/mobile/SecuredWebServlet'
        else:
            url = 'https://app.zooz.com/mobile/SecuredWebServlet'

        self.request = urllib2.Request(url)
        self.request.add_header('ZooZUniqueID', unique_id)
        self.request.add_header('ZooZAppKey', app_key)
        self.request.add_header('ZooZResponseType', 'NVP')

    def make_request(self, **kwargs):
        self.request.add_data(urllib.urlencode(kwargs))
        return parse_qs(urllib2.urlopen(self.request).read())

    def __getattr__(self, item):
        def function(**kwargs):
            kwargs['cmd'] = item
            return self.make_request(**kwargs)

        return function

