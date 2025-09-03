import pandas as pd

class Exporter:
    def __init__(self, filepath):
        self.filepath = filepath

    def save_booking(self, booking):
        df = pd.DataFrame([booking])
        try:
            existing = pd.read_excel(self.filepath)
            df = pd.concat([existing, df], ignore_index=True)
        except FileNotFoundError:
            pass
        df.to_excel(self.filepath, index=False)
