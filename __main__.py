from flask import Flask, request
from validator import PasswordValidator
from rules_specification import *



def main():
    app = Flask(__name__)
    validator = PasswordValidator(specified_rules)
    @app.route('/get-strong-password', methods=['POST'])
    def index():
        data = request.data.decode()
        return validator.get_fixed_password(data)

    app.run()


if __name__ == '__main__':
    main()
