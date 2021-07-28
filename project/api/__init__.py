from flask_restful import Api
from .resources.emotions import EmotionList
from .resources.tickets import GetTextPostTicket
from .resources.subscribe import Subscribe

api = Api(prefix='/api/')

api.add_resource(EmotionList, '/emotionlist')  # get emotions data (name, similar words, definition) of current language
api.add_resource(GetTextPostTicket, '/ticketrequest')  # GET to get 'text' data, # POST to add a row to 'tickets'
api.add_resource(Subscribe, '/subscribe')  # POST request to add email to db table 'subscribed_emails'
