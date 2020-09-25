"""-----------------------------------------------------------
  Author: Gabriel Hofer
  Course: CENG-325
  Due: September 18, 2020
-----------------------------------------------------------"""

import numpy as np
import random 
import math

def makeMessage(n): 
  return np.random.randint(2, size=(n, 1))

def encode(p):
  G74=np.array([ \
    [1,1,0,1], \
    [1,0,1,1], \
    [1,0,0,0], \
    [0,1,1,1], \
    [0,1,0,0], \
    [0,0,1,0], \
    [0,0,0,1]])
  x = np.matmul(G74,p)
  x = x & 1
  return x

def makeError(p): 
  rdm=random.randint(0,p.shape[0]-1)
  p[rdm,0]=p[rdm,0]^1;
  return p

def parityCheck(r): 
  H74 = np.array([ \
    [1,0,1,0,1,0,1], \
    [0,1,1,0,0,1,1], \
    [0,0,0,1,1,1,1]])
  z = np.matmul(H74,r)
  z = z & 1
  return z

def decodeMessage(r): 
  R74 = np.array([ \
    [0,0,1,0,0,0,0], \
    [0,0,0,0,1,0,0], \
    [0,0,0,0,0,1,0], \
    [0,0,0,0,0,0,1]])
  pr=np.matmul(R74,r)
  return pr

def correctError(z,r): 
  loc=0
  for i in range(0,z.shape[0]):
    loc+=z[i,0]*pow(2,i)
  print("loc: "+str(loc))
  r[loc-1,0]=r[loc-1,0]^1;
  return r

#-----------------------------------------------------------
def main():
  # enter mode: either (7,4) or (15,11)
  mode=input("Enter mode: ")
  if mode=="H1511": pLen=11
  else : pLen=4

  # generate random message vector, p, of length 4 or 11 
  p=makeMessage(pLen);
  print("Message:           "+str(p.transpose()))

  # encode (make send vector)
  x=encode(p)
  print("Send Vector:       "+str(x.transpose()))

  # modify the vector to simulate an error or not
  r=makeError(x)
  print("Recieved Message:  "+str(r.transpose()))

  # Parity Check
  z=parityCheck(r)
  print("Parity Check:      "+str(z.transpose()));

  # Error Correction
  corrected=correctError(z,r)
  print("Corrected Message: "+str(corrected.transpose()))

  # Decode Message 
  pr=decodeMessage(x)
  print("Decoded Message:   "+str(pr.transpose()));
  
main()


