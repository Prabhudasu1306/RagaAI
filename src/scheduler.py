import pandas as pd

class Scheduler:
    def __init__(self, filepath):
        self.df = pd.read_excel(filepath)

    def available_slots(self, doctor, patient_type):
        duration = 60 if patient_type == "New" else 30
        doctor_slots = self.df[self.df["doctor"] == doctor]["slots"].tolist()
        return [f"{slot} ({duration} mins)" for slot in doctor_slots]
