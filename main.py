import psycopg2
from flask import Flask, make_response, jsonify, request

#region Conexão com o BD
#Configurações BD
host = 'localhost'
dbname = 'postgres'
user = 'postgres'
password = 'passwordPostgres'
#endregion

#String de conexão
conn_string = 'host={0} user={1} dbname={2} password={3}'.format(host,user,dbname,password)

#def buscar_uma_categoria(id):
#    cursor.execute('SELECT * FROM public."Categoria" WHERE id=%s ;',(id,))
#    return cursor.fetchall()

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#region Endpoints de Categoria 
@app.route('/categoria', methods=['GET']) 
def get_categorias():
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()        
    cursor.execute('SELECT * FROM public."Categoria";')
    Categorias = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return make_response(
        jsonify(
        message = 'Lista de categorias.',
        data = Categorias
        )
    ) 

@app.route('/categoria', methods=['POST'])
def create_categoria():
    categoria = request.json
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()        
    cursor.execute('INSERT INTO public."Categoria" ("Nome", "Descricao") VALUES(%s, %s);', (categoria['Nome'], categoria['Descricao'],))    
    conn.commit()
    cursor.close()
    conn.close()
    return make_response(
        jsonify(
        message='Categoria cadastrada com sucesso.',
        categoria=categoria
        )
    )

@app.route('/categoria/<id>', methods=['DELETE'])
def excluir_categoria(id):
   
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()        
    cursor.execute('DELETE FROM public."Categoria" WHERE id=%s;',(id,))
    conn.commit()
    cursor.close()
    conn.close()
    return make_response(
        jsonify(
        message='Categoria excluida com sucesso.',
        )
    )

@app.route('/categoria', methods=['PUT'])
def update_categoria():
    categoria = request.json
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()        
    cursor.execute('UPDATE public."Categoria" SET "Nome"=%s, "Descricao"=%s WHERE id=%s;',(categoria['Nome'], categoria['Descricao'], categoria['id'],) )
    conn.commit()
    cursor.close()
    conn.close()
    return make_response(
        jsonify(
        message='Categoria alterada com sucesso.',
        categoria=categoria
        )
    )
#endregion


#region Endpoints de Produto
@app.route('/produto', methods=['GET']) 
def get_produtos():
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()        
    cursor.execute('SELECT * FROM public."Produto";')
    Produtos = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return make_response(
        jsonify(
        message = 'Lista de produtos.',
        data = Produtos
        )
    ) 

@app.route('/produto', methods=['POST'])
def create_produto():
    produto = request.json
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()        
    cursor.execute('INSERT INTO public."Produto" ("Nome", "Descricao", "Preco", "Categoria") VALUES(%s, %s, %s, %s);', (produto['Nome'], produto['Descricao'], produto['Preco'], produto['Categoria'],))    
    conn.commit()
    cursor.close()
    conn.close()
    return make_response(
        jsonify(
        message='Produto cadastrado com sucesso.',
        produto=produto
        )
    )

@app.route('/produto/<id>', methods=['DELETE'])
def excluir_produto(id):
   
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()        
    cursor.execute('DELETE FROM public."Produto" WHERE id=%s;',(id,))
    conn.commit()
    cursor.close()
    conn.close()
    return make_response(
        jsonify(
        message='Produto excluido com sucesso.',
        )
    )

@app.route('/produto', methods=['PUT'])
def update_produto():
    produto = request.json
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()        
    cursor.execute('UPDATE public."Produto" SET "Nome"=%s, "Descricao"=%s, "Preco"=%s, "Categoria"=%s WHERE id=%s;',(produto['Nome'], produto['Descricao'], produto['Preco'], produto['Categoria'], produto['id'],) )
    conn.commit()
    cursor.close()
    conn.close()
    return make_response(
        jsonify(
        message='Produto alterado com sucesso.',
        produto=produto
        )
    )
#endregion

app.run()
