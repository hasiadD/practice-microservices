import os
import requests
from flask import Flask, request, Response

app = Flask(__name__)
PRODUCT = os.getenv("PRODUCT_URL", "http://product-service:5000")
ORDER = os.getenv("ORDER_URL", "http://order-service:5000")

def proxy(base, path):
    r = requests.request(request.method, f"{base}/{path}",
                         json=request.get_json(silent=True), timeout=5)
    resp = Response(r.content, r.status_code, content_type=r.headers.get("Content-Type"))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp

@app.route("/products", defaults={"p": ""}, methods=["GET"])
@app.route("/products/<path:p>", methods=["GET"])
def products(p):
    return proxy(PRODUCT, "products/" + p if p else "products")

@app.route("/orders", methods=["GET", "POST"])
def orders():
    return proxy(ORDER, "orders")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
