import pandas as pd
import matplotlib.pyplot as plt

def profile_data(file_path):
    df = pd.read_csv(file_path)

    print("\nBasic Info:")
    print(df.info())

    print("\nSummary Statistics:")
    print(df.describe())

    for column in df.select_dtypes(include='number'):
        plt.hist(df[column].dropna(), bins=20)
        plt.title(f'Distribution of {column}')
        plt.show()

if __name__ == '__main__':
    profile_data('sample_data.csv')
