import json

from flask_restful import Resource
from flask import jsonify
from json import dumps
from DataBase.banlist import banlistDb

def get_user(user):
    return {
        'user_id':user['user_id'],
        'ban_reason' : user['ban_reason'],
        'status' : user['status'],
        'banned_by' : user['banned_by'],
        'banned_on' : user['first_banned'].strftime("%m/%d/%Y"),
        'unbanned_by' : user['unbanned_by'],
        'unban_reason' : user['unban_reason'],
        'unbanned_on' : user['recently_unbanned'].strftime("%m/%d/%Y")
    }

class Banned(Resource):
    def get(self):
        users = list(banlistDb.get_all_banned())
        return {'status': True, 'count': len(users), 'result':[get_user(user) for user in users]}
    def post(self):
        users = list(banlistDb.get_all_banned())
        return {'status': True, 'count': len(users), 'result': [get_user(user) for user in users]}