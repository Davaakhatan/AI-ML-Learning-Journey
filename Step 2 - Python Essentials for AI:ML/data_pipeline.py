import pandas as pd

class BaseProcessor:
    def load_data(self, filepath):
        raise NotImplementedError("Subclass must implement load_data")

class CSVProcessor(BaseProcessor):
    def load_data(self, filepath):
        return pd.read_csv(filepath)

class DataPipeline:
    def __init__(self, processor):
        self.processor = processor

    def run(self, filepath):
        df = self.processor.load_data(filepath)
        print(f"Loaded {df.shape[0]} rows from {filepath}")

pipeline = DataPipeline(CSVProcessor())
pipeline.run('sample_data.csv')
