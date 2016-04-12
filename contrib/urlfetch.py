import urllib


USERAGENT = 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; de-de) AppleWebKit/533.16 (KHTML, like Gecko) Version/4.1 Safari/533.16'
opener = urllib.request.build_opener()


def url_read(url, referer=None):
    request = urllib.request.Request(url)
    request.add_header('User-Agent', USERAGENT)
    if referer:
        request.add_header('Referer', referer)
    f = opener.open(request)
    result = f.read()
    f.close()
    return result
