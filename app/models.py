from app.extra import db


class QuestionModel(db.Model):
    '''question model'''
    __tablename__ = 'question'

    qid = db.Column(db.Integer, primary_key = True, nullable = False) # unique question id
    cid = db.Column(db.Integer, db.ForeignKey('name_category.category_id')) # kinds of questions
    description = db.Column(db.String(200)) # description of the question

    category_name = db.relationship('CategoryNameModel', backref = 'question')

    @staticmethod
    def get_category_amount():
        return len(dict(QuestionModel.query))

    @staticmethod
    def get_by_category(category_name):
        query = QuestionModel.query.\
            filter(QuestionModel.cid == CategoryNameModel.category_id).\
            filter(CategoryNameModel.name == category_name).all()
        res = []
        for i in query:
            res.append(i.description)
        return res

class CategoryNameModel(db.Model):
    '''map category id and category name'''
    __tablename__ = 'name_category'

    category_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(10))

    @staticmethod
    def get_all_categories():
        res = []
        query = CategoryNameModel.query.all()
        for i in query:
            res.append(i.name)
        return res

class UserModel(db.Model):
    '''user model'''
    __tablename__ = 'user'

    uid = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False) # unique user id
    account = db.Column(db.String(20), index = True) # user's login account
    password = db.Column(db.String(30)) # user's login password
    interest = db.Column(db.String(20)) # user's interests. 0 for indifferent, 1 for interested
    register_date = db.Column(db.DateTime, default = db.func.now()) # time of registration
    last_login = db.Column(db.DateTime) # last login time

class UserRelationshipModel():
    '''friends or blacklist of a user'''
    __tablename__ = 'relationship'

    rid = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False) # unique relationship id
    user1 = db.Column(db.Integer, index = True) # one of the related users
    user2 = db.Column(db.Integer, index = True) # one of the related users
    relationship = db.Column(db.SMALLINT) # relationship type
    status = db.Column(db.SMALLINT) # status of the relationship. 1 for user1->user2, -1 for user2->user1, 0 for user1<->user2
