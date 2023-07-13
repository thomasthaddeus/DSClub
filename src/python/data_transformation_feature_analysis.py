"""data_transformation_feature_analysis.py

Transforming Data into Features
You are a data scientist at a clothing company and are working with a data set of customer reviews. This dataset is originally from Kaggle and has a lot of potential for various machine learning purposes. You are tasked with transforming some of these features to make the data more useful for analysis. To do this, you will have time to practice the following:

Transforming categorical data
Scaling your data
Working with date-time features
Let’s get started!

Tasks
16/16 Complete
Mark the tasks as complete by checking them off
Basic Exploration
1.
Let’s start with some basic exploring by performing the following:

First, import your dataset. It is stored under a file named reviews.csv. Save it to a variable called reviews.


Stuck? Get a hint
2.
Next, we want to look at the column names of our dataset along with their data types. Do the following two steps:

Print the column names of your dataset.
Check your features’ data types by printing .info().

Stuck? Get a hint
Data Transformations
3.
Transform the recommended feature. Start by printing the feature’s .value_counts().


Stuck? Get a hint
4.
Since this is a True/False feature, we want to transform it to 1 for True and 0 for False.

To do this, create a dictionary called binary_dict where:

The keys are what is currently in the recommended feature.
The values are what we want in the new column (0s and 1s).
Click the hint if you get stuck.


Stuck? Get a hint
5.
Using binary_dict, transform the recommended column so that it will now be binary. Print the results using .value_counts() to confirm the transformation.


Stuck? Get a hint
6.
Let’s run through a similar process to transform the rating feature. This is ordinal data so our transformation should make that more clear. Again, start by printing the .value_counts().

To check your output, click the hint.


Stuck? Get a hint
7.
We want to make the following changes to the values:

‘Loved it’ → 5
‘Liked it’ → 4
‘Was okay’ → 3
‘Not great’ → 2
‘Hated it’ → 1
Create a dictionary called rating_dict where the keys are what is currently in the feature and the values are what we want in the new column. You can use the hierarchy listed above to make your dictionary.


Stuck? Get a hint
8.
Using rating_dict, transform the rating column so it contains numerical values. Print the results using .value_counts() to confirm the transformation.


Stuck? Get a hint
9.
Let’s now transform the department_name feature. This process will be slightly different, but start by printing the .value_counts() of the feature.

Use Panda’s get_dummies to one-hot encode our feature.
Attach the results back to our original data frame.
Print the column names to see!

Hint
#get the number of categories in a feature
print(df['col_name'].value_counts())
10.
Use panda’s get_dummies() method to one-hot encode our feature. Assign this to a variable called one_hot.


Stuck? Get a hint
11.
Join the results from one_hot back to our original data frame. Then print out the column names. What has been added?


Stuck? Get a hint
12.
Let’s make one more feature transformation!

Transform the review_date feature.

This feature is listed as an object type, but we want this to be transformed into a date-time feature.

Transform review_date into a date-time feature.
Print the feature type to confirm the transformation.
Click the hint if you get stuck.


Hint
Your code should be similar to the following:

df['new_col'] = pd.to_datetime(df['col'])

print(df['new_col'].dtype)
Scaling the Data
13.
The final step we will take in our transformation project is scaling our data. We notice that we have a wide range of numbers thus far, so it is best to put everything on the same scale.

Let’s get our data frame to only have the numerical features we created. If you get stuck, click the hint.


Hint
Use the following line of code:

#get numerical columns
reviews = reviews[['clothing_id', 'age', 'recommended', 'rating', 'Bottoms', 'Dresses', 'Intimate', 'Jackets', 'Tops', 'Trend']].copy()
14.
Reset the index to be our clothing_id feature.


Hint
Use the .set_index() method:

#reset index
df = df.set_index(col)
15.
We are ready to scale our data! Perform a .fit_transform() on our data set, and print the results to see how the features have changed.


Hint
Create a StandardScaler() and then use .fit_transform() on reviews. Your code should be similar to the following two lines of code:

scaler = StandardScaler()
scaler.fit_transform(df)
16.
Congratulations!

You have successfully completed this transformation project. Transformations are an incredibly valuable skill to have. Great job!

_extended_summary_
"""


import pandas as pd
from sklearn.preprocessing import StandardScaler

# import data
df = pd.read_csv("reviews.csv")

# print column names
print(df.columns)

# print .info
print(df.info())

# look at the counts of recommended
print(df["recommended"].value_counts())

# create binary dictionary
binary_dict = {
    True: 1,
    False: 0,
}

# transform column
df["recommended"] = df["recommended"].map(binary_dict)

# print your transformed column
print(df["recommended"].value_counts())

# look at the counts of rating
print(df["rating"].value_counts())

# create dictionary
rating_dict = {
    "Loved it": 5,
    "Liked it": 4,
    "Was okay": 3,
    "Not great": 2,
    "Hated it": 1,
}

# transform rating column
df["rating"] = df["rating"].map(rating_dict)

# print your transformed column values
print(df["rating"].value_counts())

# get the number of categories in a feature
print(df["department_name"].value_counts())

# perform get_dummies
one_hot = pd.get_dummies(df["department_name"])

# join the new columns back onto the original
df = df.join(one_hot)

# print column names
print(df.columns)

# transform review_date to date-time data
df["review_date"] = pd.to_datetime(df["review_date"])

# print review_date data type
print(df["review_date"].dtype)

# get numerical columns
df = df[
    [
        "clothing_id",
        "age",
        "recommended",
        "rating",
        "Bottoms",
        "Dresses",
        "Intimate",
        "Jackets",
        "Tops",
        "Trend",
    ]
].copy()

# reset index
df = df.set_index('clothing_id')

# instantiate standard scaler
scaler = StandardScaler()

# fit transform data
scaler.fit_transform(df)
