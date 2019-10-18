import pandas as pd
import numpy as np




allGenres = []
allMovies = []
# df = pd.read_excel("title_basics.xlsx")
df = pd.read_csv('title_basics.tsv', sep='\t')
print(len(df.columns))
df.genres = df.genres.astype(str)
counter = 0
for i in df.index:
	if (counter < 20):
		# print(i)
		movie = df.iloc[i]
		genreList = movie["genres"].split(",")
		for e in genreList:
			if e not in allGenres:
				allGenres.append(e)
		if "Comedy" in genreList:
			print(movie["originalTitle"])
			allMovies.append({"movie":movie["originalTitle"],"genres":genreList})
			counter+=1

Movies_names = []
for i in allMovies:
    Movies_names.append(i["movie"])

print(allGenres)

counter = 1
dict_ids= {}
with open("dados.gml",'w+') as file:

	file.write("graph [\n")
	file.write("\tdirected 0\n")
	for name in Movies_names:
		file.write("\tnode [\n")
		file.write("\t\tid %s\n" % counter)
		file.write("""\t\tname "%s"\n""" % name)
		file.write("\t]\n")
		dict_ids[name]=counter

		counter +=1
	for genre in allGenres:
		file.write("\tnode [\n")
		file.write("\t\tid %s\n" % counter)
		file.write("""\t\tgenre %s"\n""" % genre)
		file.write("\t]\n")
		dict_ids[genre]=counter
		counter +=1
	for i in allMovies:
		for e in i["genres"]:
			file.write("\tedge [\n")
			file.write("\t\tsource %s\n" % dict_ids[i["movie"]])
			file.write("\t\ttarget %s\n" % dict_ids[e])
			file.write("\t]\n")



	file.write("]")
	file.close()

# dfcolumns = pd.read_excel('title_basics.xlsx')
# print(range(len(dfcolumns.columns)))
# df = pd.read_excel('title_basics.xlsx',
#                   header = None,
#                   skiprows = 1,
#                   usecols = list(range(len(dfcolumns.columns))),
#                   names = dfcolumns.columns)

# #Filtrando colunas
# df = df.drop(columns = "endYear")
# df = df.drop(columns = "runtimeMinutes")

# for i in df.index:
# 	print(i)