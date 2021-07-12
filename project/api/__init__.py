from flask_restful import Api
from .resources.emotions import EmotionList
from .resources.subscribe import Subscribe

api = Api(prefix='/api/')

api.add_resource(EmotionList, '/emotionlist')
api.add_resource(Subscribe, '/subscribe')
