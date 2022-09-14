from .rule_abs import AbsValidationRule
from random import choice
from .uttils import random_swap, SPECIAL_CHARACTERS


class SpecialCharRule(AbsValidationRule):
    def __init__(self) -> None:
        super().__init__()
        self.SPECIAL_CHARACTERS_SET = set(SPECIAL_CHARACTERS)

    def is_validated(self, text: str) -> bool:
        return self._contain_special_characters(text)

    def _contain_special_characters(self, text: str) -> bool:
        return bool(set(text) & self.SPECIAL_CHARACTERS_SET)

    def fix_validation_issue_if_needed(self, text: str) -> str:
        if self.is_validated(text):
            return text
        return "".join(random_swap(text, choice(SPECIAL_CHARACTERS)))
