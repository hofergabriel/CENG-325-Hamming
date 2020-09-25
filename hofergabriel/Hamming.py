"""-----------------------------------------------------------
  Author: Gabriel Hofer
  Course: CENG-325
  Instructor: Dr. Karlsson
  Due: September 18, 2020
-----------------------------------------------------------"""
import numpy as np
import random 
import math

def makeMessage(n): 
  return np.random.randint(2, size=(n, 1))

def makeError(p): 
  if random.randint(0,1): return p
  # print("***MADE ERROR***")
  rdm=random.randint(0,p.shape[0]-1)
  p[rdm,0]=p[rdm,0]^1;
  return p

def correctError(z,r): 
  loc=0
  for i in range(0,z.shape[0]):
    loc+=z[i,0]*pow(2,i)
  if loc==0: return r
  # print("***Location of Error: "+str(loc)+"  ***")
  r[loc-1,0]=r[loc-1,0]^1;
  return r

def encode(G,p):
  return np.matmul(G,p) & 1

def parityCheck(H,r): 
  return np.matmul(H,r) & 1

def decodeMessage(R,r): 
  return np.matmul(R,r)

#-----------------------------------------------------------
def main():
  # enter mode: either (7,4) or (15,11)
  mode=input("Enter mode: ")
  if mode=="H1511": 
    pLen=11
    G=np.array([
      [1,1,0,1,1,0,1,0,1,0,1], \
      [1,0,1,1,0,1,1,0,0,1,1], \
      [1,0,0,0,0,0,0,0,0,0,0], \
      [0,1,1,1,0,0,0,1,1,1,1], \
      [0,1,0,0,0,0,0,0,0,0,0], \
      [0,0,1,0,0,0,0,0,0,0,0], \
      [0,0,0,1,0,0,0,0,0,0,0], \
      [0,0,0,0,1,1,1,1,1,1,1], \
      [0,0,0,0,1,0,0,0,0,0,0], \
      [0,0,0,0,0,1,0,0,0,0,0], \
      [0,0,0,0,0,0,1,0,0,0,0], \
      [0,0,0,0,0,0,0,1,0,0,0], \
      [0,0,0,0,0,0,0,0,1,0,0], \
      [0,0,0,0,0,0,0,0,0,1,0], \
      [0,0,0,0,0,0,0,0,0,0,1]])
    H = np.array([ \
      [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1], \
      [0,1,1,0,0,1,1,0,0,1,1,0,0,1,1], \
      [0,0,0,1,1,1,1,0,0,0,0,1,1,1,1], \
      [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1], \
      ])
    R = np.array([ \
     [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0], \
     [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0], \
     [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0], \
     [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0], \
     [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0], \
     [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0], \
     [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0], \
     [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0], \
     [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0], \
     [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0], \
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]])
  else : 
    pLen=4
    G=np.array([ \
      [1,1,0,1], \
      [1,0,1,1], \
      [1,0,0,0], \
      [0,1,1,1], \
      [0,1,0,0], \
      [0,0,1,0], \
      [0,0,0,1]])
    H = np.array([ \
      [1,0,1,0,1,0,1], \
      [0,1,1,0,0,1,1], \
      [0,0,0,1,1,1,1]])
    R = np.array([ \
      [0,0,1,0,0,0,0], \
      [0,0,0,0,1,0,0], \
      [0,0,0,0,0,1,0], \
      [0,0,0,0,0,0,1]])

  # generate random message vector, p, of length 4 or 11 
  p=makeMessage(pLen);
  print("Message          : "+str(p.transpose()[0]))

  # encode (make send vector)
  x=encode(G,p)
  print("Send Vector      : "+str(x.transpose()[0]))

  # modify the vector to simulate an error or not
  r=makeError(x)
  print("Received Message : "+str(r.transpose()[0]))

  # Parity Check
  z=parityCheck(H,r)
  print("Parity Check     : "+str(z.transpose()[0]));

  # Error Correction
  corrected=correctError(z,r)
  print("Corrected Message: "+str(corrected.transpose()[0]))

  # Decode Message 
  pr=decodeMessage(R,x)
  print("Decoded Message  : "+str(pr.transpose()[0]));
  
main()


