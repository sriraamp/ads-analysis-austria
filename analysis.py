
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data/ads_austria_1000.csv')
sns.set(style='whitegrid')

def top_brands():
    brand_counts = df['Brand'].value_counts().head(10)
    brand_counts.plot(kind='barh', title='Top Austrian Brands')
    plt.tight_layout()
    plt.savefig('visuals/top_brands.png')

if __name__ == '__main__':
    top_brands()
