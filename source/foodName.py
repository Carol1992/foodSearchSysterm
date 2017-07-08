import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask_restful import Resource, Api
import webbrowser

app = Flask(__name__)
api = Api(app)
with app.app_context():

    DATABASE = 'spider.sqlite'

    def get_db():
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(DATABASE)
        return db

    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    def query_db(query, args=(), one=False):
        cur = get_db().execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv

    mysql = 'select code, url, product_name from Food where product_name = ?'
    food = query_db(mysql, ["Rotini"])
    if food is None:
        print ('No such food')
    else:
        count = 0
        info = []
        for r in food:
            count += 1
            mydict = {
                'name': r[2],
                'code': r[0],
                'url': r[1]
            }
            info.append(mydict)
        myobj = {
            'rcode': '0000',
            'totalCount': count,
            'item': info
        }

        class getFoodInfo(Resource):
            def get(self):
                return myobj
        api.add_resource(getFoodInfo, '/food')
        webbrowser.open('http://localhost:5000/food')

    if __name__ == "__main__":
        app.run(host= '0.0.0.0')