from flask import Flask, jsonify

app = Flask(__name__)

# Dados fictícios (estes serão substituídos pelos usuários cadastrados no Tinder)
dados_ficticios = [
    {"nome": "Alice", "idade": 25, "sexo": "Feminino", "sexualidade": "H"},
    {"nome": "Bob", "idade": 30, "sexo": "Masculino", "sexualidade": "H"},
    {"nome": "Charlie", "idade": 22, "sexo": "Não-binário", "sexualidade": "B"},
    {"nome": "Dana", "idade": 28, "sexo": "Feminino", "sexualidade": "H"},
    {"nome": "Eli", "idade": 35, "sexo": "Masculino", "sexualidade": "H"}
]

@app.route('/dados', methods=['GET'])
def get_dados():
    return jsonify(dados_ficticios)

if __name__ == '__main__':
    app.run(debug=True)