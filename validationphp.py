import lxml.html
import sys
import json

XPATH_RESULT = '//dl[@class="dl-horizontal"]/dt[text() = "Resultado"]/following-sibling::dd[1]/b/text()'

content = sys.argv[1]

parsed = lxml.html.fromstring(content.decode('utf-8'))

result = parsed.xpath(XPATH_RESULT)

print (result[0]).encode('utf-8')

