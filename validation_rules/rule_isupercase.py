from .rule_abs import AbsValidationRule
import string
import random
from .uttils import random_swap

class UpercaseRule(AbsValidationRule):
    def is_validated(self, text: str) -> bool:
        return self._contains_uppercase(text)
    
    def _contains_uppercase(self, text):
        return any(letter.isupper() for letter in text)
    
    def fix_validation_issue_if_needed(self, text):
        if self.is_validated(text):
            return text
        return ''.join(random_swap(text, random.choice(string.ascii_uppercase)))
