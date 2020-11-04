TICKET_PRICE = 10
import math
tickets_remaining = 100
print('There are {} remaining.'.format(tickets_remaining))

name = input('What is your name? ')
number_of_tickets = float(input('How many tickets do you want {}? '.format(name)))

def cost_of_tickets(number_of_tickets):
    return math.ceil(TICKET_PRICE*number_of_tickets)
cost = cost_of_tickets(number_of_tickets)
print('For {} tickets the cost is ${}'.format(number_of_tickets,cost))
