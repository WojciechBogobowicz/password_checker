from .rule_abs import AbsValidationRule
from math import inf
import unittest
import random
import string


class CorrectLength(AbsValidationRule):
    def __init__(self, minimal_length: int=0, maximal_length: int|float=inf) -> None:
        super().__init__() 
        self.minimal_length = minimal_length
        self.maximal_length = maximal_length
        # TODO: min < max
    
    def is_validated(self, text: str) -> bool:
        return self.minimal_length <= len(text) <= self.maximal_length

    def fix_validation_issue_if_needed(self, text):
        if len(text) > self.maximal_length:
            return text[len(text) - self.minimal_length:]
        elif len(text) < self.minimal_length:
            return text + ''.join(random.choice(string.ascii_lowercase) for i in range(self.minimal_length - len(text)))
        return text


