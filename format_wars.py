import pandas as pd

def format_wars(file_in='wars.csv', file_out='wars_formatted.csv'):
    df = pd.read_csv(file_in)

    # Function to convert money strings to numbers
    def parse_money(x):
        if pd.isna(x):
            return None
        x = str(x).replace('$','').replace(',','').strip()
        if x.endswith('B'):
            return float(x[:-1]) * 1_000_000_000
        elif x.endswith('M'):
            return float(x[:-1]) * 1_000_000
        elif x.endswith('T'):
            return float(x[:-1]) * 1_000_000_000_000
        elif x.endswith('K'):
            return float(x[:-1]) * 1_000
        else:
            return float(x)

    # Function to convert percent strings to numbers
    def parse_percent(x):
        if pd.isna(x):
            return None
        x = str(x).replace('%','').replace('+','').replace('<','').strip()
        try:
            return float(x)
        except:
            return None

    # Apply formatting
    money_cols = ['Cost (2024 USD Inflation-Adjusted)']
    percent_cols = ['GDP Impact (Estimated % of GDP at Peak)', 
                    'War Debt Added to National Debt (%)',
                    'Public Approval Rating Today (%)']

    for col in money_cols:
        df[col] = df[col].apply(parse_money).round(0)

    for col in percent_cols:
        df[col] = df[col].apply(parse_percent).round(0)

    # Save formatted CSV
    df.to_csv(file_out, index=False)
    print(f"Wars formatted and saved to {file_out}.")

# Run the function
format_wars()