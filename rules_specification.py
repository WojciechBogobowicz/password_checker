task = {
    "SeriesRule": {"acceptable_in_row": 3},
    "HaveDigitRule": {},
    "SpecialCharRule": {},
    "UpercaseRule": {},
    "CorrectLengthRule": {"minimal_length": 20},
}

short = {
    "HaveDigitRule": {},
    "CorrectLengthRule": {"minimal_length": 4, "maximal_length": 4},
}

impossible = {
    "HaveDigitRule": {},
    "SpecialCharRule": {},
    "CorrectLengthRule": {"maximal_length": 1},
}
