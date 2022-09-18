from inspect import getmembers, isclass, isabstract
import warnings

import validation_rules


class RulesFactory:
    rules = dict()

    def __init__(self) -> None:
        self.load_rules()

    def load_rules(self) -> None:
        classes = getmembers(
            validation_rules, lambda m: isclass(m) and not isabstract(m)
        )
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, validation_rules.AbsValidationRule):
                self.rules[name] = _type

    def create_instance(self, rule_name: str, **kwargs):
        if rule_name not in self.rules:
            self._create_null_rule(rule_name)
        return self.rules[rule_name](**kwargs)

    @staticmethod
    def _create_null_rule(rule_name: str) -> validation_rules.NullRule:
        warnings.warn(f"{rule_name} not found. NullRule created instead.")
        return validation_rules.NullRule(rule_name)

    def get_avaliabe_rules_list(self) -> list[str]:
        return list(self.rules.keys())
