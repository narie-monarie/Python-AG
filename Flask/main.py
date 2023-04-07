from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'


def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db


@app.route('/users', methods=['GET'])
def get_users():
    db = get_db()
    users = db.execute('SELECT * FROM users').fetchall()
    db.close()
    return jsonify([dict(row) for row in users])


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    db = get_db()
    db.execute('INSERT INTO users (name, email) VALUES (?, ?)',
               (data['name'], data['email']))
    db.commit()
    db.close()
    return jsonify({'message': 'User created successfully'})


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    db = get_db()
    db.execute('UPDATE users SET name=?, email=? WHERE id=?',
               (data['name'], data['email'], user_id))
    db.commit()
    db.close()
    return jsonify({'message': 'User updated successfully'})


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    db = get_db()
    db.execute('DELETE FROM users WHERE id=?', (user_id,))
    db.commit()
    db.close()
    return jsonify({'message': 'User deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
