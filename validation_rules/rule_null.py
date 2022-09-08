from .rule_abs import AbsValidationRule
import warnings


class NullRule(AbsValidationRule):
    def __init__(self, name: str='') -> None:
        super().__init__()
        self._name = name

    def is_validated(self, text: str) -> bool:
        warnings.warn(f"You are trying to use rule {self._name} which isn't implemented in validation rules. NullRulle call insted. Returns always true")
        return True
    
    def fix_validation_issue_if_needed(self, text):
        return ''