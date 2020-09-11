import torch 
import torch.nn as nn
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


# here we're load the training data as a native way, because the second column
# of the CSV-Array includes the binary values.
# In Pandas, these values seem to can't interpretated as binarys , but as integer
with open('./t_data.csv') as fin:

    # the binary numbers as list
    X = []
    # the decoded decimal values as list
    Y = []

    counter = 0
    for line in fin.readlines():
        if counter == 0:
            counter += 1
            continue            
        else:
            line = line.strip('\n').split(',')
      
            Y.append([int(line[1])])
            X.append([int(val) for val in line[2]])

   
# here we're do convert our lists of training data 
# to PyTorch tensor objects
X = torch.tensor(X).float()
Y = torch.tensor(Y).float()



# check if CUDA is possible and store value
use_cuda = torch.cuda.is_available()

#use_cuda = False

# define device in dependency if CUDA is available or not. 
device   = torch.device('cuda:0' if use_cuda else 'cpu')

# define number of CPU cores if device gots defined as CPU
if use_cuda == False:
    torch.set_num_threads(14)   # let one core there for os
    
    
    
# do split trainingsdata into data to train model as well into a test data set
X_training, X_test, Y_training, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)

# move the training data tensors into the GPU RAM
X_training = X_training.to(device) 
X_test     = X_test.to(device) 
Y_training = Y_training.to(device) 
Y_test     =  Y_test.to(device) 




# model definition: a simple feed forward net with only 1 hidden layer, which has includes 128 neurons
# The first layer has 16 entry-neurons, Each one for each bit of a 16 bit binary integer number
# The output layer consists of only 1 Neuron which gives us the decoded binary number as decimal number
class model(nn.Module):


    def __init__(self):
        super(model, self).__init__()
        
        self.lin1 = nn.Linear(16, 128)
        self.lin6 = nn.Linear(128, 1)
        
    def forward(self, x):
    
        x = torch.nn.functional.relu(self.lin1(x))
        x = torch.nn.functional.relu(self.lin6(x))
                
        return x
        
      
# number of learning iterations      
N_epoch = 5000

# learning rate
lr      = 0.00005  
      
# criterion of the model optimization
criterion = nn.MSELoss()   

# the neural net as object   
netz = model().to(device)
    
    
# do loading the model state of an old model if it does exist    
if os.path.isfile('./weights.pt'):
    netz.load_state_dict(torch.load('./weights.pt'))      
    
    
# optimizer = torch.optim.SGD(netz.parameters(), lr=lr)
optimizer = torch.optim.Adam(netz.parameters(), lr=lr)

# we do instantiate a loss object here
loss_function = nn.MSELoss()   
        
        
# list of loss values maped on the iteration of the model optimization  
LOSS      = [] 
# list of loss values of the test data maped on the iteration of the model optimization       
TEST_LOSS = []       
        
        
        
###############################################################################  
################################# TRAINING ####################################
###############################################################################
      
for i in range(N_epoch):
   
    ### set gradient as 0 
    netz.zero_grad()
    
    
    outputs = netz(X_training).to(device)
    
    loss = loss_function(outputs, Y_training)
    print(80*'~')
    print('#Iteration :',i)
    print('loss value :', loss)
    

    # backpropagation of the model error
    loss.backward()  
    optimizer.step()


    LOSS.append(float(loss))
    
    test_outputs = netz(X_test).to(device)
    test_loss    = loss_function(test_outputs, Y_test)
    TEST_LOSS.append(float(test_loss))


   

# do write out the optimized model parameters as PT-file
torch.save(netz.state_dict(), './weights.pt')


### model optimization process visualization

epochs = [i for i in range(len(LOSS))]

plt.plot(epochs, LOSS, color='green', label='training')
plt.plot(epochs, TEST_LOSS, color='blue', label='test')
plt.title('Model Evaluation')
plt.xlabel('Number of Iterations')
plt.ylabel('Value of Loss')
plt.legend()
plt.show()


