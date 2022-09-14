from flask import Flask, request

from validator import PasswordValidator
import rules_specification


def main() -> None:
    app = Flask(__name__)
    validator = PasswordValidator(rules_dictionary=rules_specification.task)

    @app.route("/get-strong-password", methods=["POST"])
    def index():
        data = request.data.decode()
        return get_respond(data)

    def get_respond(data: str) -> str:
        rules_that_dont_passed = validator.get_invalid_rule_names(data)
        try:
            fixed_password = validator.get_fixed_password(data)
        except RuntimeError:
            return "Cannot process your request", 508

        if rules_that_dont_passed:
            return f"""Your password don't satissify folowing rules: {rules_that_dont_passed}.
            Maybe, you want use '{fixed_password}' as your password instead?"""
        return "Everything is okay with your password."

    app.run()


if __name__ == "__main__":
    main()
