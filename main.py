#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template
from flask_restful import Api, Resource
from flask_cors import CORS

from contest_list_api import Contest

app = Flask(__name__)
CORS(app)
api = Api(app)


class Details(Resource):
    def get(self):
        contest=Contest()
        try:
            return contest.contest_list()

        except:
            return {'status': 'Failed'}


api.add_resource(Details,'/api/contest_list')


@app.errorhandler(404)
def invalid_route(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run()

