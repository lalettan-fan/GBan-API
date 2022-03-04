from flask_restful import Resource, abort, reqparse
from flask import request
from DataBase.banlist import banlistDb
from DataBase.admins import adminDb

ban_post_args = reqparse.RequestParser()
ban_post_args.add_argument("user_id", type=int, help="Please provide the UserId to be banned", required=True)
ban_post_args.add_argument("reason", type=str, help="Please provide the Reason of Ban", required=True)

class Unban(Resource):
    def post(self):
        api_key = request.headers.get('X-Api-Key', None)
        if not api_key:
            abort(404, status=False, message="X-Api-Key is missing in the header")
        admin = adminDb.get_admin(api_key)
        if admin:
            args = ban_post_args.parse_args()
            if not banlistDb.check_user_in_db(args.get('user_id')):
                return {'status': True, 'message': f'User is not Banned Yet'}, 201
            if not banlistDb.is_user_banned(args.get('user_id')):
                ban = banlistDb.get_user(args.get('user_id'))
                banned_by = ban['unbanned_by']
                banlistDb.unban_user(args.get('user_id'), reason=args.get('reason'), unbanned_by=banned_by)
                return {'status': True, 'message': f'User is already UnBanned by {banned_by}'}, 201
            else:
                banlistDb.unban_user(
                    user_id=args.get('user_id'),
                    reason=args.get('reason'),
                    unbanned_by=admin,
                )
                return {'status': True, 'message': 'User is Banned'}, 200
        else:
            abort(404, status=False, message="X-Api-Key is Invalid")

