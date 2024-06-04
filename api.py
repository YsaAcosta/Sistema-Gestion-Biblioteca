from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://vicmag2413:Manuelag1$@cluster0.gvzqbpc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
mongo = PyMongo(app)

# Rutas para la colección 'books'

# Ruta para crear un libro
@app.route('/books', methods=['POST'])
def create_book():
    book_data = request.json
    title = book_data['title']
    author_id = book_data['author_id']
    genre_id = book_data['genre_id']

    # Insertar el libro en la colección 'books'
    book_id = mongo.db.books.insert_one({'title': title, 'author_id': author_id, 'genre_id': genre_id}).inserted_id

    return jsonify({'message': 'Libro creado exitosamente!', 'book_id': str(book_id)}), 201

# Ruta para obtener todos los libros
@app.route('/books', methods=['GET'])
def get_all_books():
    books = mongo.db.books.find()
    book_list = []
    for book in books:
        book['_id'] = str(book['_id'])
        book_list.append(book)
    return jsonify(book_list), 200

# Ruta para obtener un libro específico
@app.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    book = mongo.db.books.find_one({'_id': ObjectId(book_id)})
    if book:
        book['_id'] = str(book['_id'])
        return jsonify(book), 200
    else:
        return jsonify({'message': 'Libro no encontrado!'}), 404

# Ruta para actualizar un libro
@app.route('/books/<book_id>', methods=['PUT'])
def update_book(book_id):
    book_data = request.json
    title = book_data['title']
    author_id = book_data['author_id']
    genre_id = book_data['genre_id']

    # Actualizar el libro en la colección 'books'
    mongo.db.books.update_one({'_id': ObjectId(book_id)}, {'$set': {'title': title, 'author_id': author_id, 'genre_id': genre_id}})

    return jsonify({'message': 'Libro actualizado exitosamente!'}), 200

# Ruta para eliminar un libro
@app.route('/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    # Eliminar el libro de la colección 'books'
    mongo.db.books.delete_one({'_id': ObjectId(book_id)})

    return jsonify({'message': 'libro eliminado exitosamente!'}), 200


# Routes for genre collection

# Create a new genre
@app.route('/genres', methods=['POST'])
def create_genre():
    genre_data = request.json
    name = genre_data['name']

    # Insert the genre in the 'genres' collection
    genre_id = mongo.db.genres.insert_one({'name': name}).inserted_id

    return jsonify({'message': 'Genero creado exitosamente!', 'genre_id': str(genre_id)}), 201

# Get all genres
@app.route('/genres', methods=['GET'])
def get_all_genres():
    genres = mongo.db.genres.find()
    genre_list = []
    for genre in genres:
        genre['_id'] = str(genre['_id'])
        genre_list.append(genre)
    return jsonify(genre_list), 200

# Get a specific genre by ID
@app.route('/genres/<genre_id>', methods=['GET'])
def get_genre(genre_id):
    genre = mongo.db.genres.find_one_or_404({'_id': ObjectId(genre_id)})
    genre['_id'] = str(genre['_id'])
    return jsonify(genre), 200

# Update a genre by ID
@app.route('/genres/<genre_id>', methods=['PUT'])
def update_genre(genre_id):
    genre_data = request.json
    name = genre_data['name']

    # Update the genre in the 'genres' collection
    mongo.db.genres.update_one({'_id': ObjectId(genre_id)}, {'$set': {'name': name}})

    return jsonify({'message': 'Genero actualizado exitosamente!'}), 200

# Delete a genre by ID
@app.route('/genres/<genre_id>', methods=['DELETE'])
def delete_genre(genre_id):
    # Delete the genre from the 'genres' collection
    mongo.db.genres.delete_one({'_id': ObjectId(genre_id)})

    return jsonify({'message': 'Genero eliminado exitosamente!'}), 200

# Routes for author collection

# Create a new author
@app.route('/authors', methods=['POST'])
def create_author():
    author_data = request.json
    name = author_data['name']

    # Insert the author in the 'authors' collection
    author_id = mongo.db.authors.insert_one({'name': name}).inserted_id

    return jsonify({'message': 'Autor creado exitosamente!', 'author_id': str(author_id)}), 201

# Get all authors
@app.route('/authors', methods=['GET'])
def get_all_authors():
    authors = mongo.db.authors.find()
    author_list = []
    for author in authors:
        author['_id'] = str(author['_id'])
        author_list.append(author)
    return jsonify(author_list), 200

# Get a specific author by ID
@app.route('/authors/<author_id>', methods=['GET'])
def get_author(author_id):
    author = mongo.db.authors.find_one_or_404({'_id': ObjectId(author_id)})
    author['_id'] = str(author['_id'])
    return jsonify(author), 200

# Update an author by ID
@app.route('/authors/<author_id>', methods=['PUT'])
def update_author(author_id):
    author_data = request.json
    name = author_data['name']

    # Update the author in the 'authors' collection
    mongo.db.authors.update_one({'_id': ObjectId(author_id)}, {'$set': {'name': name}})

    return jsonify({'message': 'Autor actualizado exitosamente!'}), 200

# Delete an author by ID
@app.route('/authors/<author_id>', methods=['DELETE'])
def delete_author(author_id):
    # Delete the author from the 'authors' collection
    mongo.db.authors.delete_one({'_id': ObjectId(author_id)})

    return jsonify({'message': 'Autor eliminado exitosamente!'}), 200

if __name__ == '__main__':
    app.run(debug=True)