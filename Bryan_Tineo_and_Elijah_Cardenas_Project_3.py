def Display_CostummerMeters(beginning_meter, ending_meter):

    #Check how many digits the meter has
    num_char_b_meter = len(str(beginning_meter))
    num_char_e_meter = len(str(ending_meter))

    # if less than two digits, then print with nine 0s infront
    if num_char_b_meter < 2:
        beginning_meter = "{:0>9}".format(beginning_meter)

    if num_char_e_meter < 2:
        ending_meter = "{:0>9}".format(ending_meter)

    print(f"Beginning meter reading: {beginning_meter}")
    print(f"Ending meter reading:    {ending_meter}")


def calculate_Bill_depending_on_Code(code, water_usage, beginning_meter, ending_meter):

    #Check code and bill depending on the code. If the code is not there, don't execute any calculation
    if code == "r" or code == "R":
        bill = 5
        per_gallon = (water_usage * 0.0005)
        per_gallon_rounded = round(per_gallon, 2)
        bill += per_gallon_rounded
        bill = "{:.2f}".format(bill)
        return bill

    if code == "c" or code == "C":
        bill = 1000

        change_first_digits_ending_meter = ending_meter + 100000000
        gallons_used_in_millions = change_first_digits_ending_meter - beginning_meter

        if gallons_used_in_millions >= 4000000: #calculate usage if 4000000 is exceded
            substract_4000000 = (gallons_used_in_millions - 4000000) #get gallons used after 4000000 is exceded
            per_gallon = (substract_4000000* 0.00025)
            per_gallon_rounded = round(per_gallon, 2)
            bill += per_gallon_rounded
            bill = "{:.2f}".format(bill)
            return bill
                
        else:
            bill = "{:.2f}".format(bill)
            return bill

    if code == "i" or code == "I":
        bill = 1000.00
        return bill
    


def calculateWaterUsage(beginning_meter, ending_meter):

    # this is to check if meter needs is near to reset
    check_first_4_dig_b = beginning_meter//100000 
    check_first_4_dig_e = ending_meter//100000

    #if it dosent need to reset
    if check_first_4_dig_b == check_first_4_dig_e: 
        water_usage = (ending_meter - beginning_meter)/10
        return water_usage

    # reset beginning meter
    elif check_first_4_dig_b > check_first_4_dig_e:
        reset = 1000000000 - beginning_meter
        beginning_meter_reseted = 0 # reset the gratest reading meter
        add_ending = ending_meter + reset # add what you added to reset the first meter
        water_usage = (add_ending - beginning_meter_reseted)/10
        return water_usage

    # reset ending meter
    elif check_first_4_dig_b < check_first_4_dig_e:
        reset = 1000000000 - ending_meter
        ending_meter_reseted = 0 # reset the gratest reading meter
        add_beginning_meter = beginning_meter + reset # add what you added to reset the first meter
        water_usage = (add_ending - beginning_meter_reseted)/10
        return water_usage
    

def validity_Meter2(ending_meter):

    if not(0 <= int(ending_meter) <= 999999999): #if not in range, false.
        return False
    else:
        return True

def loop4Meter2():
    m = True #while loop controller for meter2
    while m:
        ending_meter = int(input("Enter the customer's ending meter reading:    "))

        validity = validity_Meter2(ending_meter)

        if validity == True:
            m = False 
            return ending_meter
        else:
            print("Error, invalid meter. Try again.")
            continue
        

def validity_Meter1(beginning_meter):
    
    if not(0 <= int(beginning_meter) <= 999999999): #if the meter is not under the range it will return false. else is True
        return False
    else:
        return True
    
def loop4Meter1():
    m = True #while loop controller for meter1
    while m:
        beginning_meter = int(input("Enter the customer's beginning meter reading: "))
        
        validity = validity_Meter1(beginning_meter)

        if validity == True:
            m = False
            return beginning_meter
        else:
            print("Error, invalid meter. Try again.")
            continue

def loop4Code():
    c = True #while loop controller for codes
    while c:
        code = input("Enter the customer's code: ")
        
        validity = validityCode(code) #identify if code exists
        
        if validity == True:
            c = False
            return code
        else:
            print("Error, invalid code. Try again.")
            continue
    
def validityCode(code):
    #dictionary
    codes = {"r": "residential", "c":"commercial", "i":"industrial", "R":"Residential", "C": "Commercial", "I":"Industrial"}
    #Check if the code is under the library
    if code in codes:
        return True
    else:
        return False

def main():

    code = loop4Code() #these function determines if the code given by the user is correct
    beginning_meter = loop4Meter1() # these function determines if the meter given is in the range
    ending_meter = loop4Meter2() # These does the same as the loop for meter 1
    
    water_usage = calculateWaterUsage(beginning_meter, ending_meter) # function to calculate water usage

    bill = calculate_Bill_depending_on_Code(code, water_usage, beginning_meter, ending_meter) # these function will calculate the bill depending on the code of the user

    print(f"\nCustomer code: {code}")
    
    Display_CostummerMeters(beginning_meter, ending_meter) #these will display the meters
    
    print(f"Gallons of water used: {water_usage}")
    print(f"Amount billed: ${bill}")

    
    

           

# The main application, where the executions start.
if __name__ == "__main__":
    Start = True # Controls wether the main(), the program, hass to be repeated or not
    
    while Start == True:
        main()

        again = True # These controls wether the user wants to execute the program again

        while again == True:
            Try_again = input("Do you want to Perform a new Calculation? Yes == y or No == n: ")

            if Try_again == "y" or Try_again == "Y": # exit "again loop" and make a new calculation
                again = False
                
            elif Try_again == "n" or Try_again =="N": # Exit the program
                Start = False
                break
            else:
                print("Sorry I didn't understand you.")
                continue  #if the user dosent type y or n ask again.
            
        
    
