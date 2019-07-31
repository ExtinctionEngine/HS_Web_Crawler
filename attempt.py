from urllib.request import urlopen
from link_finder import LinkFinder
from spider import Spider


def gather_links_attempt(page_url):
    html_string = ''
    try:
        response = urlopen(page_url)
        if 'text/html' in response.getheader('Content-Type'):
            html_bytes = response.read()
            html_string = html_bytes.decode("utf-8")
        finder = LinkFinder(Spider.base_url, page_url)
        finder.feed(html_string)
    except:
        print('Error: can not crawl page')
        return set()
    return finder.page_links()


gather_links_attempt('https://coreyms.com/')

