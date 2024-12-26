from flask import Flask, jsonify, request

app = Flask(__name__)

persons = {}
next_id = 1

@app.route('/api/v1/persons', methods=['GET'])
def list_persons():
    return jsonify(list(persons.values())), 200

@app.route('/api/v1/persons', methods=['POST'])
def create_person():
    global next_id
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'message': 'Invalid data'}), 400
    person = {
        'id': next_id,
        'name': data['name'],
        'age': data.get('age'),
        'address': data.get('address'),
        'work': data.get('work')
    }
    persons[next_id] = person
    next_id += 1
    return '', 201, {'Location': f'/api/v1/persons/{person["id"]}'}

@app.route('/api/v1/persons/<int:id>', methods=['GET'])
def get_person(id):
    person = persons.get(id)
    if person is None:
        return jsonify({'message': 'Not found'}), 404
    return jsonify(person), 200

@app.route('/api/v1/persons/<int:id>', methods=['DELETE'])
def delete_person(id):
    if id in persons:
        del persons[id]
        return '', 204
    return jsonify({'message': 'Not found'}), 404

@app.route('/api/v1/persons/<int:id>', methods=['PATCH'])
def update_person(id):
    person = persons.get(id)
    if person is None:
        return jsonify({'message': 'Not found'}), 404
    data = request.get_json()
    if 'name' in data:
        person['name'] = data['name']
    if 'age' in data:
        person['age'] = data['age']
    if 'address' in data:
        person['address'] = data['address']
    if 'work' in data:
        person['work'] = data['work']
    return jsonify(person), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
