from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1, 
        'titulo': 'Biblia Sagrada',
        'autor': 'Deus'
    },
    {
        'id': 2, 
        'titulo': 'O senhor dos Aneis',
        'autor': 'J.R.R. Tolkien'
    },
    {
        'id': 3, 
        'titulo': 'Kubernetes',
        'autor': 'novatec'
    },
] 

# consultar (todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)
# consultar por id
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
# Editar`
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livros_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
# Criar            
@app.route('/livros',methods=['POST'])
def incluir_livros():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)
# excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
        return jsonify(livros)
app.run(port=5000,host='localhost',debug=True)    