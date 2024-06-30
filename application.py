from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class book(db.books):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"

@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():
    books = book.query.all()

    output = []
    for book in books:
        book_data = {'Book Name': book.name, 'Author': book.author, 'Publisher': book.publisher}

        output.append(book_data)
    return {"books": output}

@app.route('/books/<id>')
def get_book(id):
    Book = book.query.get_or_404(id)
    return {'Book Name': book.name, 'Author': book.author, 'Publisher': book.publisher}

@app.route('/books', methods=['POST'])
def add_book():
    Book = book(book_name=request.json['book name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(Book)
    db.session.commit()
    return {'id': Book.id}