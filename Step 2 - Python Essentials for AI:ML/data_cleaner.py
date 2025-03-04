import pandas as pd
import numpy as np

class DataCleaner:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)

    def fill_missing(self):
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                self.df[col].fillna(self.df[col].mode()[0], inplace=True)
            else:
                self.df[col].fillna(self.df[col].median(), inplace=True)

    def normalize_numeric(self):
        numeric_cols = self.df.select_dtypes(include=np.number).columns
        for col in numeric_cols:
            self.df[col] = (self.df[col] - self.df[col].mean()) / self.df[col].std()

    def save_cleaned_file(self, output_path='cleaned_data.csv'):
        self.df.to_csv(output_path, index=False)

# Example usage
if __name__ == '__main__':
    cleaner = DataCleaner('sample_data.csv')
    cleaner.fill_missing()
    cleaner.normalize_numeric()
    cleaner.save_cleaned_file()
    print("✅ Data cleaned and saved!")
