import pandas as pd

class PatientDB:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)

    def lookup(self, name, dob):
        match = self.df[(self.df["name"].str.lower() == name.lower()) &
                        (self.df["dob"] == dob)]
        return "Returning" if not match.empty else "New"
