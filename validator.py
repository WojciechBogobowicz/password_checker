from rules_factory import RulesFactory


class PasswordValidator:
    factory = RulesFactory()

    def __init__(self, rules_dictionary) -> None:
        self.rules_dict = rules_dictionary
        self.rules = [self.factory.create_instance(rule_name, **kwargs) for rule_name, kwargs in self.rules_dict.items()]
            
    def get_fixed_password(self, passwd: str, max_tries: int=1000):
        safe_switch = self.__CountDown(max_tries)
        while not self._is_password_valid(passwd) and safe_switch.tick():
            for rule in self.rules:
                passwd = rule.fix_validation_issue_if_needed(passwd)
        return passwd

    def _is_password_valid(self, passwd):
        validation_flags = []
        for rule in self.rules:
            validation_flags.append(rule.is_validated(passwd))
        return all(validation_flags)
    
    def get_invalid_rule_names(self, passwd):
        return ', '.join(rule.__class__.__name__ for rule in self.rules if not rule.is_validated(passwd))


class __CountDown:
    def __init__(self, ticks: int) -> None:
        self._ticks = ticks
        self._assert_positive_ticks_num()

    def _assert_positive_ticks_num(self) -> None:
        if self._ticks <= 0:
            raise ValueError("ticks have to be positive number")

    def tick(self) -> bool:
        self._ticks = self._ticks - 1
        return self._ticks > 0
