from abc import ABC, abstractmethod

class AbstractProduct(ABC):
    @abstractmethod
    def initiate_processing(self):
        pass
    @abstractmethod
    def read_data(self):
        pass
    @abstractmethod
    def preprocess_data(self):
        pass