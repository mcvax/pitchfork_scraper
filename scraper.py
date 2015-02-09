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

import scraperwiki
import lxml.html
import time

def scrapePage(url):
  
  html = None
  attempts = 0
  
  while html == None and attempts < 3:
    try: html = scraperwiki.scrape(url)
    except:
      attempts += 1
      continue
  
    if html == None and attempts == 3:
      print 'Unable to scrape ' + review_href

  return html

def extractTrack(html, mytrackType):

  root = lxml.html.fromstring(html)

  pagetitle = root.cssselect('head title')[0].text_content()
  
  myRoot = "div[id^='{0}']".format(mytrackType)
  
  for el in root.cssselect(myRoot):
  
      #mytest = el.text_content()
      #print str(mytest.encode('utf-8'))
      
      if len(el.cssselect('div.inner div.title h1')) ==0 : continue
      title = el.cssselect('div.inner div.title h2')[0].text_content()
      artist = el.cssselect("div.inner div.title h1")[0].text_content()
      publisher = el.cssselect("div.inner div.title h3")[0].text_content()  
      rank = el.cssselect("div.inner div.review-content div.rank")[0].text_content()
      reviewtext = el.cssselect("div.inner div.review-content p")[0].text_content()  
      #link = el.attrib['href']
      #isbn = link.split("/")[2]
    
      #print title
      #print artist
      #print link
      #link = "http://www.readings.com.au" + link
      record = {
      "pagetitle" : pagetitle,
      "tracktype" : mytrackType,
      "title" : title,
      "artist" : artist,
      "publisher" : publisher,
      "rank" : rank,
      "reviewtext" : reviewtext,
      "scrape_date" : time.strftime( "%Y-%m-%d" )
    
      }
      
      scraperwiki.sqlite.save(unique_keys=["scrape_date", "rank"], data=record)
  
  return

def extractPage (baseURL, mytrackType):

  page = 1

  while page < 6:

    myhtml = scrapePage(baseURL.format(page))

    extractTrack(myhtml, mytrackType)

    page += 1

  return

### Start extraction

mybaseURL = "http://pitchfork.com/features/staff-lists/9465-the-top-100-albums-of-2010-2014/{0}/"
extractPage(mybaseURL, "album")
  

