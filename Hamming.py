"""
Author: Gabriel Hofer
Course: CENG-325
Due: September 18, 2020
"""

import numpy as np
import random 

"""
  returns - p, a message
  len - length of message required
"""
def makeMessage(len): pass

"""
  changes something in the message
  p - the message
  returns another message
"""
def makeError(p): pass 

"""
  Determines whether there was an error or not
  returns - z 
"""
def parityCheck(): pass

"""
"""
def correctError(): pass

"""
  Decode message using a decoding matrix
"""
def decodeMessage(): pass


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
  sendVector=encode(message,pLen
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
  










