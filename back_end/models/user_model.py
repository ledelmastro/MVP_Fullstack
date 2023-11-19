from sql_alchemy_ import banco
import json

class UserModel(banco.Model):
    __tablename__ = 'usuarios'
    id_user = banco.Column(banco.Integer, primary_key=True)
    login = banco.Column(banco.String(40))
    password = banco.Column(banco.String(40))
    
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def json(self):
        return {
            'id_user': self.id_user,
            'login': self.login
        }
        
    @classmethod
    def localizar_user(cls, id_user):
        user = cls.query.filter_by(id_user=id_user).first()
        if user:
            return user
        return None
    
    @classmethod
    def localizar_login(cls, login):
        user = cls.query.filter_by(login=login).first()
        if user:
            return user
        return None
    
    def save_user(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete (self):
        banco.session.delete(self)
        banco.session.commit()

