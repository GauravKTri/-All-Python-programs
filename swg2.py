import random
print("1-snake,2-water,3-gun")
i=0
while i<10:
  list1=[1,2,3]
  rand=random.choice(list1)
  end=int(input("entre sign\n"))
  if rand==1 and end==1:
    print("drew")
    break
  elif rand==1 and end==2:
    print("computer win")
    break
  elif rand==1 and end==3:
    print("you win")
    break 
  elif rand==2 and end==1:
    print("you win")
    break 
  elif rand==2 and end==2:
    print("tie")
    break 
  elif rand==2 and end==3:
    print("computer win")
    break 
  elif rand==3 and end==1:
    print("computer win")
    break 
  elif rand==3 and end==2:
    print("you win")
    break 
  elif rand==3 and end==3:
    print("tie")
  i=i+1