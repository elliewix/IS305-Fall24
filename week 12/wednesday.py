from lxml import etree

with open('hamlet-tei.xml', 'rb') as infile:
    xml = infile.read()
    tree = etree.fromstring(xml)

ns = {'tei': 'http://www.tei-c.org/ns/1.0'}

print(tree.xpath('//tei:sp[@who = "#F-ham-ham"]/tei:speaker/text()', namespaces = ns))

hamelet_names = tree.xpath('//tei:sp[@who = "#F-ham-ham"]/tei:speaker/text()', namespaces = ns)

from collections import Counter
print(Counter(hamelet_names))

hamelet_render = tree.xpath('//tei:sp[@who = "#F-ham-ham"]/tei:speaker/@rend', namespaces = ns)
print(Counter(hamelet_render))

# <stage rend="italic rightJustified" type="exit">Exeunt.</stage>

stagedir_text = tree.xpath('//tei:stage//text()', namespaces=ns)
stagedir_type = tree.xpath('//tei:stage/@type', namespaces=ns)

print(len(stagedir_text), len(stagedir_type))

just_stage_dir = tree.xpath('//tei:stage', namespaces=ns)
# print(just_stage_dir)
print(len(just_stage_dir))
for dir in just_stage_dir:
    print(dir.xpath('@type', namespaces = ns), "".join(dir.xpath('.//text()', namespaces = ns)))
