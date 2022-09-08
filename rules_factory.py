from inspect import getmembers, isclass, isabstract
import warnings
import validation_rules



class RulesFactory():
    rules = dict()
    
    def __init__(self) -> None:
        self.load_rules()
        
    def load_rules(self) -> None:
        classes = getmembers(validation_rules, lambda m: isclass(m) and not isabstract(m))
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, validation_rules.AbsValidationRule):
                self.rules[name] = _type

    def create_instance(self, rule_name, **kwargs):
        if rule_name in self.rules:
            return self.rules[rule_name](**kwargs)
        else:
            warnings.warn(f"{rule_name} not found. NullRule created instead.")
            return validation_rules.NullRule(rule_name)
    
    def get_avaliabe_rules_list(self):
        return self.rules.keys()
        