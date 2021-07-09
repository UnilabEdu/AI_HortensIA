from flask_restful import Resource
from project.models import Emotion


class EmotionList(Resource):
    def get(self):
        emotions = Emotion.get_all()
        emotions_list = [{'emotion': emotion.name_en, 'synonym': emotion.synonym_en, 'example': emotion.example_en}
                         for emotion in emotions]
        return emotions_list
