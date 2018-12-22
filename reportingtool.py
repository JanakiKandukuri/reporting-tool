from reportingTooldb import get_topThreeArticles
from reportingTooldb import get_popularAuthors, get_answersErrorPercent


def answersTopTreArticles():
    articles = [(art, view) for art, view in get_topThreeArticles()]
    resultSet = ["********* TOP 3 ARTICLES ***************"]
    print('********* TOP 3 ARTICLES *************** ')
    for a in range(3):
        resultSet.append(articles[a][0][9:]+' '+str(articles[a][1])+' views')
        print(articles[a][0][9:]+' '+str(articles[a][1])+' views')
    return resultSet


def answersTopAuthors():
    authors = [(autr, ttlArtls) for autr, ttlArtls in get_popularAuthors()]
    resultSet = ["********* AUTHORS AND THEIRS TOTAL VIEWS ***************"]
    print('********* AUTHORS AND THEIRS TOTAL VIEWS *************** ')
    for a in authors:
        resultSet.append(a[0]+' ---------- '+str(a[1])+' views')
        print(a[0]+' ---------- '+str(a[1])+' views')
    return resultSet


def answersErrorPercent():
    errors = [(date, errPer) for date, errPer in get_answersErrorPercent()]
    resultSet = ["********* Days lead to > 1% Errors ***************"]
    print('********* Days lead to > 1% Errors *************** ')
    for e in errors:
        resultSet.append(e[0]+' ---------- '+str(e[1])+'% views')
        print(e[0]+' ---------- '+str(e[1])+' views')
    return resultSet


answersTopTreArticles()
answersTopAuthors()
answersErrorPercent()
