from flask import Flask,jsonify,request
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# PostgreSQL Database Connection
conn = psycopg2.connect(
    host="localhost",
    database="books_db",
    user="postgres",
    password="240629",
    port="5432"
)

cursor = conn.cursor()

@app.route("/")
def home():
    return "Flask is connected to PostgreSQL successfully!"

@app.route("/books", methods=["GET"])
def get_books():
    cursor.execute("SELECT * FROM books;")
    books = cursor.fetchall()

    result = []

    for book in books:
        result.append({
            "id": book[0],
            "title": book[1],
            "author": book[2],
            "price": float(book[3])
        })

    return jsonify(result)

@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()

    title = data["title"]
    author = data["author"]
    price = data["price"]

    cursor.execute(
        "INSERT INTO books (title, author, price) VALUES (%s, %s, %s) RETURNING id;",
        (title, author, price)
    )

    book_id = cursor.fetchone()[0]
    conn.commit()

    return jsonify({
        "message": "Book added successfully",
        "id": book_id,
        "title": title,
        "author": author,
        "price": price
    }), 201

@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    data = request.get_json()

    title = data["title"]
    author = data["author"]
    price = data["price"]

    cursor.execute(
        """
        UPDATE books
        SET title = %s, author = %s, price = %s
        WHERE id = %s
        """,
        (title, author, price, id)
    )

    conn.commit()

    if cursor.rowcount == 0:
        return jsonify({"message": "Book not found"}), 404

    return jsonify({
        "message": "Book updated successfully"
    })

@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):

    cursor.execute("DELETE FROM books WHERE id = %s;", (id,))
    conn.commit()

    if cursor.rowcount == 0:
        return jsonify({"message": "Book not found"}), 404

    return jsonify({
        "message": "Book deleted successfully"
    })

if __name__ == "__main__":
    app.run(debug=True)