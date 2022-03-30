def root_suma(user): #Does the same thing as the function called "suma"
    continuar = True
    
    while continuar:
        product = additive_loop(user)
        
        if len(str(product)) == 1:
            break
        if len(str(product)) > 1:
            user = product
            
    return product



def root_multiplicacion(user): #Does the same thing as the function called "multiplicacion"
    continuar = True
    
    while continuar:
        
        product = multiplicative_loop(user)
        
        if len(str(product)) == 1:
            break
        if len(str(product)) > 1:
            user = product
    return product
    
def additive_loop(user):
    add = 0
    while not(user == 0):
        add += user % 10 #<-- this helps get each digit and add to each other
        user //= 10
    return add

def suma(user):
    continuar = True
    perseistence_sum = 0
    
    while continuar:
        product = additive_loop(user)
        #print("sum: {}".format(product)) <-- Diagnostic output (erase the "#" to print it)
        perseistence_sum += 1
        
        if len(str(product)) == 1: # Check if one digit so we can exit the loop
            break
        if len(str(product)) > 1: # if not one digit continue iterating using the product we got
            user = product
            
    return perseistence_sum

def muliplicacion(user):
    continuar = True # <--- loop remote
    perseistence_multiplicative = 0 
    
    while continuar:
        
        product = multiplicative_loop(user) # <-- here we get our product for each iteration
        #print("product: {}".format(product)) <-- Diagnostic output (erase the "#" to print it)
        perseistence_multiplicative += 1    # <-- add for each iteration
        
        if len(str(product)) == 1: # Check if one digit so we can exit the loop
            break
        if len(str(product)) > 1: # if not one digit continue iterating using the product we got
            user = product
    return perseistence_multiplicative



def multiplicative_loop(user):
    multiply = 1
    while not(user == 0):
        multiply *= user % 10 #<-- this helps get each digit and multiply to each other
        user //= 10
    return multiply
        

def negative_exit(user_integer):
    if user_integer < 0: # if is negative is False
        return False
    if user_integer > 0: # if non-negative is True
        return True
        

def main(user_integer): # <-- We enter to the main program only if user input is non-negative
    
    if len(str(user_integer)) == 1: # check if the user imputs a 1 digit integer, if so the persistence is 0 for both cases and the root for both cases would be the input itself
        multiplication_persistence = 0
        multiplication_Root = user_integer

        Additive_persistence = 0
        Additive_Root = user_integer

        print("                Additive Persistence: {}, Additive Root: {}".format(Additive_persistence, Additive_Root))
        print("                Multiplicative Persistence: {}, Multiplicative Root: {}".format(multiplication_persistence, multiplication_Root))
        print()

    else:
        user = user_integer
        
        #print("\nMultiplicative loop") <-- Diagnostic output (erase the "#" to print it)
        multiplication_persistence = muliplicacion(user) # <---- find the persistence of the multiplication
        multiplication_Root = root_multiplicacion(user)  # <---- find the root of the multiplication

        #print("\nAdditive loop") <-- Diagnostic output (erase the "#" to print it)
        Additive_persistence = suma(user) # <----find the persistence of the sum
        Additive_Root = root_suma(user)   # <----find the root of the sum

        print("\nFor the integer: {}".format(user))
        print("                Additive Persistence: {}, Additive Root: {}".format(Additive_persistence, Additive_Root))
        print("                Multiplicative Persistence: {}, Multiplicative Root: {}".format(multiplication_persistence, multiplication_Root))
        print()
    
    

if __name__ == '__main__': #As i said in previous Projects, This is "just" to reference were the code starts. Here we are executing the loop if the user inputs a negative integer
    remote = True   #this controls the loop. I like to call it remote like how remotes are used for tv's to turn on or off a TV.  LOL
    while remote:
        user_integer = int(input("Please enter an integer (negative integer to quit): "))
        remote = negative_exit(user_integer) #identifies if the input is negative or not
        if remote == False: # this is if statement exits the loop and terminates the program
            print("Thanks for playing with numbers...Goodbye")
            break
        if remote == True: # if is not negative we execute the main program. Here we just entered the program
            main(user_integer)
        
