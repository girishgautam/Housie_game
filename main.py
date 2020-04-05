# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:55:47 2020

@author: G&S
"""
import random
import Colour




def generateTicket():
    ticket_numbers = random.sample(range(1, 100), 15)
    # print(ticket_numbers)
    ticket = [ticket_numbers[0:5],ticket_numbers[5:10],ticket_numbers[10:15]]
    # print(ticket[1][3])
    for line in ticket:
        print("|",end="")
        for number in line:
            print(" {:02d} |".format(number),end="")
        print()
        print()
        
def board_display(prev_numbers):
    board = range(0, 100)
    curr_num = prev_numbers[-1]
    chunks = [board[x*10:(x*10)+10] for x in range(0, 10)]
    for chunk in chunks:
        print("|",end="")
        for num in chunk:
            if num+1 in prev_numbers:
                if num+1 == curr_num:
                    print(Colour.color.BOLD + " {:02d} |".format(num+1),end="" + Colour.color.END)
                else:
                    print(" {:02d} |".format(num+1),end="")
            else:
                print("    |",end="")
        print()
        print()


def main():
    
    print("**Welcome to the Game of Housie***")
    
    ticketPrice = int(input("Enter the price per ticket in £:"))
    
    noOfPlayers = int(input("Enter number of players: "))
    # print(noOfPlayers)
    print("Enter their names:")
    
    player_tickets = {}
    while len(player_tickets.keys()) < noOfPlayers:
        player = input()
        noOfTickets = input("How many tickets do you want {0}?".format(player))
        player_tickets[player] = int(noOfTickets)
        
    # print(player_tickets)
    
    totalPot = sum(player_tickets.values()) * ticketPrice
    
    print("Total pot is: £{0}".format(totalPot))
    
    benchmarks = {"Fast Five":0.1,"Top Line":0.15,"Middle Line":0.15,"Bottom Line":0.15,"Full House":0.45}
      
    print("Winnings for the games are as follows:")
    
    for game,percent in benchmarks.items():
        print("{0} - £{1}".format(game, percent*totalPot))
        
    for player,tickets in player_tickets.items():
        print("{0} here are your tickets: ".format(player))
        for i in range(tickets):
            generateTicket()
            print()
            print()
            
    print("Let's start playing Housie!!")
    print()
    
    output_numbers = random.sample(range(1, 100), 99)
    prev_numbers = []
    
    for number in output_numbers:
        # print(number)
        prev_numbers.append(number)
        board_display(prev_numbers)
        input()
                    
    
main()
# generateTicket()
# board_display([1,34])
        
print(Colour.color.BLUE + 'Hello World !' + Colour.color.END)


