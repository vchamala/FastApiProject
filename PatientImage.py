# Author: Venkat Chamala
# Description: Class to represent image metadata.

class PatientImage:
    # data members of class
    name = "name"  # patient name
    dob = "dob"  # patient date of birth
    captured_date = "captured_date"  # patient image captured date

    # class default constructor
    def __init__(self, name, dob, captured_date):
        self.name = name
        self.dob = dob
        self.captured_date = captured_date
