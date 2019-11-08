import omdb
import pandas as pd
from IMDBParser import retorna_id
import json
import sys
from multiprocessing.dummy import Pool

#So rodar a primeira vez para construir o inicio do json
#with open('test.json', 'w') as f:
#    f.write("[")

anos = [2011,2012,2013,2014,2015,2016,2017,2018,2019]
with open('position_request.json', 'r') as g:
    dic = json.loads(g.read())

omdb.set_default('apikey', 'ca7ae7f8')

def requests(x):
	fim = 0
	while fim == 0:
		for i in range(dic[str(x)], len(retorna_id(x))):
		    if i == (len(retorna_id(x)) - 1):
		    	fim = 1 
		    	break
		    b = retorna_id(x)
		    try:
		        a = omdb.imdbid(b.iloc[i], timeout=5)
		        print(x, i)
		        with open('testrecent.json', 'a') as f:
		            if len(a) != 0:
			            json.dump(a, f)
			            f.write(",\n") 
		    except :
		        dic[str(x)] = i
		        print("Error:", sys.exc_info()[0], x, len(retorna_id(x)))
		        with open('position_request.json', 'w') as g:
		            json.dump(dic, g)
		        break

pool = Pool(len(anos))
pool.map(requests, anos)

pool.close()
pool.join()

print('FIM')





