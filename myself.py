import requests
import lxml.html as html

HOME_URL = 'https://www.larepublica.co/'

XPATH_LINK_TO_ARTICLE = '//h2[@class="headline"]/a/@href'
XPATH_TITLE = '//h1[@class="headline"]/a/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="articleWrapper  "]/p[not(@class)]/text()'


def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')  # take the content
            parsed = html.fromstring(home)  # prepare this html
            links_to_notice = parsed.xpath(XPATH_LINK_TO_ARTICLE)  # apply
            # print(links_to_notice.pop())
        else:
            raise ValueError('error: {%s}' % response.status_code)
    except ValueError as ve:
        print(ve)


def run():
    parse_home()


if __name__ == '__main__':
    run()
