from .rule_abs import AbsValidationRule
import string
from random import choice
from .uttils import random_swap
import unittest


class HaveDigitRule(AbsValidationRule):
    def is_validated(self, text: str) -> bool:
        return self._contains_digit(text)
    
    def _contains_digit(self, text: str) -> bool:
        return bool(set(text) & set(string.digits))
    
    def fix_validation_issue_if_needed(self, text):
        if self.is_validated(text):
           return text
        return "".join(random_swap(text, choice(string.digits)))



