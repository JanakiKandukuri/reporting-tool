from flask import Flask, render_template, request, redirect, jsonify
from reportingTooldb import get_topThreeArticles, get_popularAuthors, get_answersErrorPercent
from flask_wtf import FlaskForm
from wtforms.fields import SelectField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


class Form(FlaskForm):
    question = SelectField('question', choices=[
        ('select a question', 'Select a Question'),
        ('all', 'View All'),
        ('articles', 'Display top 3 articles in descending order'),
        ('authors', 'Display authors and total views of their articles in descending order'),
        ('error', 'Display requests that lead to more than 1% of errors on a day')
    ])

@app.route('/', methods=['GET','POST'])
def main():
    form = Form()
    value = dict(form.question.choices).get(form.question.data)
    print(value)
    return render_template('reportingTool.html',form=form)

@app.route('/question/<question>')
def report(question): 
    answer = "will return in a sec"
    if question == 'articles':
        answer = answersTopTreArticles()
    elif question == 'authors':
        answer = answersTopAuthors()
    elif question == 'error':
        answer = answersErrorPercent()
    elif question == 'all': 
        answer = answersViewAll()
    else :
       answer = answersViewAll()
    return jsonify({'answer': answer})


def answersTopTreArticles():
    articles = [(article,totalViews) for article, totalViews in get_topThreeArticles()]
    resultSet = ["********* TOP 3 ARTICLES ***************"]
    print('********* TOP 3 ARTICLES *************** ')
    for a in range(3):
        resultSet.append(articles[a][0][9:]+' ---------- '+str(articles[a][1])+' views')
        print(articles[a][0][9:]+' ---------- '+str(articles[a][1])+' views')
    return resultSet

def answersTopAuthors():
    authors = [(author,totalArticles) for author, totalArticles in get_popularAuthors()]
    resultSet = ["********* AUTHORS AND THEIRS TOTAL VIEWS ***************"]
    print('********* AUTHORS AND THEIRS TOTAL VIEWS *************** ')
    for a in authors:
        resultSet.append(a[0]+' ---------- '+str(a[1])+' views')
        print(a[0]+' ---------- '+str(a[1])+' views')
    return resultSet

def answersErrorPercent():
    errors = [(date,errorPercent) for date, errorPercent in get_answersErrorPercent()]
    resultSet = ["********* Days lead to > 1% Errors ***************"]
    print('********* Days lead to > 1% Errors *************** ')
    for e in errors:
        resultSet.append(e[0]+' ---------- '+str(e[1])+'% views')
        print(e[0]+' ---------- '+str(e[1])+' views')
    return resultSet

def answersViewAll():
    resultSet = ["********* View All Answers ***************",answersTopTreArticles(),answersTopAuthors(),answersErrorPercent()]
    print(resultSet)
    return resultSet

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
