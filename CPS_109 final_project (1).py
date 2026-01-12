"""
The problem is to determine whether a planned multi-destination trip can be completed
within a fixed financial budget. Each destination in the trip has several associated
expenses, including transportation, accommodation, food, and entertainment. Because
these costs can vary across destinations, travelers often need a systematic way to
calculate the total projected trip cost and compare it against their available funds.

This program must accurately compute the total and individual expenses across all 
destinations and report whether the traveler’s total spending stays within the budget,
exceeds it, or matches it exactly. If it exceeds it, then it will tell the user that 
the expenses exceed their current budget. If it matches it, then it will say to the user 
that it is just enough for their trip. Lastly, if it's within the budget, it will tell the 
user GO RIGHT AWAY FOR THAT TRIP!!!."""



def budget_calculator():
    
    """Here we are just defining our variable and asking the user for their budget"""
    
    print("Welcome to the Travel budget planner!")
    budget= float(input("Enter your total budget ($): "))
    destinations_list=[]
    destination_costs={}
    subtotal=0
    
    while True:                                                          # We create a while True loop for the user to input as much information as they want. 
        print("\n Enter the information of your destination")                          
        
        name= input("Enter the name of your destination: ")              # These are the inputs(expenses) our program will us to calculate our total from.
        transportation = float(input("Transportation cost($): "))               
        accommodation= float(input("accommodation cost($): "))
        food= float(input("food cost ($): "))
        entertainment= float(input("entertainment cost ($): "))
        
        destination_costs= { "name": name, "transportation" : transportation, "accommodation": accommodation, "food":food, "entertainment": entertainment}    # We store each destination name and the costs associated to that trip in a dictionary       
        
        destinations_list.append(destination_costs)                            # We append our expenses to our destination_list for further use.
    
        another_destination= input("add another destination (y/n): ").lower() # Here, we are asking the user to input the information of another destination to our dictionary.
    
        if another_destination !="y":               # If the user inputs "y" then it will break the loop. Otherwise it will ask the user for information about their other trip.
           break
    total= calculate_total(destinations_list)       # Here we are calling the total from our function calculate_total where you get the total cost of all our trips.
    trip_summary(destinations_list,total,budget)    # This calls the function trip_summary for creating a text file with all our destination expenses, our budget and the final total.
    
    print("\n-------Trip summary-------")
    print(f"Budget: ${budget:.2f}")
    print(f" Total_trip_expenses = ${total:.2f}")  # Here we are rounding our  total to two decimal places
    
    for i in destinations_list:
        
        subtotal= i["transportation"]+ i["accommodation"]+ i["food"]+ i["entertainment"] # We are writting the individual cost of our trip expenses on our text file. In this way: name- $expenses.
        print(f"{i['name']}- ${subtotal:.2f}\n")                                         # this will print the individual cost of our trip expenses on the console.
                
    
    
    """These are the possible outputs, they will be shown depending on the user budget 
       and the final total."""
   
    if total>budget:
        print(f" You are over the budget by ${total- budget:.2f}. Try to cut some expenses or try with a higher budget")
    
    elif total==budget:
        print ("Perfect, you are exactly on budget")
    
    else:
        print(f"GO RIGHT AWAY FOR THAT TRIP!!!, you are under budget by ${budget-total:.2f}.")
    
    
"""We use the function calulate_total to iterate over the cost of each destination and create a final total."""

def calculate_total (destinations_list):
               
           total=0
               
           for i in destinations_list:
                   
                   total+= i["transportation"]+ i["accommodation"]+ i["food"]+ i["entertainment"]  # we sum up the total of all our expenses, iterating on each of the given expenses. 
                   
           return total                                                                            #return the combine total of all the expenses of our destinations.
       
       
"""This function will write down all our destinations with all their total, and individual expenses included.
 and if our budget is enough for that."""
 
def trip_summary (destinations_list, total, budget):
        
        with open("Trip_summary_expenses.txt", "w") as trip:            # We open a text file and we write our total expenses on it
            trip.write ("Travel Budget Summary\n")                      # This is the header of our text file
            
            for i in destinations_list:
                
                subtotal= i["transportation"]+ i["accommodation"]+ i["food"]+ i["entertainment"] 
                trip.write (f"{i['name']}-${subtotal:.2f}\n" )          # We are writting the individual cost of our trip expenses on our text file. In this way: name- $expenses. 
                
            trip.write("\n  \n")                                        #It's just a space line in our text for reading clarity
            
            trip.write(f"Total trip cost: ${total:.2f}\n")              # Here, we are doing the same for our subtotal as in our main function, but we are writting it in our file
            trip.write(f" Budget: ${budget:.2f}\n")                     # Just writting our budget on our text file
            
            
            """ This part just check if the total expenses are equal, less or more than our budget. 
                If any of the conditions are True then it will write down the output on our text file. 
                The same logic we applied on our main function"""
                
            if total>budget:
                trip.write(f"Your expenses exceeds your current budget by ${ total- budget :.2f}\n")
                
            elif total== budget:
                trip.write("Exactly on budget\n")
                
            else:
                trip.write(f" GO RIGHT AWAY FOR THAT TRIP!!!, you under budget by ${budget-total:.2f}\n")
                
budget_calculator() #Here we are calling our main function to run all the program
