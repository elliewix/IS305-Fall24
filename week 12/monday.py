from lxml import etree

with open('hamlet-tei.xml', 'rb') as infile:
    xml = infile.read()
    # print(xml[:10])
    tree = etree.fromstring(xml)

print(tree)

ns = {'tei': 'http://www.tei-c.org/ns/1.0'}

# general pattern
# tree.xpath('xpath query as a string', namespaces = ns)

query = tree.xpath('//text()', namespaces = ns)
# print(query)

# here's our first alias to handle
# gets all the title text
print(tree.xpath('//tei:title/text()', namespaces = ns))

# get all the standard names

print(tree.xpath('//tei:person/@xml:id', namespaces = ns))

# now get the text of the names
# print(tree.xpath('//tei:person//text()', namespaces = ns))
# too much, let's be more specific

# print(tree.xpath('//tei:person/tei:persName/text()', namespaces = ns))
print(tree.xpath('//tei:person/tei:persName[@type = "standard"]/text()', namespaces = ns))