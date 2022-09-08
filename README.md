# Password validator
The aim of this microservice is to provide its user with a password that is that meets validation requirements. Strong password can be acquired by using POST method.

## Applied validation rules
The requirements for this example are:
- max 3 identical characters in row
- at least one digit
- at least one special character
- at least one upper case letter
- minimum 20 characters long

## Service implementation
The rules listed above are saved in a form of dictionary (example below and in [here](rules_specification.py)):
```python
specified_rules = {
    'SeriesRule': {'acceptable_in_row': 3},
    'HaveDigitRule': {},
    'SpecialCharRule': {},
    'UpercaseRule': {},
    'CorrectLength': {"minimal_length": 20}
}
```
Since the rules are implemented using the simple factory pattern they can be created by calling method with rule class name as attribute - all the rules must be contained in [the same package folder](validation_rules) and appropriate imports must be added to [init file](validation_rules/__init__.py).

## REST method
Password checker is avaliable using POST method on URI:
```
http://localhost:5000/get-strong-password
```
Content of the request body is in plain text, as well as the response of it.

### Egzample curl request:
```
curl -d "data" -X POST http://localhost:5000/get-strong-password
```
It returns status code `200 OK` and the password corrected for validation rules (or if it has already met the validation requirements, password is returned unchanged).
