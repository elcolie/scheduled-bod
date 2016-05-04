import os, sys, requests
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#curl -H "Content-Type: application/json" -X POST -d '{"job_id":"ac97682c-c81e-4170-bb46-8301df317587"}' http://localhost:9000/scheduled-bod


class UIHRecurrence(Resource):
    def post(self):
        """Receive Post from UIH-scheduler"""
        data = request.get_json()
        res_msg = "Launching job id : '{0}'".format(data['job_id'])
        print(data['job_id'])
        return res_msg, 200


def main(*args, **kwargs):
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        if len(sys.argv) > 2 and sys.argv[1] == 'debug':
            app.debug = True
        else:
            app.debug = False
        app.run(host='localhost', port=9000)
    except (KeyboardInterrupt, SystemExit):
        print("Exit program")


if __name__ == '__main__':
    api.add_resource(UIHRecurrence, '/scheduled-bod')
    main()
