# "Database code" for the DB NewsData.

import datetime
import psycopg2
import bleach
from bleach.sanitizer import Cleaner



DBNAME = "news"

def get_topThreeArticles():
  """Return top 3 articles from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("Select log.path article, count(log.path) totalViews from articles join log on articles.slug=substring(log.path, 10) and log.status like '%200%' group by log.path order by count(log.path) desc; ")
  results = c.fetchall()
  cleaner = Cleaner()
  cleanResults = []
  for r in results:
    articles = r[0]
    totalViews = r[1]
    cleaner.clean(articles+'')
    cleanResults.append((articles,totalViews))  
  db.close()
  return cleanResults

def get_popularAuthors():
  """Return top authors from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("Select  name, t3.total from authors join (Select t1.author id, sum(val) total from articles t1 join (select path, count(path) val from log where log.status like '%200%' group by path) t2 on t1.slug=substring(t2.path, 10) group by t1.author order by total desc) t3 on authors.id = t3.id;")
  results = c.fetchall()
  cleaner = Cleaner()
  cleanResults = []
  for r in results:
    authors = r[0]
    totalArticlesViews = r[1]
    cleaner.clean(authors+'')
    cleanResults.append((authors,totalArticlesViews))  
  db.close()
  return cleanResults

def get_answersErrorPercent():
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select TO_CHAR(time, 'Monthdd,YYYY') dateVal, ROUND(count(status)*100.0/ ((select count(status) from log where status like '%4%' or status like '%5%')*1.0),2) as statusCount from log where status like '%4%' or status like '%5%' group by dateVal order by dateVal;")
  results = c.fetchall()
  cleaner = Cleaner()
  cleanResults = []
  for r in results:
    date = r[0]
    errorPercent = r[1]
    cleaner.clean(date+'')
    cleanResults.append((date,errorPercent))  
  db.close()
  return cleanResults


