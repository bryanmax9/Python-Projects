
code = input("Enter the customer's code: ")
beginning_meter = int(input("Enter the customer's beginning meter reading: "))
ending_meter = int(input("The customer's ending meter reading:          "))


#dictionary in order to check if code is correct
codes = {"r": "residential", "c": "commercial", "i":"industrial", "R":"Residential", "C": "Commercial", "I":"Industrial"}


#check if the code input is correct.if so, calculate water usage
if code in codes:
    
    check_first_4_dig_b = beginning_meter//100000 # this is to check if meter needs is near to reset
    check_first_4_dig_e = ending_meter//100000
    
    if check_first_4_dig_b == check_first_4_dig_e:
        water_usage = (ending_meter - beginning_meter)/10
        
        
    elif check_first_4_dig_b > check_first_4_dig_e:# reset meter
        reset = 1000000000 - beginning_meter
        beginning_meter_reseted = 0 # reset the gratest reading meter
        add_ending = ending_meter + reset # add what you added to reset the first meter
        water_usage = (add_ending - beginning_meter_reseted)/10
        
    elif check_first_4_dig_b < check_first_4_dig_e:# reset meter
        reset = 1000000000 - ending_meter
        ending_meter_reseted = 0 # reset the gratest reading meter
        add_beginning_meter = beginning_meter + reset # add what you added to reset the first meter
        water_usage = (add_ending - beginning_meter_reseted)/10

#Check code and bill depending of the code. If the code is not ther, dont execute any calculation
if code == "r" or code == "R":
    bill = 5
    per_gallon = (water_usage * 0.0005)
    per_gallon_rounded = round(per_gallon, 2)
    bill += per_gallon_rounded
    bill = "{:.2f}".format(bill)
    
if code == "c" or code == "C":
    bill = 1000
    
    if check_first_4_dig_b == check_first_4_dig_e: #when meter is not reset
        change_first_digits_ending_meter = ending_meter + 100000000
        gallons_used_in_millions = change_first_digits_ending_meter - beginning_meter
        
        if gallons_used_in_millions >= 4000000: #calculate usage if 4000000 is exceded
            substract_4000000 = (gallons_used_in_millions - 4000000) #get gallons used after 4000000 is exceded
            per_gallon = (substract_4000000* 0.00025)
            per_gallon_rounded = round(per_gallon, 2)
            bill += per_gallon_rounded
            bill = "{:.2f}".format(bill)
            
    elif check_first_4_dig_b > check_first_4_dig_e: #when meter is reset
        change_first_digits_ending_meter = add_ending + 100000000
        gallons_used_in_millions = change_first_digits_ending_meter - beginning_meter_reseted

        if gallons_used_in_millions <= 4000000: #calculate usage if 4000000 is exceded
            substract_4000000 = (gallons_used_in_millions - 4000000) #get gallons used after 4000000 is exceded
            per_gallon = (substract_4000000* 0.00025)
            per_gallon_rounded = round(per_gallon, 2)
            bill += per_gallon_rounded
            bill = "{:.2f}".format(bill)

    bill = "{:.2f}".format(bill)
            

if code == "i" or code == "I":
    bill = 1000
    
print(f"\nCustomer code: {code}")


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

if not(code in codes):
    water_usage = "{:.1f}".format(0)
    bill = "{:.2f}".format(0)
    print("invalid Entry")

if not(0 <= int(beginning_meter) <= 999999999) or not(0 <= int(ending_meter) <= 999999999): #if meter not in range
    water_usage = "{:.1f}".format(0)
    bill = "{:.2f}".format(0)
    print("invalid Entry")
    
    

print(f"Gallons of water used: {water_usage}")
print(f"Amount billed: ${bill}")


    
        
        



