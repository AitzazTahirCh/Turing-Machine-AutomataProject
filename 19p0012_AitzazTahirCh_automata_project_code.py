string = input("Enter String: ")
length = len(string) + 2
tape = ['B']*length
i = 1
tapehead = 1
for s in string: #loop to place string in tape
    tape[i] = s
    i += 1

state = 0
#assigning characters to variable so that don't have to use characters each time
X, Y, S, B, R, L = 'X', 'Y', 'S', 'B', 'R', 'L' 
oldtapehead = -1
accept = False

def action(input_char, replace_with, move, new_state):
    global tapehead, state
    if tape[tapehead] == input_char:
        tape[tapehead] = replace_with
        state = new_state
        if move == 'L':
            tapehead -= 1
            return True
        elif move == 'R':
            tapehead += 1
            return True
    return False

while(oldtapehead != tapehead): #if tapehead not moving that means terminate Turing machine
    oldtapehead = tapehead
    print(tape , "with tapehead at index", tapehead, "on state" , state)
    
    if state == 0:
        if action('0', X, R, 1) or action('1', Y, R, 1) or action(Y, Y, L, 4) or action(X, X, L, 4):
            pass
        
    elif state == 1:
        if action('1', '1', R, 1) or action('0', '0', R, 1) or action(Y, Y, L, 2) or action(X, X, L, 2) or action(B, B, L, 2):
            pass
        
    elif state == 2:
        if action('0', X, L, 3) or action('1', Y, L, 3):
            pass
            
    elif state == 3:
        if action('1', '1', L, 3) or action('0', '0', L, 3) or action(X, X, R, 0) or action(Y, Y, R, 0):
            pass
    
    elif state == 4:
        if action(X, '0', L, 4) or action(Y, '1', L, 4) or action(B, B, R, 5):
            pass
        
    elif state == 5:
        if action(B, B, L, 9) or action('0', X, R, 6) or action('1', Y, R, 7):
            pass
            
    elif state == 6:
        if action('1', '1', R, 6) or action('0', '0', R, 6) or action(B, B, R, 6) or action(X, B, L, 8):
            pass
            
    elif state == 7:
        if action('1', '1', R, 7) or action('0', '0', R, 7) or action(B, B, R, 7) or action(Y, B, L, 8):
            pass
            
    elif state == 8:
        if action('1', '1', L, 8) or action('0', '0', L, 8) or action(B, B, L, 8) or action(X, X, R, 5) or action(Y, Y, R, 5):
            pass        
    
    elif state == 9:
        accept = True

    else:
        accept = True
        
            
if accept:
    print("String accepted on state = ", state)
else:
    print("String not accepted on state = ", state)