import omdb
import pandas as pd
from IMDBParser import retorna_id
import json

with open('test.json', 'w') as f:
    f.write("[")

omdb.set_default('apikey', '2777e8dd')

for i in retorna_id():
    try:
        a = omdb.imdbid(i, timeout=5)
        with open('test.json', 'a') as f:
            json.dump(a, f)
            f.write(",\n") 
    except:
        f.write("]")    
        f.close()
    



