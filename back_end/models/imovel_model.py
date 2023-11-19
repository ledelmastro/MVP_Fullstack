from sql_alchemy_ import banco
import json

class ImovelModel(banco.Model):
    __tablename__ = 'imoveis'
    id_imovel = banco.Column(banco.String(10000000), primary_key=True)
    cidade_imovel = banco.Column(banco.String(30))
    end_imovel = banco.Column(banco.String(50))
    tipo_imovel = banco.Column(banco.String(20))
    area_imovel = banco.Column(banco.Integer)
    quartos_imovel = banco.Column(banco.Integer)
    banheiros_imovel = banco.Column(banco.Integer)
    garagem_imovel = banco.Column(banco.Integer)
    valor_imovel = banco.Column(banco.String(30))
    descricao_imovel = banco.Column(banco.String(30))

    def __init__(self, id_imovel, cidade_imovel, end_imovel, tipo_imovel, area_imovel, quartos_imovel, banheiros_imovel, garagem_imovel, valor_imovel, descricao_imovel):
        self.id_imovel = id_imovel
        self.cidade_imovel = cidade_imovel
        self.end_imovel = end_imovel
        self.tipo_imovel = tipo_imovel
        self.area_imovel = area_imovel
        self.quartos_imovel = quartos_imovel
        self.banheiros_imovel = banheiros_imovel
        self.garagem_imovel = garagem_imovel
        self.valor_imovel = valor_imovel
        self.descricao_imovel = descricao_imovel 
        
    def json(self):
        return {
            'id_imovel': self.id_imovel,
            'cidade_imovel': self.cidade_imovel,
            'end_imovel': self.end_imovel,
            'tipo_imovel': self.tipo_imovel,
            'area_imovel': self.area_imovel + " metros quadrados.",
            'quartos_imovel': self.quartos_imovel + " quartos.",
            'banheiros_imovel': self.banheiros_imovel + " banheiros.",
            'garagem_imovel': self.garagem_imovel + " vagas de garagem.",
            'valor_imovel': self.valor_imovel + " Reais.",
            'descricao_imovel': self.descricao_imovel
        }
        
    @classmethod
    def localizar_imovel(cls, id_imovel):
        imovel = cls.query.filter_by(id_imovel=id_imovel).first()
        if imovel:
            return imovel
        return None
    
    def save_imovel(self):
        banco.session.add(self)
        banco.session.commit()
    
    def update (self, cidade_imovel, end_imovel, tipo_imovel, area_imovel, quartos_imovel, banheiros_imovel, garagem_imovel, valor_imovel, descricao_imovel):
        self.cidade_imovel = cidade_imovel
        self.end_imovel = end_imovel
        self.tipo_imovel = tipo_imovel
        self.area_imovel = area_imovel
        self.quartos_imovel = quartos_imovel
        self.banheiros_imovel = banheiros_imovel
        self.garagem_imovel = garagem_imovel
        self.valor_imovel = valor_imovel
        self.descricao_imovel = descricao_imovel
    
    def delete (self):
        banco.session.delete(self)
        banco.session.commit()
    
    

