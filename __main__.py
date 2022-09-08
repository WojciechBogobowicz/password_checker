from flask import Flask, request
from validator import PasswordValidator
from rules_specification import *



def main():
    app = Flask(__name__)
    validator = PasswordValidator(specified_rules_impossible)


    @app.route('/get-strong-password', methods=['POST'])
    def index():
        data = request.data.decode()
        rules_that_dont_passed = validator.get_invalid_rule_names(data)
        if rules_that_dont_passed:
            return f"""Your password don't satissify folowing rules: {rules_that_dont_passed}.
            Maybe, you want use '{validator.get_fixed_password(data)}' as your password instead?"""
        return "Everything is okay with your password."


    app.run()


if __name__ == '__main__':
    main()
