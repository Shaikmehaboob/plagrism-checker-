# Importing SequenceMatcher
# from difflib module
from difflib import SequenceMatcher

# Declaring string variables 
# change the strings here 
string1 = 'As thiis is a internship program for students and experience peoples free of cost so there is no stipend provided to you'
string2 = 'the code clause will give internships'

# Using the SequenceMatcher()
match = SequenceMatcher(None,
						string1, string2)

# convert above output into ratio
# and multiplying it with 100
result = match.ratio() * 100

# Display the final result
print(int(result), "%")
