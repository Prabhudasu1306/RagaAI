import pandas as pd
from src.scheduler import Scheduler
from src.database import PatientDB
from src.export import Exporter
from src.emailer import Emailer
from src.reminders import ReminderSystem

class SchedulingAgent:
    def __init__(self):
        self.patient_db = PatientDB("data/patients.csv")
        self.scheduler = Scheduler("data/doctor_schedules.xlsx")
        self.exporter = Exporter("output/bookings.xlsx")
        self.emailer = Emailer()
        self.reminders = ReminderSystem()
        self.state = {}

    def chat(self, message):
        if "name" not in self.state:
            self.state["name"] = message
            return "Hello {}, please provide your Date of Birth (YYYY-MM-DD)".format(message)

        elif "dob" not in self.state:
            self.state["dob"] = message
            patient_type = self.patient_db.lookup(self.state["name"], self.state["dob"])
            self.state["type"] = patient_type
            return f"Got it. You are a **{patient_type} patient**. Please choose a doctor."

        elif "doctor" not in self.state:
            self.state["doctor"] = message
            slots = self.scheduler.available_slots(self.state["doctor"], self.state["type"])
            return f"Available slots for {self.state['doctor']}:\n" + "\n".join(slots)

        elif "slot" not in self.state:
            self.state["slot"] = message
            return "Please provide your insurance carrier, member ID, and group number."

        elif "insurance" not in self.state:
            self.state["insurance"] = message
            self.exporter.save_booking(self.state)
            self.emailer.send_confirmation(self.state)
            self.reminders.schedule_reminders(self.state)
            return "✅ Appointment booked! Confirmation sent to your email with intake form."

        else:
            return "Your appointment is already booked. ✅"
