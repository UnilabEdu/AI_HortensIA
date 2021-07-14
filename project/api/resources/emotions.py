from flask_restful import Resource
from project.models import Emotion
from project.front_integration.views import get_locale


class EmotionList(Resource):
    def get(self):
        emotions = Emotion.get_all()
        language = get_locale()
        if language == 'en':
            emotions_list = [{'emotion': emotion.name_en, 'synonym': emotion.synonym_en, 'example': emotion.example_en}
                             for emotion in emotions]
        elif language == 'ka':
            emotions_list = [{'emotion': emotion.name_ka, 'synonym': emotion.synonym_ka, 'example': emotion.example_ka}
                             for emotion in emotions]
        return emotions_list
