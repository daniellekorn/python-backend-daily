from flask import Flask, request, jsonify, json
from monday.classes.users import User
from monday.classes.instruments import Instrument

app = Flask(__name__)

users = {}
instruments = {}


@app.route("/instruments")
def get_all_instruments():
    return jsonify({'instruments': instruments})


@app.route("/users")
def get_all_users():
    print(users)
    return jsonify({'users': users})


@app.route("/instruments", methods=['POST'])
def add_instrument():
    content = request.form
    new_instrument = Instrument(content.get('name'), content.get('model'), content.get('type'))
    instruments[new_instrument.get('id_num')] = new_instrument
    response = {"new_instrument": new_instrument}
    return app.response_class(response=json.dumps(response), status=200, mimetype='application/json')


@app.route("/users", methods=['POST'])
def add_user():
    content = request.form
    new_user = User(content.get('name'), content.get('title'), {})
    users[new_user.get('user_id')] = new_user
    response = {"new_user": new_user}
    return app.response_class(response=json.dumps(response), status=200, mimetype='application/json')


@app.route("/instrument/<instrument_id>/user/<user_id>", methods=['PUT'])
def assign_instrument_to_user(instrument_id, user_id):
    users[user_id]['instruments'][instrument_id] = instruments[instrument_id]
    response = {"updated_user": users[user_id]}
    return app.response_class(response=json.dumps(response), status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run()

