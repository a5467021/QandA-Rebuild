from app.extra import db, params, rand_item, get_image_amount
from app.models import QuestionModel, CategoryNameModel
from flask_restful import Resource, request
import string
import random
import json

class RandomQuestion(Resource):
    '''
    This address deals with incoming requests acquiring
    questions with specific categories.
    '''
    
    QUESTIONS_AMOUNT = 4
    IMAGE_PREFIX = '/api/static/bgimage'

    def post(self): # supposed category is a list with names in Chinese
        '''get questions'''
        categories = request.json.get('categories')
        if categories == None: # empty categories implies a new user
            categories = CategoryNameModel.get_all_categories()
        categories = rand_item(categories, self.QUESTIONS_AMOUNT)
        question = {}
        n = 1
        for category in categories:
            title = 'ques{0}'.format(n); # make the response structure
            question[title] = {}
            # get the question from database
            question[title]['description'] = rand_item(QuestionModel.get_by_category(category), 1)[0]
            if get_image_amount(category) < 1:
                question[title]['image'] = self.IMAGE_PREFIX + 'default.jpg'
            else:
                question[title]['image'] = self.IMAGE_PREFIX + category + '/'\
                    + str(random.randint(1, get_image_amount(category))) + '.jpg'
            question[title]['category'] = category
            n += 1
        return question
