# Create a parking garage class to give tickets upon entry and payment when leaving
# limited parking spots (keep track of spaces)
# different prices for different times - extra credit?
# payment upon leaving (increases parking spaces left by 1)

# create a dictionary of available parking spaces
# create an empty dictionary of current parking tickets given out
# if, elif, else loop for input options from user.
# What are the functions we need? 
#   Give a ticket (add to the ticket dictionary and remove from the available dictionary)(decrease amount of tickets by 1)
#   Show spaces left
#   Pay upon leaving garage (remove from ticket dictionary and add to available dictionary) -change variable to 'paid'
#   Leave parking garage that checks if they've paid [variable='paid'](print thank you message)
#   Input loop function


# dictionary of tickets available
available = { 
        1:"unpaid",
        2:"unpaid",
        3:"unpaid",
        4:"unpaid",
        5:"unpaid",
        6:"unpaid",
        7:"unpaid",
        8:"unpaid",
        9:"unpaid",
        10:"unpaid"
}

garage = {} # dictionary of spaces in the garage taken



class Parking():
    
      # Define the inputs
        # 1st: response = Take Ticket/Show/Pay/Leave
        # 2nd: payment = to pay (i.e. press any key to pay)
        # 3rd: Ticket Number = Input ticket number
        # 4th: Show Ticket = Show ticket to leave

    def show_spaces(self):
        
        print("Parking Spaces Left:")
        if available:
            print(len(available))
            
        else:
            print("Sorry! No Parking Spaces Available. \n Please come back when parking is available!")
        # now have to assign variables 'spaces' and 'garage'

    def take_ticket(self):
        
        
        # give next ticket in line (range(len)) bullshit?        
        #   remove ticket from available
        #   add ticket to garage
        #   subtract 1 from spaces
        # access the first position in a list [0]
        ticket = list(available)[0]
        garage.update({ticket:available[ticket]})        
        del available[ticket]
        print(f'Your ticket is #{ticket}')
        
    def pay_ticket(self):
        # input the ticket
        
        while True:
            ticket_number_response = int(input("What is your ticket #?\n '0' to quit\n "))
            if ticket_number_response == 0:
                break
            elif ticket_number_response in garage.keys():
                confirm = input(f'Your ticket # is {ticket_number_response} is that correct? Y/N ')
                while True:
                    if confirm.lower() == 'y':
                        payment = input('Your total is $15\nDebit or Credit?\n')
                        if payment.lower() == 'debit' or payment.lower() == 'credit':
                            garage[ticket_number_response] = 'Paid'
                            print("Thank you for your payment")
                            break
                    elif confirm.lower() == 'n':
                        break
                    else:
                        print("Invalid Response, Try Again")
            else:
                print("Invalid Response, Try Again")


    def leave_garage(self):
        
        # this function needs to: check if paid, if paid leave a thank you message
        # if paid remove ticket from garage and add to available
        # if not paid, ask to pay
            #if response = leave do what?
        
        while True:
            show_ticket = int(input("Type '0' to quit\nShow your ticket number: "))
            if show_ticket == 0: 
                break
            elif garage.get(show_ticket) == 'Paid':
                print("Thank you for Parking with us.\n Have a great day!")
                garage[show_ticket] = "unpaid"
                available.update({int(show_ticket):garage[show_ticket]})
                
                del garage[show_ticket]
                break
            elif garage.get(show_ticket) == 'unpaid':
                print("Please pay your ticket before leaving")
                
                
            else:
                print("Invalid Response, Try Again")
                

    # UI
    def ui(self):
        while True:
            response = input("What would you like to do?\n 'Show Spaces'/'Take Ticket'/'Pay Ticket'/'Leave'/'Quit'\n")
            if response.lower() == 'quit':
                print("Please visit our garage again!")
                break
            elif response.lower() == 'show spaces':
                self.show_spaces()
            elif response.lower() == 'take ticket':
                self.take_ticket()
            elif response.lower() == 'pay ticket':
                self.pay_ticket()
            elif response.lower() == 'leave':
                self.leave_garage()
            else:
                print("Invalid Response, Try Again")

        #     ticket = list(available)[0]
        # garage.update({ticket:available[ticket]})        
        # del available[ticket]



run = Parking()
run.ui()      









