import omdb
import pandas as pd
from IMDBParser import retorna_id
import json

with open('test.json', 'w') as f:
    f.write("[")

omdb.set_default('apikey', 'ca7ae7f8')

for i in retorna_id():
    try:
        a = omdb.imdbid(i, timeout=5)
        with open('test.json', 'a') as f:
            json.dump(a, f)
            f.write(",\n") 
    except:
        f.write("]")
        f.close()



