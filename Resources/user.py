from flask_restful import Resource
from DataBase.banlist import banlistDb

def get_res(user_id, status,banned_by=None, banned_date=None, reason=None):
    return dict(
        user_id=user_id,
        status=status,
        banned_by=banned_by,
        banned_date=banned_date,
        ban_reason=reason
    )


def get_unban_res(user_id, status,unbanned_by,banned_date,reason):
    return dict(
        user_id=user_id,
        status=status,
        unbanned_by=unbanned_by,
        unbanned_date=banned_date,
        unban_reason=reason
    )


class User(Resource):
    def get(self,user_id):
        if not banlistDb.check_user_in_db(user_id):
            return {'status': True, 'response':get_res(user_id,'User is not banned')}
        else:
            ban = banlistDb.get_user(user_id)
            if ban['status'] == 'banned':
                res = 'User is banned'
                return {'status': True, 'response': (get_res(user_id, res,ban['banned_by'],ban['first_banned'].strftime("%m/%d/%Y"),ban['ban_reason']))}
            else:
                res = 'User is unbanned'
                return {'status': True,
                        'response': get_unban_res(user_id, res, ban['unbanned_by'], ban['recently_unbanned'].strftime("%m/%d/%Y"), ban['unban_reason'])}
