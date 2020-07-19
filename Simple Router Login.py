#python 3.7.1

#simple begin


print ("C o n t r o l - p a n e l\n\n")


user = ("admin")
pwd = ("admin")
  
user1 = ("user") 
pwd1 = ("user")

x = input("Enter USERNAME : ")

y = input("Enter PASSWORD : ")

if x == user or x == user1 and y == pwd or y == pwd1:
  
  for percent in range(1, 101):
    
    print(f'\rWaiting for scan information | {percent}% |\n')
    
    print ("Login Success") 

else: 
      
      for percent in range(1, 101):
        
        print(f'\rWaiting for scan  information | {percent}% |\n')
        
        print ("Error Login..try again!!\n")
        
        print ("Please don't forget put start")