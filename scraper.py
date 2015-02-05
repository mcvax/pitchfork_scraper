# This is a template for a Python scraper on Morph (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries. You can use whatever libraries are installed
# on Morph for Python (https://github.com/openaustralia/morph-docker-python/blob/master/pip_requirements.txt) and all that matters
# is that your final data is written to an Sqlite database called data.sqlite in the current working directory which
# has at least a table called data.


#

import scraperwiki
import lxml.html
import time
html = scraperwiki.scrape("http://www.readings.com.au/collection/bestselling-books")
root = lxml.html.fromstring(html)

pos = 0
for el in root.cssselect("div.text year-end-review a"):
title = el.cssselect("h1")[0].text_content()
artist = el.cssselect("H2")[0].text_content()
publisher = el.cssselect("H3")[0].text_content()
link = el.attrib['href']
isbn = link.split("/")[2]
pos += 1

#print title
#print author
#print link
print isbn
link = "http://www.readings.com.au" + link
record = {"title" : title,
"artist" : artist,
"publisher" : publisher,
"isbn" : isbn,
"link" : link,
"pos" : pos,
"sdate" : time.strftime( "%Y-%m-%d" )
}
scraperwiki.sqlite.save(unique_keys=["isbn", "sdate"], data=record)
