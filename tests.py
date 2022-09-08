import unittest
from validation_rules.rule_islowecase import LowercaseRule
from validation_rules.rule_null import NullRule
from validator import CountDown, PasswordValidator
from validation_rules.rule_havedigit import HaveDigitRule
from validation_rules.rule_correctlength import CorrectLengthRule
from validation_rules.rule_series import SeriesRule
from validation_rules.rule_havespecialchar import SpecialCharRule
from validation_rules.rule_isupercase import UpercaseRule
from validation_rules.uttils import genrate_random_password, random_swap
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
        
    def test_init_error_handle(self):
        with self.assertRaises(ValueError):
            CorrectLengthRule(-1, 4)
        with self.assertRaises(ValueError):
            CorrectLengthRule(6, 4)

class SeriesRuleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.rule3 = SeriesRule(3)
        
    def test_fix_validation_issue_if_needed(self):
        self.assertEqual("aaabbccca", self.rule3.fix_validation_issue_if_needed("aaaabbcccccca"))
        self.assertEqual("aaabb???ccca", self.rule3.fix_validation_issue_if_needed("aaaabb??????cccccca"))
        self.assertEqual("aaaąąąbbccca", self.rule3.fix_validation_issue_if_needed("aaaaąąąąąąąbbcccccca"))

    def test_init_exceptions_handle(self):
        with self.assertRaises(ValueError):
            SeriesRule(0)
        with self.assertRaises(ValueError):
            SeriesRule(-1)
        

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
        self.assertTrue(self.rule._contains_lowercase(self.rule.fix_validation_issue_if_needed("ABCDEF")))
        self.assertEqual("ab5De", self.rule.fix_validation_issue_if_needed("ab5De"))


class NullRuleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.rule = NullRule("name")
    
    def test_is_validated(self):
        self.assertTrue(self.rule.is_validated("asdas"))
    
    def test_fix_validation_issue_if_needed(self):
        password = "12345asd.,/ASD"
        self.assertEqual(password, self.rule.fix_validation_issue_if_needed(password))


class PasswordValidatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.validator = PasswordValidator(specified_rules_task)
        self.validator_short = PasswordValidator(specified_rules_short)
        self.validator_imposible = PasswordValidator(specified_rules_impossible)

    def test_get_fixed_password_adam(self):
        self._assertFixed("adam", self.validator_short)

    def test_get_fixed_password(self):
        self._assertFixed("f;goirjfkj", self.validator)

    def test_get_fixed_password_errors_handle(self):
        with self.assertRaises(RuntimeError):
            self.validator_imposible.get_fixed_password("sdfghj") 
        with self.assertRaises(ValueError):
            self.validator.get_fixed_password("asdfg", max_tries=0)          

    def _assertFixed(self, passowrd, validator):
        fixed_pass = validator.get_fixed_password(passowrd)
        self.assertTrue(validator._is_password_valid(fixed_pass))


class CountDownTest(unittest.TestCase):
    def setUp(self) -> None:
        self.counter3 = CountDown(3)
    
    def test_tick(self):
        self.assertTrue(self.counter3.tick())
        self.assertTrue(self.counter3.tick())
        self.assertFalse(self.counter3.tick())
    
    def test_tick_errors_handle(self):
        with self.assertRaises(ValueError):
            CountDown(0)
        with self.assertRaises(ValueError):
            CountDown(-1)

class UtilsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.digit_rule = HaveDigitRule()
        self.correct_length_rule = CorrectLengthRule(4, 4)
        self.spcial_char_rule = SpecialCharRule()
        self.upercase_rule = UpercaseRule()
        self.lowercase_rule = LowercaseRule()
    
    def test_generate_random_password_len(self):
        passwd = genrate_random_password(4)
        self.assertTrue(self.correct_length_rule.is_validated(passwd))
    
    def test_generate_random_password_lowercase(self):
        passwd = genrate_random_password(1, True, False, False, False)
        self.assertTrue(self.lowercase_rule.is_validated(passwd))
        
    def test_generate_random_password_upercase(self):
        passwd = genrate_random_password(1, False, True, False, False)
        self.assertTrue(self.upercase_rule.is_validated(passwd))

    def test_generate_random_password_digit(self):
        passwd = genrate_random_password(1, False, False, True, False)
        self.assertTrue(self.digit_rule.is_validated(passwd))

    def test_generate_random_password_specialchar(self):
        passwd = genrate_random_password(1, False, False, False, True)
        self.assertTrue(self.spcial_char_rule.is_validated(passwd))
    
    def test_random_swap(self):
        items = (1, 2)
        self.assertEqual(items, random_swap(*items, proba=0))
        self.assertEqual(items, random_swap(*items[::-1], proba=1))
    
    def test_random_swap_handle_exceptions(self):
        with self.assertRaises(ValueError):
            random_swap(None, None, -1)
        with self.assertRaises(ValueError):
            random_swap(None, None, 2)
    
        
        


if __name__ == "__main__":
    unittest.main()
