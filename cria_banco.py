import sqlite3
import json
connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS imoveis (id_imovel integer NOT NULL PRIMARY KEY,\
    cidade_imovel text, end_imovel text, tipo_imovel text, area_imovel float,\
        quartos_imovel integer, banheiros_imovel integer, garagem_imovel integer, valor_imovel float,\
            descricao_imovel text)"

create_imovel = "INSERT OR REPLACE INTO imoveis VALUES ('2', 'São Paulo', 'Avenida Alváres DE Azevedo, 1000',\
    'Apartamento', '70', 2, 3, '1', 2.500,\
        'Apartamento localizado na Avenida Álvares Penteado, 330,\
            com dois quartos, sala, cozinha, dois banheiros, garagem para um atuomóvel, valor: R$ 2.500,00')"

cursor.execute(create_table)
cursor.execute(create_imovel)

connection.commit()
connection.close()