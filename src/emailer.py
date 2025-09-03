class Emailer:
    def send_confirmation(self, booking):
        print(f"[Email Simulation]")
        print(f"To: {booking['name']}")
        print(f"Subject: Appointment Confirmation")
        print(f"Your appointment with {booking['doctor']} at {booking['slot']} is confirmed.")
        print("Attachment: New Patient Intake Form (simulated)")
