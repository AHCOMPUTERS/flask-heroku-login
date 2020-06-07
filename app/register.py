@application.route('/register', methods=["GET", "POST"])
def register():
    username = request.args.get('username')
    email = request.args.get('email')
    password = request.args.get('password')
    password_hash = generate_password_hash(password)
    account = Table('account', metadata, autoload=True)
    engine.execute(account.insert(), username=username,
                   email=email, password=password_hash)
    return jsonify({'user_added': True})