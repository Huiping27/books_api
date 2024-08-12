from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "published_year": 1949},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "published_year": 1960},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Add other routes here...

if __name__ == '__main__':
    app.run(port=5001)

