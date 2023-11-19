from flask_restful import Resource, reqparse
from models.user_model import UserModel
from werkzeug.security import hmac
import json

args = reqparse.RequestParser() 
args.add_argument('login', type=str, required=True, help="O campo 'Login' deve ser preenchido.")
args.add_argument('password', type=str, required=True, help="O campo 'password' deve ser preenchido.")

class User(Resource):
    def get(self, id_user):
        user = UserModel.localizar_user(id_user)
        if user:
            return user.json()   
        return {'message': 'Usuário não encontrado.'}, 404 #mensagem de erro

    def delete(self, id_user):      
        user = UserModel.localizar_user(id_user)
        if user:
            try:
                user.delete()
            except:
                return {'message': "Falha ao deletar. Realize a exclusão novamente"}
            return {'message': 'usuário removido.'}, 200 #requisição com sucesso 
        return {'message': 'usuário não localizado.'}, 404 #mensagem de erro

class UserReg(Resource):
    def post(self):
        valor_chave = args.parse_args()
                
        if UserModel.localizar_login(valor_chave['login']):
            return {"message": "O login '{}' já existe".format(valor_chave['login'])}
        
        user = UserModel(**valor_chave)       
        try:
            user.save_user()
        except:
            return {'message': "Falha ao salvar. Realize o cadastro novamente"}    
        return {'message': "Usuário '{}' criado com sucesso".format(valor_chave['login'])}, 201 #usuário criado

class UserLog(Resource):
    @classmethod
    def post(cls):
        valor_chave = args.parse_args()
        user = UserModel.localizar_login(valor_chave['login'])
        str_to_bytes = lambda s: s.encode("utf-8") if isinstance(s, str) else s
        safe_str_cmp = lambda a, b: hmac.compare_digest(str_to_bytes(a), str_to_bytes(b))
    
        if user and safe_str_cmp(user.password, valor_chave['password']):
            return {'message': "Login realizado com sucesso."}, 200 #Authorized
        return {'message': "Login ou senha incorretos."}, 401 #Unauthorized
            