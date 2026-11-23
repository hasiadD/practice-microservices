import os
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)
app.json.ensure_ascii = False
PRODUCT_URL = os.getenv("PRODUCT_URL", "http://product-service:5000")
ORDERS = []

@app.post("/orders")
def create_order():
    pid = (request.get_json(silent=True) or {}).get("product_id")
    if pid is None:
        return jsonify({"error": "product_id required"}), 400
    r = requests.get(f"{PRODUCT_URL}/products/{pid}", timeout=3)
    if r.status_code != 200:
        return jsonify({"error": "product not found"}), 404
    order = {"id": len(ORDERS) + 1, "product": r.json()}
    ORDERS.append(order)
    return jsonify(order), 201

@app.get("/orders")
def list_orders():
    return jsonify(ORDERS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
