# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 18:40:49 2020

@author: G&S
"""
player_tickets = {'g': [
                        [[0, 9, False], [0, 25, False], [0, 2, False], [0, 29, False], [0, 7, False], 
                         [1, 59, False], [1, 43, True], [1, 52, False], [1, 47, False], [1, 56, False], 
                         [2, 74, True], [2, 64, True], [2, 78, True], [2, 84, True], [2, 82, True]],
                        
                        [[0, 12, True], [0, 24, True], [0, 14, True], [0, 16, True], [0, 21, True], 
                         [1, 33, False], [1, 41, False], [1, 51, False], [1, 32, False], [1, 45, False], 
                         [2, 85, False], [2, 92, False], [2, 89, False], [2, 91, False], [2, 75, False]]], 
    
                 's': [[[0, 15, False], [0, 21, False], [0, 17, False], [0, 18, False], [0, 6, False], 
                        [1, 58, False], [1, 34, False], [1, 39, False], [1, 59, False], [1, 33, False], 
                        [2, 94, False], [2, 76, False], [2, 89, False], [2, 95, False], [2, 91, False]], 
                       
                       [[0, 7, False], [0, 28, False], [0, 5, False], [0, 19, False], [0, 9, False], 
                        [1, 32, True], [1, 51, True], [1, 42, True], [1, 55, True], [1, 47, True], 
                        [2, 79, False], [2, 90, False], [2, 72, False], [2, 91, False], [2, 96, False]]]}
xyz = 'BOTTOM_LINE'

def row_winner(player_tickets, benchmark):    
    for player,tickets in player_tickets.items():        
        for index,ticket in enumerate(tickets): 
            
            flag = False
            numbers = []
            if benchmark == 'TOP_LINE':
                numbers = ticket[0:5]
            elif benchmark == 'MIDDLE_LINE':
                numbers = ticket[5:10]
            elif benchmark == 'BOTTOM_LINE':
                numbers = ticket[10:15]
            else:
                numbers = ticket[0:15]
                
            for item in numbers:                
                if item[2] == False:
                    flag = True;
                    break;
            
            if flag == False:
                print("{0} is the winner of {2} for ticket number {1}!!".format(player, index+1, benchmark))
                #print(ticket)
                return player    
                


print(row_winner(player_tickets, xyz))