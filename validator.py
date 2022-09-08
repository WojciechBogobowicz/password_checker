from rules_factory import RulesFactory


class PasswordValidator:
    factory = RulesFactory()

    def __init__(self, rules_dictionary) -> None:
        self.rules_dict = rules_dictionary
        self.rules = [self.factory.create_instance(rule_name, **kwargs) for rule_name, kwargs in self.rules_dict.items()]
            
    def get_fixed_password(self, passwd):
        current_try = 0
        while not self._is_password_valid(passwd):
            for rule in self.rules:
                passwd = rule.fix_validation_issue_if_needed(passwd)
        return passwd

    def _is_password_valid(self, passwd):
        validation_flags = []
        for rule in self.rules:
            validation_flags.append(rule.is_validated(passwd))
        return all(validation_flags)
    
    def get_invalid_rule_names(self, passwd):
        acc = []
        for rule in self.rules:
            if not rule.is_validated(passwd):
                acc.append(rule.__class__.__name__)
        return ", ".join(acc)

    # class 