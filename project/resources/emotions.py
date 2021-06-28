from flask_restful import Resource
from project.models import Emotion


class EmotionList(Resource):
    def get(self):
        emotions = Emotion.get_all()
        emotions_list = [{'emotion': emotion.name, 'synonym': emotion.synonym, 'example': emotion.example}
                         for emotion in emotions]
        return emotions_list
