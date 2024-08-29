import random

messages = ["You stink","You suck","You are dumb","You are amazing","You are a godsend","You are worth it"]#random.randit(0,4) will take a random between 0 and 4.  
print(messages[random.randint(0,len(messages)-1)])  #random.randit(0,len(messages)-1) takes the length of the list and choose random int between 0 and the length of the list.