from flask_restful import Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint
from resources.imoveis1 import Imovel, Imoveis
from resources.user import UserReg, UserLog, User
from apiflask import APIFlask
from flask import jsonify
import json

app = APIFlask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api.add_resource(Imoveis, '/imoveis')
api.add_resource(Imovel, '/imoveis/<id_imovel>')
api.add_resource(User, '/user/<id_user>')
api.add_resource(UserReg, '/cadastro')
api.add_resource(UserLog, '/login')

SWAGGER_URL = '/swagger'
API_URL = 'http://127.0.0.1:5000/openapi2.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Api de aluguel de Imóveis"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/openapi2.json')
def swagger():
    with open('openapi2.json', 'r') as f:
        return jsonify(json.load(f))

if __name__ == '__main__':
    from sql_alchemy_ import banco
    banco.init_app(app)
    with app.app_context():
        banco.create_all()
    app.run(host='127.0.0.1', port=5000, debug=True)
