import pandas as pd

df = pd.read_csv("C:/Users/hugoc/Desktop/dataim.tsv", sep='\t')
df = df[df.startYear != "\\N"].astype({"startYear": int})
df = df[(df.startYear >= 2011) & (df.startYear < 2020) & (df.genres != "\\N") & (df.titleType == "movie")]
df = df[(~df.genres.str.contains("Reality-TV")) & (~df.genres.str.contains("Sport")) & (~df.genres.str.contains("News")) & (~df.genres.str.contains("Talk-Show")) & (~df.genres.str.contains("Game-Show"))]
print(df.head())

def retorna_id(x):
    df1 = df[(df.startYear == x)]
    return df1["tconst"]




#Mostra todos os generos de filmes
#df.genres = df.genres.astype(str)
# g = []
# for i in df.index:
#     movie = df.iloc[i]
#     genreList = movie["genres"].split(",")
#     for j in genreList:
#             if j not in g:
#                 g.append(j)
#                 print(j)


