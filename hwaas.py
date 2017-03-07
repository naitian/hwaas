import falcon
import json


class HelloWorld:
    def on_get(self, req, resp):
        """Handles GET requests"""
        hw = 'hello world'

        hw = hw + '!' if req.get_param_as_bool('excited') else hw
        hw = hw + '!' if req.get_param_as_bool('excited') else hw

        resp.body = json.dumps(hw)

api = falcon.API()
api.add_route('/', HelloWorld())
