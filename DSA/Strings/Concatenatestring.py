def concatenate(a,b):
  c=a+b
  return c

while True:
  str1=input("Enter the first string")
  str2=input("Enter the second string")
  print(concatenate(str1,str2))
  a=input("Concatenate more strings? y/n")
  if a.lower()=="y":
    continue
  if a.lower()=="n":
    break
  else:
    print("You have entered an invalid response.")
    break
