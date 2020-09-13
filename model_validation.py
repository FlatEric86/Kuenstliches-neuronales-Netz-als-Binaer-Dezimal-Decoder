import numpy as np
import pandas as pd
import torch 
import torch.nn as nn
import torch.nn.functional as F
from tqdm import tqdm
import random as rand
import os
import time as t

import matplotlib.pyplot as plt


device   = torch.device('cpu')



class model(nn.Module):

    def __init__(self):
        super(model, self).__init__()
        
        self.lin1 = nn.Linear(16, 128)
        self.lin2 = nn.Linear(128, 1)      
        
    def forward(self, x):
   
        x = torch.nn.functional.relu(self.lin1(x))
        x = torch.nn.functional.relu(self.lin2(x))
               
        return x
   

   
netz = model().to(device) 
           
if os.path.isfile('./weights.pt'):
    netz.load_state_dict(torch.load('./weights.pt')) 
    
    
accuracy_counter = 0    
with open('./validation_data.csv') as fin:
    line_count = 0
    for line in tqdm(fin.readlines()):
        if line_count == 0:
            line_count += 1
            continue
            
        else:
            line    = line.strip('\n').split(',')
            dec_val = int(line[1])
            bin_val = [int(val) for val in line[2]]
            
            
            x = torch.tensor(bin_val).float().to(device)
            
            # the converted number ... here is the crux, because the Net produces floating point numbers which have to get convertet into
            # integer by rounding them. This is a critical part, because rounding errors may produce model errors.
            y = int(round(float(netz(x))))
            
            # print(80*'#')
            # print('Decimal value: ', dec_val)
            # print('Binary value : ', bin_val)
            
            # print('Model result : ', y)
            
            if y == dec_val:
                accuracy_counter += 1
                
                
                
            line_count += 1

            
accuracy = accuracy_counter/(line_count-1)   


print(80*'#')
print('\n\nAccuracy of model is: ', accuracy)         
            
            
            
            
            
