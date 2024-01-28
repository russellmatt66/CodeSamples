# How to create a DataFrame
# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.
fruits = pd.DataFrame({'Apples': [30], 'Bananas': [21]})

# Check your answer
# q1.check()
fruits

# How to add custom labels to the rows
# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruit_sales.
fruit_sales = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index=['2017 Sales', '2018 Sales'])

# Check your answer
q2.check()
fruit_sales
