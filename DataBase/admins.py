from DataBase import Mongo
import secrets

class Database(Mongo):
    def __init__(self):
        self.col = self.db.admins

    def get_admin(self, api_key:str):
        admin = self.col.find_one({'api_key': api_key})
        if admin:
            return admin['name']
        else:
            return False

    def add_admin(self,name:str):
        generated_key = secrets.token_urlsafe(16)
        admin = dict(
            name=name,
            api_key=generated_key
        )
        return self.col.insert_one(admin)

adminDb = Database()