# Week 5: Data Wrangling with Pandas

**Objective**: To learn how to manipulate data using Pandas.

## Materials

- Python installed on laptops
- Jupyter notebooks or any Python supported IDE
- Sample dataset (CSV file)

## Lab Outline

<details markdown="1"><summary>Table of Contents</summary>

- [Week 5: Data Wrangling with Pandas](#week-5-data-wrangling-with-pandas)
  - [Materials](#materials)
  - [Lab Outline](#lab-outline)
    - [Loading Data into Pandas DataFrame](#loading-data-into-pandas-dataframe)
    - [Filtering Data](#filtering-data)
    - [Sorting Data](#sorting-data)
    - [Grouping and Aggregation](#grouping-and-aggregation)
    - [Handling Missing Data](#handling-missing-data)
    - [Feature Engineering](#feature-engineering)
  - [Load and use data from JSON and SQL databases in Python](#load-and-use-data-from-json-and-sql-databases-in-python)
    - [JSON](#json)
    - [SQL](#sql)
    - [MySQL | PostgreSQL](#mysql--postgresql)
    - [Merge, Join, and Concatenate](#merge-join-and-concatenate)
    - [Pivot Tables](#pivot-tables)
    - [Date Functionality](#date-functionality)
    - [Visualizing Data](#visualizing-data)
    - [Applying Functions](#applying-functions)
    - [Multi-Indexing](#multi-indexing)
    - [Reshaping and Pivoting](#reshaping-and-pivoting)
    - [String Manipulation](#string-manipulation)
    - [Categorical Data](#categorical-data)
    - [Setting With Enlargement](#setting-with-enlargement)
    - [Time Series Functionality](#time-series-functionality)
    - [Reading HTML Tables](#reading-html-tables)
    - [Data Types in Pandas](#data-types-in-pandas)
  - [Discussion and Conclusion:](#discussion-and-conclusion)

</details>

### Loading Data into Pandas DataFrame

```python
import pandas as pd

# load data
df = pd.read_csv('sample_data.csv') # replace with your csv file

# inspect the first 5 rows of the dataframe
df.head()
```

### Filtering Data

Pandas provides powerful and flexible methods to filter your data.

```python
# filter rows based on condition
high_earning = df[df['Salary'] > 100000]

# filter using multiple conditions
high_earning_engineers = df[(df['Salary'] > 100000) & (df['Occupation'] == 'Engineer')]
```

### Sorting Data

Sorting your data according to certain criteria is another common operation.

```python
# sort by age
df_sorted = df.sort_values(by='Age')

# sort by multiple columns
df_sorted = df.sort_values(by=['Occupation', 'Age'])
```

### Grouping and Aggregation

Grouping and aggregation are powerful tools provided by pandas that allows you to group the data based on certain criteria and then apply aggregation functions such as sum, count, min, max etc.

```python
# group by occupation and calculate average salary
average_salary = df.groupby('Occupation')['Salary'].mean()
```

### Handling Missing Data

Pandas provides methods to handle missing data.

```python
# check for missing data
df.isnull().sum()

# drop rows with missing data
df_dropna = df.dropna()

# fill missing data
df_filled = df.fillna('MISSING')
```

### Feature Engineering

Feature engineering is the process of using domain knowledge of the data to create features that can be used by machine learning algorithms.

```python
# binning ages into categories
bins = [0, 18, 35, 60, 100]
labels = ['Child', 'Young Adult', 'Adult', 'Senior']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)
```

## Load and use data from JSON and SQL databases in Python

### JSON

JSON (JavaScript Object Notation) is a popular data format which is often used for transmitting data in web applications. It is easy for humans to read and write and easy for machines to parse and generate.

Here's how to load data from a JSON file:

```python
import json

# Open JSON file and load the data
with open('data.json') as f:
    data = json.load(f)

# You can now work with your data as a Python object
for item in data:
    print(item)
```

**NOTE**: replace `data.json` with the path to your actual JSON file.

### SQL

To interact with SQL databases from within a Python application, you can use the sqlite3 module, which is included in Python standard library.

Let's assume you have a SQLite database. Here's how you can load data from an SQLite database:

```python
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('test.db')  # replace 'test.db' with your SQLite database

# Create a cursor object
cur = conn.cursor()

# Write your SQL query
sql_query = "SELECT * FROM Customers;"  # replace with your SQL query

# Execute the query
cur.execute(sql_query)

# Fetch all the rows as a list and print them
rows = cur.fetchall()
for row in rows:
    print(row)

# Don't forget to close the connection once you're done
conn.close()
```

### MySQL | PostgreSQL

If your database is a MySQL or PostgreSQL or other types of SQL databases, you'd need a corresponding Python library (like `mysql-connector-python` or `psycopg2`) to interact with the database. The process will be similar to the SQLite example above: establish a connection, execute your query, fetch the results, and close the connection.

Also, if you want to convert your SQL data to a pandas DataFrame, you can use the `read_sql_query` function from pandas:

```python
import pandas as pd

# Assume you're still connected to the SQLite database, and 'conn' is your connection
df = pd.read_sql_query("SELECT * FROM Customers", conn)

# Now you can work with your SQL data as a pandas DataFrame
print(df.head())
```

**NOTE**: Remember to replace `test.db` and `SELECT * FROM Customers` with your actual database file and SQL query.

### Merge, Join, and Concatenate

Pandas has full-featured, high performance in-memory join operations that are similar to relational databases like SQL. These methods can be used to combine different dataframes.

```python
# Concatenation
result = pd.concat([df1, df2])

# Merge
result = pd.merge(df1, df2, on='key')

# Join
result = df1.join(df2)
```

### Pivot Tables

Pandas provides functionality to create Excel-style pivot tables for summarizing data. It serves as a powerful tool when trying to analyze large amounts of data.

```python
table = pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'], aggfunc=np.sum)
```

### Date Functionality

Extensive capabilities for working with dates, time series, and time-indexed data.

```python
# Create a range of dates
dates = pd.date_range('20230101', periods=6)

# Create a DataFrame using dates
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
```

### Visualizing Data

Pandas is integrated with Matplotlib to provide easy visualization of data.

```python
import matplotlib.pyplot as plt

# Plot all columns
df.plot()

# Plot one column against another
df.plot(x='A', y='B')

# Bar plot
df.plot.bar()

# Histogram
df.plot.hist(bins=12)
plt.show()
```

### Applying Functions

You can apply your own functions or lambda expressions across your data.

```python
# Apply function
df['column1'] = df['column1'].apply(lambda x: x*2)
```

### Multi-Indexing

Pandas can have multiple (two or more) index levels on an axis. This provides a way to work with higher dimensional data in a lower dimensional form.

```python
arrays = [np.array(['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux']),
          np.array(['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two'])]

df = pd.DataFrame(np.random.randn(8, 4), index=arrays)
```

### Reshaping and Pivoting

You can reshape your DataFrame using `melt` and `pivot` methods, which are particularly useful when your data is presented in a format that doesn't suit your analysis needs.

```python
# Melting
df_melted = pd.melt(df, id_vars=['A'], value_vars=['B', 'C'])

# Pivoting
df_pivoted = df.pivot(index='A', columns='B', values='C')
```

### String Manipulation

Pandas provides vectorized string functions that make it easy to operate on columns containing text.

```python
# Split string into multiple columns
df['col'] = df['col'].str.split('_', expand=True)

# Replace part of a string
df['col'] = df['col'].str.replace('old', 'new')

# Extract part of a string
df['col'] = df['col'].str.extract('(pattern)', expand=False)
```

### Categorical Data

Pandas can include categorical data in a DataFrame.

```python
df['grade'] = pd.Categorical(df['grade'], categories=['poor', 'average', 'good'], ordered=True)
```

### Setting With Enlargement

The `.loc/.iloc/.at/.iat` methods can perform enlargement when setting a non-existent key for that axis.

```python
df.loc['k'] = [1, 2, 3, 4]
```

### Time Series Functionality

Pandas has simple, powerful, and efficient functionality for performing resampling operations during frequency conversion.

```python
# Convert secondly data into 5-minutely data
df.resample('5Min').sum()

# Moving window statistics, like rolling mean and rolling standard deviation.
df.rolling(window=5).mean()
```

### Reading HTML Tables

You can read HTML tables directly into a DataFrame.

```python
dfs = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
```

### Data Types in Pandas

Sure, here's a table illustrating the types of data that can be ingested and output using pandas, along with the corresponding commands.

| Data Type    | Input Command                                     | Output Command                             |
| ------------ | ------------------------------------------------- | ------------------------------------------ |
| CSV          | pd.read_csv('filename.csv')                       | df.to_csv('filename.csv')                  |
| JSON         | pd.read_json('filename.json')                     | df.to_json('filename.json')                |
| HTML         | pd.read_html('url_or_filename.html')              | df.to_html('filename.html')                |
| SQL Database | pd.read_sql_query('sql_query', connection_object) | df.to_sql('table_name', connection_object) |
| Excel        | pd.read_excel('filename.xlsx')                    | df.to_excel('filename.xlsx')               |
| HDF5         | pd.read_hdf('filename.h5')                        | df.to_hdf('filename.h5', 'key')            |
| Feather      | pd.read_feather('filename.ftr')                   | df.to_feather('filename.ftr')              |
| Parquet      | pd.read_parquet('filename.parquet')               | df.to_parquet('filename.parquet')          |
| Stata        | pd.read_stata('filename.dta')                     | df.to_stata('filename.dta')                |
| SAS          | pd.read_sas('filename.sas7bdat')                  | N/A                                        |
| Pickle       | pd.read_pickle('filename.pkl')                    | df.to_pickle('filename.pkl')               |

## Discussion and Conclusion:

Discuss the topics covered, encourage questions, and sum up the session.

Remember to replace 'sample_data.csv' with the path to the actual dataset you're going to use for this session. All the data manipulations done in this lab should be related to the real-world data you're using, this will give the students a much better understanding and make the learning process more engaging.
Please note that for some commands, you might need to install additional libraries. For example, reading and writing to Excel files requires the openpyxl library, and interacting with SQL databases might require libraries like sqlite3, psycopg2, or mysql-connector-python.
