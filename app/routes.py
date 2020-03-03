from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  title = 'Create & Train Model'
  return render_template('index.html', title=title)

@app.route('/test')
def test():
  title = 'Test Model'
  return render_template('test.html', title=title)

@app.route('/validate')
def validate():
  title = 'Validate Model'
  return render_template('validate.html', title=title)