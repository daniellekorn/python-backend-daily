from flask import Flask, request, jsonify, json, render_template, redirect, flash, url_for
from mini_project.classes.users import User
from mini_project.classes.instruments import Instrument
from mini_project.classes.registration import RegistrationForm, RegisterInstrument
from mini_project.classes.mockDatabase import users, instruments
from mini_project.modules.validators import validator

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template('index.html')


@app.route("/instruments", methods=['GET', 'POST'])
def get_or_add_instruments():
    if request.method == "POST":
        content = request.form
        new_instrument = Instrument(content.get('model'), content.get('type'))
        instruments[new_instrument.get('id_num')] = new_instrument
        response = {"new_instrument": new_instrument}
        return app.response_class(response=json.dumps(response), status=200, mimetype='application/json')
    return jsonify({'instruments': instruments})


@app.route("/instruments/<instrument_id>", methods=["GET",  "DELETE"])
def get_or_delete_instrument_by_id(instrument_id):
    if request.method == "DELETE":
        instruments.pop(instrument_id, None)
        return app.response_class(response=json.dumps({'deleted': instrument_id}), status=200,
                                  mimetype='application/json')
    return jsonify({'instrument': instruments[instrument_id]})


@app.route("/instrument/<instrument_id>/upload", methods=["POST"])
def upload_instrument_img():
    f = request.files[&#39;data&#39;]
    f.save(&#39;images/uploaded_file.jpg&#39;)
    response = app.response_class(
    response=json.dumps({&quot;status&quot;: &quot;ok&quot;}),
    status=200,
    mimetype=&#39;application/json&#39;
    )
    return response


@app.route("/instruments/user/<user_id>")
def get_all_instruments_for_user(user_id):
    return jsonify({'users_instruments': users[user_id]['instruments']})


@app.route("/users", methods=["GET", "POST"])
def get_or_add_users():
    if request.method == "POST":
        content = request.form
        new_user = User(content.get('name'), content.get('title'), {})
        users[new_user.get('user_id')] = new_user
        response = {"new_user": new_user}
        return app.response_class(response=json.dumps(response), status=200, mimetype='application/json')
    return jsonify({'users': users})


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        new_user = User(form.username.data, form.email.data, form.password.data, {})
        users[new_user.get('user_id')] = new_user
        flash('Thanks for registering')
        return redirect(url_for('user_add_instrument'))
    return render_template('register.html', form=form)


@app.route('/register/instrument', methods=['GET', 'POST'])
def user_add_instrument():
    form = RegisterInstrument(request.form)
    if request.method == 'POST' and form.validate():
        user_info = form.username.data
        new_instrument = Instrument(form.type.data, form.model.data)
        instruments[new_instrument.get('id_num')] = new_instrument
        for user in users:
            if users[user]['username'] == user_info:
                user_id = users[user]['user_id']
                assign_instrument_to_user(new_instrument.get('id_num'), user_id)
                return app.response_class(response=json.dumps({'updated profile': users[user_id]}), status=200,
                                          mimetype='application/json')
        return "Username invalid: only registered users can submit instruments"
    return render_template('instrument.html', form=form)


@app.route("/users/<user_id>", methods=["GET", "DELETE"])
def get_or_delete_user_by_id(user_id):
    if request.method == "DELETE":
        users.pop(user_id, None)
        return app.response_class(response=json.dumps({'deleted': user_id}), status=200, mimetype='application/json')
    return jsonify({'user': users[user_id]})


# add validation here
@app.route("/instrument/<instrument_id>/user/<user_id>", methods=['PUT'])
def assign_instrument_to_user(instrument_id, user_id):
    users[user_id]['instruments'][instrument_id] = instruments[instrument_id]
    response = {"updated_user": users[user_id]}
    return app.response_class(response=json.dumps(response), status=200, mimetype='application/json')


# add video to instrument validation here

if __name__ == "__main__":
    app.secret_key = b'testing'
    app.run()

