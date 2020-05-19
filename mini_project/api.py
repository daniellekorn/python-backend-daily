from flask import Flask, request, jsonify, json, render_template, redirect, flash, url_for, send_file
from werkzeug.utils import secure_filename
from time import perf_counter
from mini_project.classes.users import User
from mini_project.classes.instruments import Instrument
from mini_project.classes.registration import RegistrationForm, RegisterInstrument
from mini_project.classes.mockDatabase import Users, Instruments
from mini_project.modules.validators import Validator
import os.path
import io

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template('index.html')


@app.route("/users", methods=["GET", "POST"])
def get_or_add_users():
    if request.method == "POST":
        content = request.form
        new_user = User(content.get('username'), content.get('email'), content.get('password'), [])
        Users.add_item(new_user)
    return jsonify({'users': Users.data})


@app.route("/instruments", methods=['GET', 'POST'])
def get_or_add_instruments():
    if request.method == "POST":
        content = request.form
        new_instrument = Instrument(content.get('type'), content.get('model'), [])
        Instruments.add_item(new_instrument)
    return jsonify({'instruments': Instruments.data})


@app.route('/register', methods=['GET', 'POST'])
def register_user():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        new_user = User(form.username.data, form.email.data, form.password.data, [])
        Users.add_item(new_user)
        flash('Thanks for registering')
        return redirect(url_for('register_instrument'))
    return render_template('register.html', form=form)


@app.route('/register/instrument', methods=['GET', 'POST'])
def register_instrument():
    form = RegisterInstrument(request.form)
    if request.method == 'POST' and form.validate():
        user_name = form.username.data
        new_instrument = Instrument(form.type.data, form.model.data, [])
        Instruments.add_item(new_instrument)
        user_id = Validator.get_user_id_by_name(user_name)
        if user_id:
            assign_instrument_to_user(new_instrument.get('id_num'), user_id)
            return app.response_class(response=json.dumps({'updated profile': Users.data[user_id]}), status=200,
                                      mimetype='application/json')
        return "Username invalid: only registered users can submit instruments"
    return render_template('instrument.html', form=form)


@app.route("/instruments/<instrument_id>", methods=["GET",  "DELETE"])
def get_or_delete_instrument_by_id(instrument_id):
    if request.method == "DELETE":
        Instruments.delete_item(instrument_id)
        response = {'deleted': instrument_id}
        return app.response_class(response=json.dumps(response), status=200, mimetype='application/json')
    return jsonify({'instrument': Instruments.data.get(instrument_id)})


@app.route("/users/<user_id>", methods=["GET", "DELETE"])
def get_or_delete_user_by_id(user_id):
    if request.method == "DELETE":
        Users.delete_item(user_id)
        return app.response_class(response=json.dumps({'deleted': user_id}), status=200, mimetype='application/json')
    return jsonify({'user': Users.data.get(user_id)})


@app.route("/instruments/<instrument_id>/image", methods=["PUT"])
def upload_instrument_img(instrument_id):
    f = request.files['image']
    filename = secure_filename(f.filename)
    f.save('media/instrument_images/' + filename)
    if Validator.instrument_exists(instrument_id):
        instrument_images = Instruments.data.get(instrument_id)['images']
        if len(instrument_images) > 1:
            response_info = {"Failure": f"Instrument with ID '{instrument_id}' already has max number of images (2)."}
        else:
            Instruments.append_new_item(instrument_id, 'images', filename)
            response_info = {"successfully uploaded file": filename}
    else:
        response_info = {"Failure": f"Instrument with ID '{instrument_id}' does not exist."}
    response = app.response_class(response=json.dumps(response_info), status=200, mimetype="application/json")
    return response


@app.route("/instruments/<instrument_id>/image/<img_num>")
def get_instrument_image(instrument_id, img_num):
    # user can input image 1 or 2 to get the first or second image, which I change into an int and -1 for index loc
    img_num = int(img_num - 1)
    if img_num > 1:
        response = {'Bad request': 'Image search number too large'}
        return app.response_class(response=json.dumps(response), status=404, mimetype="application/json")
    try:
        image_name = Instruments.data.get(instrument_id)['images'][img_num]
        with open(os.path.join('media/instrument_images/', image_name), "rb") as bites:
            print("here")
            return send_file(io.BytesIO(bites.read()), attachment_filename=image_name, mimetype='image/jpg')
    except Exception as e:
        response = {f"'Error': {e}"}
        return app.response_class(response=json.dumps(response), status=404, mimetype="application/json")


@app.route("/instruments/user/<user_id>", methods=["GET"])
def get_all_instruments_for_user(user_id):
    return jsonify({'users_instruments': Users.data.get(user_id)['instruments']})


@app.route("/instruments/user/<user_id>/<instrument_id>", methods=["PUT"])
def delete_instrument_for_user(user_id, instrument_id):
    Users.delete_sub_item(user_id, 'instruments', instrument_id)
    return jsonify({'users_instruments': Users.data.get(user_id)['instruments']})


@app.route("/instruments/<instrument_id>/users/<user_id>", methods=['PUT'])
def assign_instrument_to_user(instrument_id, user_id):
    Users.append_new_item(user_id, 'instruments', instrument_id)
    response = {"updated_user": Users.data.get(user_id)}
    return app.response_class(response=json.dumps(response), status=200, mimetype='application/json')


@app.route("/instruments/search")
def search_for_instrument():
    results = []
    start_time = perf_counter()
    search_query = request.args.get('search')
    for item in Instruments.data:
        instrument = Instruments.data[item]
        if instrument.get('type').lower() == search_query.lower():
            results.append(instrument)
    end_time = perf_counter()
    search_time = end_time - start_time
    return jsonify({'Search results': results, 'Total duration of search': search_time})


if __name__ == "__main__":
    app.secret_key = b'testing'
    app.run()

