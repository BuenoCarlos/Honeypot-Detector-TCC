
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={
    r"/analisar": {"origins": ["http://localhost:3000"]}
})

@app.route("/analisar", methods=["POST"])
def analisar():
    # Recebe o JSON enviado pelo honeypot
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({"erro": "JSON inválido"}), 400

    usuario = dados.get("username", "")
    senha = dados.get("password", "")

    if not isinstance(usuario, str) or not isinstance(senha, str):
        return jsonify({"erro": "Dados inválidos"}), 400

    print("Tentativa recebida!")
    print("Usuário:", usuario)
    print("Password:", senha)

    resultado = {
        "recebido": True,
        "classificacao": "pendente",
        "mensagem": "Entrada recebida para análise"
    }

    return jsonify(resultado), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
    