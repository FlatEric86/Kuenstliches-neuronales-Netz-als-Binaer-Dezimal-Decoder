from tqdm import tqdm as tqdm
import random as rand
import pandas as pd

N = 20000

def encoder(integer):
    return "{0:{fill}16b}".format(integer, fill='0')
 


df = pd.DataFrame(columns=['decimal', 'binary'])

counter = 0
while tqdm(counter < N):
    z     = rand.randrange(0,65534)
    bin_z = encoder(z)
    
    if z in df.values:
        continue
        
    df = df.append(
        {
        'decimal':z,
        'binary':bin_z
        }
        ,ignore_index=True
    )
    counter += 1
    
df.to_csv('./validation_data.csv')    

