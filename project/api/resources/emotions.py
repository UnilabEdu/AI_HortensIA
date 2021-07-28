from flask_restful import Resource
from project.models import Emotion
from project.front_integration.views import get_locale


class EmotionList(Resource):
    def get(self):
        emotions = Emotion.query.all()
        language = get_locale()
        if language == 'en':
            emotions_list = [{'emotion': emotion.name_en, 'similar': emotion.similar_en, 'definition': emotion.definition_en}
                             for emotion in emotions]
        elif language == 'ka':
            emotions_list = [{'emotion': emotion.name_ka, 'similar': emotion.similar_ka, 'definition': emotion.definition_ka}
                             for emotion in emotions]
        return emotions_list
