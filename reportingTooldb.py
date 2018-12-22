# "Database code" for the DB NewsData.

import datetime
import psycopg2
import bleach
from bleach.sanitizer import Cleaner
DBNAME = "news"


def get_topThreeArticles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''SELECT articles.title article, count(log.path) totalViews FROM
          articles JOIN log ON articles.slug=substring(log.path, 10) and
          log.status LIKE '%200%' GROUP BY articles.title ORDER BY
          count(log.path) desc; ''')
    results = c.fetchall()
    cleaner = Cleaner()
    cleanResults = []
    for r in results:
        articles = r[0]
        totalViews = r[1]
        cleaner.clean(articles+'')
        cleanResults.append((articles, totalViews))
    db.close()
    return cleanResults


def get_popularAuthors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''SELECT  name, t3.total FROM authors JOIN
            (SELECT t1.author id, sum(val) total FROM articles t1 JOIN
            (SELECT path, count(path) val FROM log WHERE log.status LIKE
            '%200%' GROUP BY path) t2 ON t1.slug=substring(t2.path, 10)
            GROUP BY t1.author ORDER BY total desc)
            t3 ON authors.id = t3.id;''')
    results = c.fetchall()
    cleaner = Cleaner()
    cleanResults = []
    for r in results:
        authors = r[0]
        totalArticlesViews = r[1]
        cleaner.clean(authors+'')
        cleanResults.append((authors, totalArticlesViews))
    db.close()
    return cleanResults


def get_answersErrorPercent():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''SELECT t3.time, t3.per FROM (SELECT t1.dateVal as time,
             (t1.error*100.0/t2.totalCount*1.0) as per FROM (SELECT
             TO_CHAR(time, 'Monthdd,YYYY') dateVal,count(status) as error
             FROM log WHERE status LIKE '%4%' or status LIKE '%5%'
             GROUP BY dateVal) as t1, (SELECT TO_CHAR(time, 'Monthdd,YYYY')
             dateVal, count(status) as totalCount FROM log GROUP BY
             dateVal) as t2 WHERE t1.dateVal = t2.dateVal) as t3
             WHERE t3.per > 1;''')
    results = c.fetchall()
    cleaner = Cleaner()
    cleanResults = []
    for r in results:
        date = r[0]
        errorPercent = r[1]
        cleaner.clean(date+'')
        cleanResults.append((date, errorPercent))
    db.close()
    return cleanResults
