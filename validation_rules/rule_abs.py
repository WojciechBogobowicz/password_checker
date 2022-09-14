import abc


class AbsValidationRule(abc.ABC):
    @abc.abstractmethod
    def is_validated(self, text: str) -> bool:
        pass

    @abc.abstractmethod
    def fix_validation_issue_if_needed(self, text: str) -> str:
        pass
