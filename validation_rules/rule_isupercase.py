import string
import random

from .uttils import random_swap
from .rule_abs import AbsValidationRule


class UpercaseRule(AbsValidationRule):
    def is_validated(self, text: str) -> bool:
        return self._contains_uppercase(text)

    def _contains_uppercase(self, text: str) -> bool:
        return any(letter.isupper() for letter in text)

    def fix_validation_issue_if_needed(self, text: str) -> bool:
        if self.is_validated(text):
            return text
        return "".join(random_swap(text, random.choice(string.ascii_uppercase)))
