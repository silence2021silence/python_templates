from lxml import etree


tree = etree.HTML(html)
# html -> 网页源码
content = tree.xpath(xpath)
# xpath -> xpath表达式
# content -> 取得内容 type:list
