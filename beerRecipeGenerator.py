#   Author: Tom Craig
#   Purpose: Dealing with Big Data, when too big to assign to a variable to analyse the most popular brewing choices from recipes around the world 
#   
#   

# Creating a generator that will generate the data row by row
def beerRecipeGenerator():
    file = "/Users/tomcraig/Documents/BeCloudReady/Git/generator/recipeData.csv"
    for row in open(file, encoding="ISO-8859-1"):
        yield row

# Store an instance of the generator so we can refer back to it
beer = beerRecipeGenerator()
print(next(beer))

