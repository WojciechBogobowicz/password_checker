import unittest
from validator import PasswordValidator

from validation_rules.rule_havedigit import HaveDigitRule
from validation_rules.rule_correctlength import CorrectLengthRule
from validation_rules.rule_series import SeriesRule
from validation_rules.rule_havespecialchar import SpecialCharRule
from validation_rules.rule_isupercase import UpercaseRule
from rules_specification import *


class HaveDigitRuleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.rule = HaveDigitRule()

    def test_contains_digit(self):
        self.assertTrue(self.rule._contains_digit("abdc7ef"))        
        self.assertTrue(self.rule._contains_digit("2"))        
        self.assertFalse(self.rule._contains_digit("abdcef")) 
        self.assertFalse(self.rule._contains_digit("!"))
        

    def test_fix_validation_issue_if_needed(self):
        self.assertEqual("ab5de", self.rule.fix_validation_issue_if_needed("ab5de"))
        self.assertTrue(self.rule._contains_digit(self.rule.fix_validation_issue_if_needed("abcdef")))
        

class CorrectLengthTest(unittest.TestCase):
    def setUp(self) -> None:
        self.rule44 = CorrectLengthRule(4, 4)
        self.rule28 = CorrectLengthRule(2, 8)
        
    def test_same_max_min(self):
        self.assertEqual(4, len(self.rule44.fix_validation_issue_if_needed("1234")))
        self.assertEqual(4, len(self.rule44.fix_validation_issue_if_needed("123456")))
        self.assertEqual(4, len(self.rule44.fix_validation_issue_if_needed("1")))
        

    def test_diff_max_min(self):
        self.assertTrue(2 <= len(self.rule28.fix_validation_issue_if_needed("1234")) <= 8)
        self.assertTrue(2 <= len(self.rule28.fix_validation_issue_if_needed("123456789012")) <= 8)
        self.assertTrue(2 <= len(self.rule28.fix_validation_issue_if_needed("1")) <= 8)
        

class SeriesRuleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.rule3 = SeriesRule(3)
        
    def test_fix_validation_issue_if_needed(self):
        self.assertEqual("aaabbccca", self.rule3.fix_validation_issue_if_needed("aaaabbcccccca"))
        self.assertEqual("aaabb???ccca", self.rule3.fix_validation_issue_if_needed("aaaabb??????cccccca"))
        self.assertEqual("aaaąąąbbccca", self.rule3.fix_validation_issue_if_needed("aaaaąąąąąąąbbcccccca"))
        

class SpecialCharRuleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.rule = SpecialCharRule()
        
    def test_fix_validation_issue_if_needed(self):
        self.assertTrue(self.rule._contain_special_characters("abd c7.ef")) 
        self.assertTrue(self.rule._contain_special_characters(",")) 
        self.assertFalse(self.rule._contain_special_characters("abk75kj"))
        self.assertFalse(self.rule._contain_special_characters("a5"))
        self.assertTrue(self.rule._contain_special_characters(self.rule.fix_validation_issue_if_needed("abcdef")))
        self.assertEqual("ab5,de", self.rule.fix_validation_issue_if_needed("ab5,de"))
        

class UpercaseRuleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.rule = UpercaseRule()
    
    def test_contains_uppercase(self):
        self.assertTrue(self.rule._contains_uppercase("abdC7ef"))        
        self.assertTrue(self.rule._contains_uppercase("F"))        
        self.assertFalse(self.rule._contains_uppercase("abdc; ef")) 
        self.assertFalse(self.rule._contains_uppercase("!a7"))

    def test_fix_validation_issue_if_needed(self):
        self.assertTrue(self.rule._contains_uppercase(self.rule.fix_validation_issue_if_needed("abcdef")))
        self.assertEqual("ab5De", self.rule.fix_validation_issue_if_needed("ab5De"))


class LowercaseRuleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.rule = LowercaseRule()
    
    def test_contains_uppercase(self):
        self.assertTrue(self.rule._contains_lowercase("abdC7ef"))        
        self.assertTrue(self.rule._contains_lowercase("f"))        
        self.assertFalse(self.rule._contains_lowercase("ABCD; EF")) 
        self.assertFalse(self.rule._contains_lowercase("!A7"))

    def test_fix_validation_issue_if_needed(self):
        self.assertTrue(self.rule._contains_uppercase(self.rule.fix_validation_issue_if_needed("ABCDEF")))
        self.assertEqual("ab5De", self.rule.fix_validation_issue_if_needed("ab5De"))


class PasswordValidatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.validator = PasswordValidator(specified_rules)
        self.validator_adam = PasswordValidator(specified_rules_adam)

    def test_get_fixed_password_adam(self):
        self._assertFixed("adam", self.validator_adam)

    def test_get_fixed_password(self):
        self._assertFixed("f;goirjfkj", self.validator)

    def _assertFixed(self, passowrd, validator):
        fixed_pass = validator.get_fixed_password(passowrd)
        self.assertTrue(validator._is_password_valid(fixed_pass))


if __name__ == "__main__":
    unittest.main()
