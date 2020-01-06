import random
print('Rock Scissors Paper')



def loop():
    print('Please enter your items [rock,scissors,paper]')
    player = input().lower()
    
    words = ['rock','scissors','paper']
    word =  random.choice(words)


    
    if player == 'rock' and word == 'scissors':
        print('you choose  ' + player + '  computer choose  ' + word)
        print('player win')
        
    elif player == 'scissors' and word == 'rock':
         print('you choose  ' + player + '  computer choose  ' + word)
         print('computer win')    
         
         
    elif player == 'paper' and word == 'scissors':
         print('you choose  ' + player + '  computer choose  ' + word)
         print('computer win')   
          
    elif player == 'scissors' and word == 'paper':
         print('you choose  ' + player + '  computer choose  ' + word)
         print('player win')
             
    elif player == 'paper' and word == 'rock':
         print('you choose  ' + player + '  computer choose  ' + word)
         print('player win')    
         
    elif player == 'rock' and word == 'paper':
         print('you choose  ' + player + '  computer choose  ' + word)
         print('computer win') 
    elif player == word:
          print('you choose  ' + player + '  computer choose  ' + word)
          print('draw')      
    else:
        print('please enter a word from the list')        

            
loop()
    
