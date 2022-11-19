from utils import get_by_pk, get_by_skill, get_all
from flask import Flask


app = Flask(__name__)


@app.route('/')
def page_index():
    result = '<br>'
    candidates = get_all()

    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'

    return f'<pre> {result} </pre>'


@app.route('/candidate/<int:pk>')
def get_candidate(pk):
    candidate = get_by_pk(pk)
    result = '<br>'
    result += candidate['name'] + '<br>'
    result += candidate['position'] + '<br>'
    result += candidate['skills'] + '<br>'
    result += '<br>'

    return f"""
        <img src= "{candidate['picture']}">
        <pre>{result}</pre> 
    """


@app.route('/candidate/<skills>')
def get_skills(skills):
    candidates = get_by_skill(skills)
    result = '<br>'
    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'

    return f'<pre> {result} </pre>'


app.run(debug=True)


