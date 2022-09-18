from typing import Protocol, runtime_checkable
import typing


@runtime_checkable
class ValidationRule(Protocol):
    def is_validated(self, text: str) -> bool: ...


    def fix_validation_issue_if_needed(self, text: str) -> str: ...
    
    




