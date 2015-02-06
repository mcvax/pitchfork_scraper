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
#html = scraperwiki.scrape("http://pitchfork.com/features/staff-lists/9465-the-top-100-albums-of-2010-2014/")
#root = lxml.html.fromstring(html)

html = scraperwiki.scrape("http://pitchfork.com/features/staff-lists/9465-the-top-100-albums-of-2010-2014")
root = lxml.html.fromstring(html)


pos = 0
#for el in root.cssselect("div[starts-with(@id, 'album')]"):
#for el in root.cssselect("div.#album-99"):
for el in root.cssselect("div.inner"):
  
  mytest = el.text_content()

  print str(mytest.encode('utf-8'))
  
  if hasattr(el, 'div div h1'):
    print 'One' + el.cssselect('div div h1')[0].text_content()
    
  if hasattr(el, 'div div div h1'):
    print 'Two' + el.cssselect('div div div h1')[0].text_content()
  
  if hasattr(el, 'div div div h1'):
    title = el.cssselect("div div div h1")[0].text_content()
  else:
    title = ''
    
  if hasattr(el, 'div div div h2'):
    artist = el.cssselect("div div div H2")[0].text_content()
  else:
    artist = ''
    
  #artist2 = el.cssselect("H2").text_content()
  #publisher = el.cssselect("H3")[0].text_content()
  #link = el.attrib['href']
  #isbn = link.split("/")[2]
  pos += 1

  print title
  print artist
  #print link
  #print isbn
  #link = "http://www.readings.com.au" + link
  record = {"title" : title,
  "artist" : artist,
  #"artist2" : artist,
  #"publisher" : publisher,
  #"isbn" : isbn,
  #"link" : link,
  #"pos" : pos,
  "sdate" : time.strftime( "%Y-%m-%d" )
  }
  
  scraperwiki.sqlite.save(unique_keys=["sdate"], data=record)
