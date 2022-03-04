from flask import Flask
from flask_restful import Api
from DataBase.admins import adminDb
from Resources import Home, Ban, User, Unban, Banned

app = Flask(__name__)
api = Api(app)


api.add_resource(Home, "/")
api.add_resource(Ban, "/api/ban_user")
api.add_resource(Unban, "/api/unban_user")
api.add_resource(Banned, "/api/banned")
api.add_resource(User, "/api/user/<int:user_id>")

@app.route('/docs')
def documention():
    x = adminDb.add_admin('W4RR10R')
    return x

if __name__ == '__main__':
    app.run(debug=True)