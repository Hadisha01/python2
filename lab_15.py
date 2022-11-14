import random
strength = str(input("you want it strong or weak?: "))
if strength == "strong":
  keys =['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 
         'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 
         ';', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '.', '/', '!', '@', '$', '%', '^', '&', '*', '(', ')', '_', '+', 
         'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 
         'L', ':', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?']
  picked = random.sample(keys, 10)
  passe = str("".join(picked))
  print("your password is: "+ passe)
  
elif strength == 'weak':
  words = ['green','late','far','shoes','hot','tv','camel','indian','pizza','old','red','chockolate','orange']
  pickedd = random.sample(words,2)
  passs = str("".join(pickedd))
  print("your password is: "+ passs)
  