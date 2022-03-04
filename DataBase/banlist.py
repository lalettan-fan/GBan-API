from DataBase import Mongo
from datetime import datetime

class Database(Mongo):
    def __init__(self):
        self.col = self.db.banlist

    def new_user(self, user_id: int, reason: str, banned_by: str, status: str = 'banned'):
        return dict(
            user_id= user_id,
            ban_reason= reason,
            status= status,
            banned_by= banned_by,
            first_banned= datetime.now(),
            recently_banned=datetime.now(),
            recently_unbanned='None',
            unbanned_by='None',
            unban_reason='None'
        )

    def check_user_in_db(self,user_id: int):
        user = self.col.find_one({'user_id': user_id})
        if user:
            return True
        else:
            return False

    def ban_user(self,user_id: int, reason: str, banned_by: str):
        if not self.check_user_in_db(user_id):
            user = self.new_user(
                user_id=user_id,
                reason=reason,
                banned_by=banned_by
            )
            self.col.insert_one(user)
        else:
            user = self.col.update_one({'user_id': user_id}, { "$set": { "status": "banned", "ban_reason": "reason", "recently_banned": datetime.now()}})

    def unban_user(self,user_id, unbanned_by:str, reason: str = 'None'):
        user = self.col.update_one({'user_id': user_id},
                                   {"$set": {"status": "unbanned", "recently_unbanned": datetime.now(), "unbanned_by": unbanned_by, "unban_reason" :reason}})

    def is_user_banned(self,user_id):
        user = self.col.find_one({"user_id" :user_id})
        if not user:
            return False
        if user['status'] == 'banned':
            return True
        else:
            return False

    def get_user(self,user_id):
        user = self.col.find_one({"user_id": user_id})
        if not user:
            return None
        else:
            return user

    def get_all_banned(self):
        user = self.col.find({"status": "banned"})
        if not user:
            return None
        else:
            return user

banlistDb = Database()