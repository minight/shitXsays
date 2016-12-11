from flask import Blueprint

blueprint = Blueprint('user',
    __name__,
    template_folder='templates',
    static_folder='static')

import views
