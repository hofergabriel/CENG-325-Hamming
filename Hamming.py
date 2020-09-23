"""
Author: Gabriel Hofer
Course: CENG-325
Due: September 18, 2020
"""

import numpy as np
import random 

"""
  returns - p, a message
  n - length of message required
"""
def makeMessage(n): 
  return ((123*np.random.rand(n,1)).astype(int)) & 1

"""
G74:
  1101
  1011
  0111
  1000
  0100
  0010
  0001
"""
def encode(p):
  G74 = np.array([[1,1,0,1], [1,0,1,1], [0,1,1,1], [1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]])
  print(G74) 
  x = np.matmul(G74,p)
  print("x: ")
  print(x)
  x = x & 1
  print("x: ")
  print(x)
  return x


"""
  changes something in the message
  p - the message
  returns another message
"""
def makeError(p): pass 



"""
  Determines whether there was an error or not
  returns - z 

  H74:
    100|1101
    010|1011
    001|0111
"""
def parityCheck(x): 
  H74 = np.array([[1,0,0,1,1,0,1],[0,1,0,1,0,1,1],[0,0,1,0,1,1,1]])
  z = np.matmul(H74,x)
  print("z: ")
  print(z)
  z = z & 1
  print("z: ")
  print(z)

"""
"""
def correctError(): pass

"""
  Decode message using a decoding matrix
"""
def decodeMessage(): pass


"""
Used for debugging
"""
def debug():
  print("debugging") 
  p=makeMessage(4)
  x=encode(p)
  z=parityCheck(x) 

debug()

"""
  p - the message vector
  pLen - length of p, message
  returns nothing
"""
def main():
  # enter mode: either (7,4) or (15,11)
  mode=input("Enter mode: ")
  if mode=="H1511": pLen=11
  else : pLen=4

  # generate random message vector, p, of length 4 or 11 
  p = makeMessage();
  print("Message: "+message)

  # encode (make send vector)
  sendVector=encode(message,pLen)
  print("Send Vector: "+sendVector)

  # modify the vector to simulate an error or not
  recievedMessage=makeError()
  print("Recieved Message: "+recievedMessage)

  # Parity Check
  z=parityCheck()
  print("Parity Check: "+z);

  # Error Correction
  correctError()
  print("Corrected Message: ")

  # Decode Message 
  pr=decodeMesssage()
  print("Decoded Message: "+pr);
  





