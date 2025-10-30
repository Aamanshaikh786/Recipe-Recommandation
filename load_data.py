import pandas as pd 
from pymongo import MongoClient
import ast
# df=pd.read_csv("Food_Dataset.csv")
# # print(df.head(5))
# print(df.columns)
# df.rename(columns={'TranslatedRecipeName':'Recipe'},inplace=True)
# df.rename(columns={'TranslatedIngredients':'Spices'},inplace=True)
# df.rename(columns={'TotalTimeInMins':'TimeInMins'},inplace=True)
# df.rename(columns={'TranslatedInstructions':'Instructions'},inplace=True)
# df.rename(columns={'Cleaned-Ingredients':'Ingredients'},inplace=True)
# df.rename(columns={'Ingredient-count':'No_of_Ingredients'},inplace=True)
# df.drop(columns=['URL','image-url'],inplace=True)
# print(df.columns)
# df.to_csv('Food_recipe.csv')
# print(df['TranslatedIngredients'].head(5),df['Cleaned-Ingredients'].head(5))

#here we have made changes as per our requirements now we can use our dataset 
# df=pd.read_csv('Food_recipe.csv')
# print(df.columns)
# def ingredients(inge):
#     if pd.isna(inge):
#         return []
#     return [item.strip().lower() for item in inge.split(',')]
# df['Cleaned_Ingredients']=df['Ingredients'].apply(ingredients)
# df.to_csv('processes_recipe.csv')

df=pd.read_csv('processes_recipe.csv')

#one time step

df['Cleaned_Ingredients'] = df['Cleaned_Ingredients'].apply(ast.literal_eval)

#it will make data of each columns  
data = df.to_dict('records')

# Step 3: Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["recipe_db"]
collection = db["recipes"]

# Step 4: Clear old data (optional)
collection.delete_many({})

#that data is inserted
# Step 5: Insert new data
collection.insert_many(data)

print("✅ Data successfully inserted into MongoDB!")

