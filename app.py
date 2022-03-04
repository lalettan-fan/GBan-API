from flask import Flask
from flask_restful import Api
from Resources import Home, Ban, User, Unban, Banned
import threading, os, requests, time

app = Flask(__name__)
api = Api(app)


api.add_resource(Home, "/")
api.add_resource(Ban, "/api/ban_user")
api.add_resource(Unban, "/api/unban_user")
api.add_resource(Banned, "/api/banned")
api.add_resource(User, "/api/user/<int:user_id>")

@app.route('/docs')
def documention():
    return "DOCS UNAVAIABLE"
def timed_check():
    url= os.environ.get('URL', 'https://www.google.com')
    while(True):
        print(requests.get(url))
        time.sleep(600)

if __name__ == '__main__':
    th = threading.Thread(target=timed_check)
    th.daemon = True
    th.start()
    app.run()
