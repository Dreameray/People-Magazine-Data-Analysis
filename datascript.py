# First, you will need to import the necessary libraries
import pandas as pd

# Next, you will need to load your data into a Pandas DataFrame.
# You can do this by using the read_csv function, which takes a file path or URL as an argument
pd.set_option('display.max_rows', None)

df = pd.read_csv("people.csv")

df = df.sort_values(by=['Main Keyword','Theme', 'Representations' , 'Changing After An Event', 'Past Tragedy' ,'Overall Percepted Theme', 'Sameness'])
df = df.drop_duplicates(subset=['Main Keyword','Theme', 'Representations', 'Changing After An Event' ,'Past Tragedy' ,'Overall Percepted Theme', 'Sameness'], keep='first')
print(df)

#Make an output file
#df.to_csv('output.csv', index=False)

#Individuals
#df2 = pd.read_csv("people.csv")
#df2 = df2[df2['Representations'] == 'Individual']
#df2_grouped = df2.groupby(['Main Keyword']).size()


#Remove duplicate as groups
#df = df.drop_duplicates(subset=['Theme', 'Changing After An Event', 'Representations' ,'Past Tragedy' ,'Overall Percepted Theme'], keep='first')

#print(df)

df_grouped = df.groupby(['Main Keyword']).size()
print(df_grouped)



