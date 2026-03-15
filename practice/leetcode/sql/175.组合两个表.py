import pandas as pd
import polars as pl

# pandas解答
data = [[1, 'Wang', 'Allen'], [2, 'Alice', 'Bob']]
person = pd.DataFrame(data, columns=['personId', 'firstName', 'lastName']).astype({'personId':'Int64', 'firstName':'object', 'lastName':'object'})
data = [[1, 2, 'New York City', 'New York'], [2, 3, 'Leetcode', 'California']]
address = pd.DataFrame(data, columns=['addressId', 'personId', 'city', 'state']).astype({'addressId':'Int64', 'personId':'Int64', 'city':'object', 'state':'object'})

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(person, address, on='personId', how='left')
    df = df[['firstName', 'lastName', 'city', 'state']]
    return df

print(combine_two_tables(person, address))



# polars解答

data = [[1, 'Wang', 'Allen'], [2, 'Alice', 'Bob']]
plperson = pl.DataFrame(data, schema=['personId', 'firstName', 'lastName'], orient='row')
data = [[1, 2, 'New York City', 'New York'], [2, 3, 'Leetcode', 'California']]
pladdress = pl.DataFrame(data, schema=['addressId', 'personId', 'city', 'state'], orient='row')

# print(plperson)
# print(pladdress)

def pl_combine_two_tables(person: pl.DataFrame, address: pl.DataFrame) -> pl.DataFrame:
    df = plperson.join(pladdress, on='personId', how='left')
    df = df.select([pl.col("firstName"), pl.col("lastName"), pl.col("city"), pl.col("state")])
    return df

print(pl_combine_two_tables(plperson, pladdress))