



list=[["1","2","3"],["4","5","6"],["7","8","9"]]
avail_value={1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:"",}

total_move=9;
ava=True
check=True
player1=False
player2=True
winner=""

def winningDecision():
  global check
  global winner
  if list[0][0]==list[0][1]==list[0][2]:
    winner=list[0][0]
    list[0][0]=list[0][1]=list[0][2]="win"
    check=False
    print "win"
  if list[1][0]==list[1][1]==list[1][2]:
    winner=list[1][0]
    list[1][0]=list[1][1]=list[1][2]="win"
    check=False
    print "win"  
  if list[2][0]==list[2][1]==list[2][2]:
    winner=list[2][0]
    list[2][0]=list[2][1]=list[2][2]="win"
    check=False
    print "win"
  if list[0][0]==list[1][0]==list[2][0]:
     winner=list[0][0]
     list[0][0]=list[1][0]=list[2][0]="win"
     check=False
     print "win"
  if list[0][1]==list[1][1]==list[2][1]:
     winner=list[0][1]
     list[0][1]=list[1][1]=list[2][1]="win"
     check=False
     print "win"
     
  if list[0][2]==list[1][2]==list[2][2]:
     winner=list[0][2]
     list[0][2]=list[1][2]=list[2][2]="win"
     check=False
     print "win"
  if list[0][0]==list[1][1]==list[2][2]:
     winner=list[0][0]
     list[0][0]=list[1][1]=list[2][2]="win"
     check=False
     print "win"   
     
    

def fillBox(arg,player1,player2):
    global total_move
    
    if avail_value[arg]=="sealed":
      print "cell is not available "
      if player1:
        print "Player 2 move"
      else:
        print "player 1 move "
      total_move+=1
      return False
    else:
      avail_value[arg]="sealed"
      if player1:
        print "Player 1 move"
      else:
        print "player 2 move "
  
    
    if arg==1 and player1:
      list[0][0]='X'
      
    
    if arg==1 and player2:
      list[0][0]='O'
      
      
    if arg==2 and player1:
      list[0][1]='X'
      
      
    if arg==2 and player2:
      list[0][1]='O'
      
      
    if arg==3 and player1:
      list[0][2]='X'
      
      
    if arg==3 and player2:
      list[0][2]='O'
      
      
    if arg==4 and player1:
      list[1][0]='X'
      
      
    if arg==4 and player2:
      list[1][0]='O'
      
      
    if arg==5 and player1:
      list[1][1]='X'
     
      
      
    if arg==5 and player2:
      list[1][1]='O'
      
      
      
    if arg==6 and player1:
      list[1][2]='X'
      
      
      
    if arg==6 and player2:
      list[1][2]='O'
      
      
    if arg==7 and player1:
      list[2][0]='X'
      
      
      
    if arg==7 and player2:
      list[2][0]='O'
      
      
      
    if arg==8 and player1:
      list[2][1]='X'
      
      
    if arg==8 and player2:
      list[2][1]='O' 
      
      
    if arg==9 and player1:
      list[2][2]='X'
      
      
    if arg==9 and player2:
      list[2][2]='O' 
      
    
    return True
       
    
       
      
    
def display():
  print "Board state Below" 
  print "_ _ _ _ _ _ _ _ _ _ _ _"
  print ""
  for x in list:
    for y in x:
      print " |  "+y+" ",
    print "\n_ _ _ _ _ _ _ _ _ _ _ _\n"
    
    
 
      


display()
print "player 1 move"
print  "Move left:{}".format(total_move)    
while ava and check:
  if(total_move==1):
    ava=False
  try:  
    var =raw_input("Enter value :")
    if player1:
      if fillBox(int(var),player1,player2):
         player1=False
         player2=True
         
      
        
    else:
      if fillBox(int(var),player1,player2):
         player1=True
         player2=False
      
      
    total_move -= 1
    print  "Move left:{}".format(total_move)
    winningDecision()
    display()
  except:
    print "Invalid input enter number between(1 to 9) please"
    continue

if check==False:
  if winner=="X":
    print "Match over player 2 win"
  else:
    print "Match over player 1 win"
else:
  print "Match over Drawn"
  
  