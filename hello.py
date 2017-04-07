# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
import pandas as pd

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<category>')
def category(category):
    web_csv = pd.read_csv(
        "/Users/duqi/qiusuo/static/website_info.csv", encoding="gb2312")
    data = web_csv[web_csv['category'] == category]
    #website = [u'网易', u'京东', u'阿里巴巴', u'杜七']
    return render_template('category.html', title=category, webcsv=data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
