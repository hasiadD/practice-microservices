from flask import Flask, jsonify

app = Flask(__name__)
app.json.ensure_ascii = False
PRODUCTS = [
    {"id": 1, "name": "Ноутбук", "price": 32000},
    {"id": 2, "name": "Мишка", "price": 600},
    {"id": 3, "name": "Клавіатура", "price": 1500},
]

@app.get("/products")
def list_products():
    return jsonify(PRODUCTS)

@app.get("/products/<int:pid>")
def get_product(pid):
    for p in PRODUCTS:
        if p["id"] == pid:
            return jsonify(p)
    return jsonify({"error": "not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(__import__("os").getenv("PORT", 5000)))
