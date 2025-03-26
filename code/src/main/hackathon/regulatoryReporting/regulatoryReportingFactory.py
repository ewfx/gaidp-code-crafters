import sys

from src.main.hackathon.models.promptGeneration import append_file_contents_to_prompt
from src.main.hackathon.common.utils.configLoader import ConfigLoader
from src.main.hackathon.models.anomalyDetectionModels.modelTraining import ModelTraining
from src.main.hackathon.models.llm import get_gemini_response
from src.main.hackathon.models.validations.anomalyVerification import VerifyAnomalies

class RegulatoryReportingFactory:
    def __init__(self):
        self.config = ConfigLoader('config/config.yml')
        self.prompt = self.config.get_config('data','prompt')
        self.instructions = self.config.get_config('data','instructions')
        self.columns_instructions = self.config.get_config('data','column_instructions')
        self.final_prompt = self.config.get_config('data','final_prompt')
        self.validation_code = self.config.get_config('data','validation_code')
        pass

    def generateReport(self):
        print('Started generating report...')
        try:
            self.read_prompt_file()
            # print('validation code generated')
            modelTrainer = ModelTraining(self.config)
            modelTrainer.process()
            anomalyVerification = VerifyAnomalies(self.config)
            anomalyVerification.verify()
            print('Report generated successfully')
        except:
            print("Some Error Occurred. Please check the logs for more details")

    def read_prompt_file(self):
        try:
            append_file_contents_to_prompt(self.prompt, self.instructions, self.columns_instructions, self.final_prompt)
            self.prompt_text = open(self.final_prompt, 'r').read()
            generated_code=get_gemini_response(self.prompt_text)
            generated_code = generated_code.splitlines()[1:-1]
            generated_code = "\n".join(generated_code)
            with open(self.validation_code, 'w') as file:
                file.write(generated_code)
                   
        except FileNotFoundError:
            print("prompt.txt file not found")
