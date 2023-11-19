from flask import jsonify, render_template, request, redirect, url_for, flash
from flask_restful import reqparse, Resource
from flask_restful_swagger_3 import swagger, Resource
from models.imovel_model import ImovelModel
import sqlite3
import json

class Imoveis(Resource):
    def get(self):
        return {'imoveis': [imovel.json() for imovel in ImovelModel.query.all()]}, 200

class Imovel(Resource):      
    args = reqparse.RequestParser()
    args.add_argument('cidade_imovel', type=str, required=True, help="O campo 'cidade' deve ser preenchido.")
    args.add_argument('end_imovel', type=str, required=True, help="O campo 'endereço' deve ser preenchido.")
    args.add_argument('tipo_imovel', type=str, required=True, help="O campo 'tipo de imovel' deve ser preenchido.")
    args.add_argument('area_imovel', type=int, required=True, help="O campo 'área do imóvel' deve ser preenchido.")
    args.add_argument('quartos_imovel', type=int, required=True, help="O campo 'quartos' deve ser preenchido.")
    args.add_argument('banheiros_imovel', type=int, required=True, help="O campo 'banheiros' deve ser preenchido.")
    args.add_argument('garagem_imovel', type=int, required=True, help="O campo 'garagem' deve ser preenchido.")
    args.add_argument('valor_imovel', type=str, required=True, help="O campo 'valor' deve ser preenchido.")
    args.add_argument('descricao_imovel', type=str, required=True, help="O campo 'descrição' deve ser preenchido.")    
    
    def get(self, id_imovel):
        imovel = ImovelModel.localizar_imovel(id_imovel)
        if imovel:
            return imovel.json()   
        return {'message': 'Imovel não encontrado.'}, 404 #mensagem de erro
    
    def post(self, id_imovel):
        if ImovelModel.localizar_imovel(id_imovel):
            return {'message': 'imovel ja existe.'}
        valor_chave = Imovel.args.parse_args()
        imovel = ImovelModel(id_imovel, **valor_chave)
        try:
            imovel.save_imovel()
        except:
            return {'message': "Utilize outro ID e Realize o cadastro novamente"}    
        return imovel.json()
        return {'message': "Imóvel criado com sucesso"}, 201 #imovel criado
    
    def put(self, id_imovel):
        valor_chave = Imovel.args.parse_args()
        imovel_existe = ImovelModel.localizar_imovel(id_imovel)
        if imovel_existe:
            imovel_existe.update(**valor_chave)
            try:
                imovel_existe.save_imovel()
            except:
                return {'message': "Falha ao salvar. Realize o cadastro novamente"}
            return imovel_existe.json(), 200
        imovel = ImovelModel(id_imovel, **valor_chave)
        try:
            imovel.save_imovel()
        except:
            return {'message': "Falha ao salvar. Realize o cadastro novamente"}
        return imovel.json()
    
    def delete(self, id_imovel):      
        imovel = ImovelModel.localizar_imovel(id_imovel)
        if imovel:
            try:
                imovel.delete()
            except:
                return {'message': "Falha ao deletar. Realize a exclusão novamente"}
            return {'message': 'imovel removido.'}, 200 #requisição com sucesso 
        return {'message': 'imovel não localizado.'}, 404 #mensagem de erro