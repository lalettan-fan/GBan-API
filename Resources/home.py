from flask_restful import Resource


common_output = dict(
    status='Success',
    message='GBAN APi is Running'
)


class Home(Resource):
    def get(self):
        return common_output
    def post(self):
        return common_output