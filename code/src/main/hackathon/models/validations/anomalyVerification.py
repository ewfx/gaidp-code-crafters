from src.main.hackathon.models.validations.validations import process_anomalies_dataset
import pandas as pd

class VerifyAnomalies:
    def __init__(self, config):
        self.anomalies = config.get_config('model','anomalies_path')
        self.final_anomalies = config.get_config('model','final_anomalies_path')
        self.final_anomalies_ui = config.get_config('model','final_anomalies_ui_path')

    def verify(self):
        # print(pd.read_csv(self.anomalies).head())
        df = process_anomalies_dataset(self.anomalies)
        df.to_csv(self.final_anomalies, index=False)
        # print('Anomalies verified and saved to', self.final_anomalies)
        # I want to print only identifiers and validation messages
        df[['IdentifierValue', 'ValidationMessages']].to_csv(self.final_anomalies_ui, index=False)
        pass
        