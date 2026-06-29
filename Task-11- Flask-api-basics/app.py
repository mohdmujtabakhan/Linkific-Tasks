from flask import Flask, jsonify,request

app = Flask(__name__)

# Sample Data
items = [
    {"id": 1, "name": "Laptop"},
    {"id": 2, "name": "Mouse"},
    {"id": 3, "name": "Keyboard"}
]

# Home Route
@app.route("/")
def home():
    return "Hello, Flask!"

# GET All Items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

# GET with parameter - Return a specific item
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    for item in items:
        if item["id"] == item_id:
            return jsonify(item)

    return jsonify({"message": "Item not found"}), 404

# POST - Add a new item
@app.route("/items", methods=["POST"])
def add_item():
    new_item = request.get_json()

    items.append(new_item)

    return jsonify({
        "message": "Item added successfully",
        "item": new_item
    }), 201 
# PUT - Update an existing item
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    updated_data = request.get_json()

    for item in items:
        if item["id"] == item_id:
            item["name"] = updated_data["name"]

            return jsonify({
                "message": "Item updated successfully",
                "item": item
            })

    return jsonify({"message": "Item not found"}), 404

# DELETE - Remove an item
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    for item in items:
        if item["id"] == item_id:
            items.remove(item)

            return jsonify({
                "message": "Item deleted successfully"
            })

    return jsonify({"message": "Item not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)