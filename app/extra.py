from flask_sqlalchemy import SQLAlchemy
from flask import g, abort, request
from functools import wraps
from flask_restful import reqparse
import random
import os


db = SQLAlchemy()


class NotFoundError(Exception):
    def __init__(self, message):
        self.message = message

def rand_item(item_list, length):
    item_list = list(set(item_list))
    cat_len = len(item_list)
    random.shuffle(item_list)
    if cat_len == length:
        return item_list
    elif cat_len > length:
        return item_list[0:length]
    else:
        while len(item_list) < length:
            item_list.append(item_list[random.randint(0, cat_len - 1)])
        return item_list

def get_image_amount(category_name):
    prefix = 'app' + os.sep + 'static' + os.sep + 'bgimage' + os.sep + category_name
    return len(os.listdir(prefix))

def params(param_list, location="json", empty_check=True):

    def inner(func):
        if func.__name__ == "get":
            _location = "args"
        _location = location

        @wraps(func)
        def decorated(*args, **kwargs):
            parser = reqparse.RequestParser()
            try:
                for element in param_list:
                    parser.add_argument(
                        element[0], type=element[1],
                        required=element[2],
                        location=_location)
                _args = parser.parse_args()
                if empty_check:
                    for _element in param_list:
                        if _element[2] and not _args.get(_element[0]):
                            abort(400, "{0} can not be empty".format(
                                _element[0]))
                kwargs.update(_args)
            except reqparse.exceptions.BadRequest:
                abort(400)
            return func(*args, **kwargs)
        return decorated
    return inner


def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            abort(403, "log in first")
        _response = rds.cache.hgetall(token)
        if not _response:
            abort(403, "log in again")
        g.response_ = _response
        return func(*args, **kwargs)
    return inner