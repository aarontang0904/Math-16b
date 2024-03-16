import pandas as pd

# Question 1
def get_per_cap_gdp(file_path):
    '''
    Parameters:
    ------------
    file_path: str
        The path to the csv file containing the GDP and population data.
    
    Returns:
    ------------
    df: pandas.DataFrame
        A dataframe containing the country name and per-capita GDP.
    
    This function reads a csv file and returns a dataframe containing the country name and per-capita GDP.
    The per-capita GDP is calculated by dividing the GDP by the population.

    '''
    # Read the csv file
    df = pd.read_csv(file_path)

    # Calculate the per-capita GDP
    df['Per-Capita GDP'] = df['GDP'] / df['Population']

    # Return the country name and per-capita GDP
    return df[['Country Name', 'Per-Capita GDP']]

# Question 2
def get_emissions_sum(file_path, L1, L2):
    '''
    Parameters:
    ------------
    file_path: str
        The path to the csv file containing the emissions data.
    L1: list
        A list of strings containing the names of the countries to be included in the sum.
    L2: list
        A list of strings containing the names of the columns to be included in the sum.

    Returns:
    ------------
    float
        The sum of the emissions for the selected countries and columns.

    This function reads a csv file and returns the sum of the emissions for the selected countries and years.
    '''
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Select the rows where the country is in the list L1 and the columns in the list L2
    df_filtered = df[df['Country Name'].isin(L1)][['Country Name'] + L2]
    
    # Handle Nan values
    df_filtered.fillna(0, inplace=True)
    
    # Sum across the selected columns for each country, then sum across all countries
    return df_filtered[L2].sum().sum()

# Question 3
def get_total_volume(file_path, y):
    '''
    Parameters:
    ------------
    file_path: str
        The path to the csv file containing the stock data.
    y: str
        The year for which the stock volume is to be calculated.
    
    Returns:
    ------------
    float
        The sum of the stock volume for the selected year.

    This function reads a csv file and returns the sum of the stock volume for the selected year.
    '''
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Convert the Date column to string
    df['Date'] = [str(x) for x in df['Date']]

    # Select the rows where the Date column contains the selected year, then sum the Volume column
    return df[df['Date'].str.contains(y)]['Volume'].sum()

# Question 4
def get_max_price(file_path):
    '''
    Parameters:
    ------------
    file_path: str
        The path to the csv file containing the wine data.

    Returns:
    ------------
    pandas.DataFrame
        A dataframe containing the winery with the maximum price for each country.

    This function reads a csv file and returns a dataframe containing the winery with the maximum price for each country.
    '''
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Handle Nan values
    df = df.dropna(subset=['price'])

    # Group by 'country' and find the max price for each group
    max_prices = df.groupby('country')['price'].max()

    # Merge the max prices with the original dataframe to get all rows that match the max price
    result_df = df.merge(max_prices, on='country', suffixes=('', '_max'))

    # Filter rows where the price matches the max price within the group
    result_df = result_df[result_df['price'] == result_df['price_max']]

    # Sort by 'country' alphabetically
    result_df.sort_values('country', inplace=True)

    # In case of multiple wineries with the same max price, drop duplicates within each country
    result_df.drop_duplicates(subset=['country', 'winery'], inplace=True)

    # Set the 'country' as the index
    result_df.set_index('country', inplace=True)

    return result_df[['winery']]

# Question 5
def min_weight(file_path):
    '''
    Pamaeters:
    ------------
    file_path: str
        The path to the csv file containing the data.

    Returns:
    ------------
    pandas.DataFrame
        A dataframe containing the name and origin of the car with the minimum weight for each year.
    
    This function reads a csv file and returns a dataframe containing the name and origin of the car with the minimum weight for each year.
    '''
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Handle Nan values
    df = df.dropna(subset=['weight'])

    # Group by 'year' and find the min weight for each group
    min_weight = df.groupby('year')['weight'].min()

    # Merge the min weights with the original dataframe to get all rows that match the min weight
    merged_df = df.merge(min_weight, on='year', suffixes=('', '_min'))

    # Filter rows where the weight matches the min weight within the group
    result_df = merged_df[merged_df['weight'] == merged_df['weight_min']]

    # Sort by 'year' ascending
    result_df.set_index('year', inplace=True)

    return result_df[['name', 'origin']]