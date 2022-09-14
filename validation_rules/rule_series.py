import itertools

from .rule_abs import AbsValidationRule


class SeriesRule(AbsValidationRule):
    def __init__(self, acceptable_in_row: int = 2) -> None:
        self.acceptable_in_row = acceptable_in_row
        self._assert_acceptable_in_row_is_positive()

    def _assert_acceptable_in_row_is_positive(self):
        if self.acceptable_in_row < 1:
            raise ValueError("acceptable_in_row value have to be positive number.")

    def is_validated(self, text: str) -> bool:
        lengths_mask = (
            len(list(block)) <= self.acceptable_in_row
            for _, block in itertools.groupby(text)
        )
        return all(lengths_mask)

    def fix_validation_issue_if_needed(self, text: str) -> str:
        shortened_blocks = [
            "".join(list(block))[: self.acceptable_in_row]
            for _, block in itertools.groupby(text)
        ]

        return "".join(shortened_blocks)
