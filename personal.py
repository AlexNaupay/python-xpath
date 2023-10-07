import requests
import lxml.html

_URL = 'https://intranet.igp.gob.pe/gestion-rrhh/public/listado_personal'
XPATH_LINK_TO_PERSONAL_NAMES = '//div[@class="frame"]/b/text()'
XPATH_LINK_TO_PERSONAL_EMAILS = '//div[@class="frame"]/div[@class="persona-datos2"]/div[1]/text()'
XPATH_LINK_TO_PERSONAL_CAMPUS = '//div[@class="frame"]/div[@class="rh-extra content"]/span[1]/text()'

response = requests.get(_URL)

print("Response status code %s" % response.status_code)

content = response.content.decode('utf-8')  # DECODE content
parsed = lxml.html.fromstring(content)  # parsed to special format
personal_names = parsed.xpath(XPATH_LINK_TO_PERSONAL_NAMES)  # like jquery selector
personal_emails = parsed.xpath(XPATH_LINK_TO_PERSONAL_EMAILS)  # like jquery selector
personal_campus = parsed.xpath(XPATH_LINK_TO_PERSONAL_CAMPUS)  # like jquery selector

for name in personal_names:
    print(name)

for email in personal_emails:
    print(email.strip())

for campus in personal_campus:
    print(campus.strip())

length = len(personal_names)
i = 0
while i < length:
    print("%s, %s, %s" % (personal_names[i], personal_emails[i].strip(), personal_campus[i].strip()))
    i = i + 1
