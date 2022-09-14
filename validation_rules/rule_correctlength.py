from math import inf

from .uttils import genrate_random_password
from .rule_abs import AbsValidationRule


class CorrectLengthRule(AbsValidationRule):
    def __init__(
        self, minimal_length: int = 0, maximal_length: int | float = inf
    ) -> None:
        super().__init__()
        self.minimal_length = minimal_length
        self.maximal_length = maximal_length
        self._assert_min_max_is_range()
        self._assert_min_max_is_positive()

    def _assert_min_max_is_range(self):
        if self.maximal_length < self.minimal_length:
            raise ValueError(
                "Maximal length have to be greater or equal minimal length."
            )

    def _assert_min_max_is_positive(self):
        if self.maximal_length < 0:
            raise ValueError("Maximal length have to be positive number")
        if self.minimal_length < 0:
            raise ValueError("Minimal length have to be positive number")

    def is_validated(self, text: str) -> bool:
        return self.minimal_length <= len(text) <= self.maximal_length

    def fix_validation_issue_if_needed(self, text: str) -> str:
        if len(text) > self.maximal_length:
            return text[len(text) - self.minimal_length :]
        elif len(text) < self.minimal_length:
            missing_len = self.minimal_length - len(text)
            return f"{text}{genrate_random_password(missing_len)}"
        return text
