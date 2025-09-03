import time

class ReminderSystem:
    def schedule_reminders(self, booking):
        print(f"[Reminder] Sent to {booking['name']} for {booking['slot']}")
        print(" - Reminder 1: Standard")
        print(" - Reminder 2: Form completion check")
        print(" - Reminder 3: Final confirmation")
