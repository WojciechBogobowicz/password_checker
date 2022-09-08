# Password validator
The aim of this microservice is to provide its user with a password that is that meets validation requirements. Strong password can be acquired by using POST method.

## Applied validation rules
The requirements for this example are:
- max 3 identical characters in row
- at least one digit
- at least one special character
- at least one upper case letter
- minimum 20 characters long

## Service Usage
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
Since the rules are implemented using the simple factory pattern they can be created by calling method with rule class name as attribute - all the rules must be contained in [the same package folder](validation_rules), inherit from [AbsValidationRule](validation_rules/rule_abs.py) and appropriate imports must be added to [init file](validation_rules/__init__.py).  
If you want change default rules set you should modify parameter rules_dictionary of `ParseValidator` in [main](__main__.py#9).

## Fixing invalid password
It is two steps process, whose implementation can be found [here](validator.py).  
- Program checks if password is valid for all loaded rules. If yes, process ends.
- All rules are correcting passwords to satisfy theirs requirements, if password doesn't satisfy the rule.  
Those steps are repeating until all rules are validated.  
 
 ### Potencial conflicts
 Since rules don't know anything about each other, it is possible to define a rule set that can't be satisfied. For example, specified_rules_impossible from file [rules_specification](rules_specification.py).  
 In those cases, infinite loop risk occurs. That's why fixing password method has a safe switch implemented to break the loop, if it has exceeded maximum tries number (by default it is 1000). In those situations, the server sends a response with `508 code` (infinite loop occurred), and does not provide password suggestions.

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
