from flask_restful import Resource, abort, reqparse
from flask import request
from DataBase.admins import adminDb
from DataBase.banlist import banlistDb

ban_post_args = reqparse.RequestParser()
ban_post_args.add_argument("user_id", type=int, help="Please provide the UserId to be banned", required=True)
ban_post_args.add_argument("reason", type=str, help="Please provide the Reason of Ban", required=True)


class Ban(Resource):
    def post(self):
        api_key = request.headers.get('X-Api-Key', None)
        if not api_key:
            abort(404, status=False, message="X-Api-Key is missing in the header")
        admin = adminDb.get_admin(api_key)
        if admin:
            args = ban_post_args.parse_args()
            if banlistDb.is_user_banned(args.get('user_id')):
                ban = banlistDb.get_user(args.get('user_id'))
                banned_by = ban['banned_by']
                banlistDb.ban_user(args.get('user_id'), reason=args.get('reason'), banned_by=banned_by)
                return {'status': True, 'message': f'User is already Banned by {banned_by}'}, 201
            else:
                banlistDb.ban_user(
                    user_id=args.get('user_id'),
                    reason=args.get('reason'),
                    banned_by=admin
                )
                return {'status': True, 'message': 'User is Banned'}, 200
        else:
            abort(404,status=False,message="X-Api-Key is Invalid")
