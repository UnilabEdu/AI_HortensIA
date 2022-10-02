from flask_restful import Resource

from project.views.main.views import get_locale
from project.models import Emotion


class EmotionList(Resource):
    def get(self):
        """
        returns a dictionary of emotions data (emotion name, similar words, definitions) of current language
        """

        emotions = Emotion.query.all()
        language = get_locale()
        if language == 'en':
            emotions_list = [{'emotion': emotion.name_en,
                              'similar': emotion.similar_en,
                              'definition': emotion.definition_en}
                             for emotion in emotions]

        elif language == 'ka':
            emotions_list = [{'emotion': emotion.name_ka,
                              'similar': emotion.similar_ka,
                              'definition': emotion.definition_ka}
                             for emotion in emotions]

        else:
            return {'error:' 'current language is not supported'}, 400

        return emotions_list, 200
