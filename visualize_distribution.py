import pandas as pd
import matplotlib.pyplot as plt


csv_file_path = '/Users/srijitaseth/distribution_of_ages_or_genders_in_a_population/Human Development Index - Full.csv'
try:
    df = pd.read_csv(csv_file_path, on_bad_lines='skip')
except pd.errors.ParserError as e:
    print(f"Error parsing the CSV file: {e}")


life_expectancy_columns = [col for col in df.columns if 'Life Expectancy at Birth' in col]


life_expectancy_df = df[life_expectancy_columns]
life_expectancy_df = life_expectancy_df.melt(var_name='Year', value_name='Life Expectancy at Birth')


life_expectancy_df['Year'] = life_expectancy_df['Year'].str.extract(r'\((\d{4})\)')[0]


life_expectancy_df['Year'] = pd.to_numeric(life_expectancy_df['Year'])


life_expectancy_df = life_expectancy_df.dropna()

def plot_life_expectancy_distribution(data):
    plt.figure(figsize=(14, 7))
    data.groupby('Year')['Life Expectancy at Birth'].mean().plot(kind='bar', color='lightblue', edgecolor='black')
    plt.title('Average Life Expectancy at Birth Over Time')
    plt.xlabel('Year')
    plt.ylabel('Average Life Expectancy at Birth')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


plot_life_expectancy_distribution(life_expectancy_df)
