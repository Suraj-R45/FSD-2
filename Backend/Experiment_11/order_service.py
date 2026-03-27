from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# In-memory order data
orders = [
    {
        "id": 1,
        "user_id": 101,
        "order_date": "2026-02-20",
        "order_amount": 2500,
        "order_status": "Shipped",
        "items": [
            {"name": "Laptop", "quantity": 1, "price": 2000},
            {"name": "Mouse", "quantity": 2, "price": 250}
        ]
    },
    {
        "id": 2,
        "user_id": 101,
        "order_date": "2026-02-22",
        "order_amount": 1200,
        "order_status": "Processing",
        "items": [
            {"name": "Keyboard", "quantity": 1, "price": 1200}
        ]
    },
    {
        "id": 3,
        "user_id": 102,
        "order_date": "2026-02-18",
        "order_amount": 800,
        "order_status": "Delivered",
        "items": [
            {"name": "Headphones", "quantity": 1, "price": 800}
        ]
    }
]

# 🔹 Home Route
@app.route("/")
def home():
    return jsonify({"service": "Order Service Running"})


# 🔹 Get Orders by User
@app.route("/orders/user/<int:user_id>", methods=["GET"])
def get_orders_by_user(user_id):
    user_orders = [o for o in orders if o["user_id"] == user_id]

    if not user_orders:
        return jsonify({"message": "No orders found"}), 404

    return jsonify(user_orders)


# 🔹 Update Order Status
@app.route("/orders/<int:order_id>/status", methods=["PUT"])
def update_order_status(order_id):
    data = request.get_json()

    # Validate JSON body
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    new_status = data.get("order_status")

    if not new_status:
        return jsonify({"error": "order_status is required"}), 400

    # Find and update order
    for order in orders:
        if order["id"] == order_id:
            order["order_status"] = new_status
            return jsonify({
                "message": "Order status updated successfully",
                "order": order
            })

    return jsonify({"error": "Order not found"}), 404


# 🔹 Run Server (IMPORTANT for deployment)
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )