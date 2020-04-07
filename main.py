import random

FAST_FIVE = "Fast Five"
TOP_LINE = "Top Line"
MIDDLE_LINE = "Middle Line"
BOTTOM_LINE = "Bottom Line"
FULL_HOUSE = "Full House"

def generate_ticket():
    
    print()
    ticket = [sorted(random.sample(range(1+(33*x), 33+(33*x+1)), 5)) for x in range(3)]
            
    # This will show the ticket in Housie format
    for e in ticket:
        print('|', '|'.join(map(str, e)), '|', sep='')
        print()
    
    # This will show the ticket for computing
    marked_ticket = []
    for index,line in enumerate(ticket):
        for number in line:
            marked_ticket.append([index, number, False])
    return marked_ticket 
     
def board_display(prev_numbers):
    board = range(0, 100)
    curr_num = prev_numbers[-1]
    chunks = [board[x*10:(x*10)+10] for x in range(0, 10)]
    
    for chunk in chunks:
        print("|",end="")
        for num in chunk:
            if num+1 in prev_numbers:
                if num+1 == curr_num:
                    print("({:02d})|".format(num+1),end="")
                else:
                    print(" {:02d} |".format(num+1),end="")
            else:
                print("    |",end="")
        print()
        print()

def main():
    print()
    print("**Welcome to the Game of Housie***")
    
    ticket_price = int(input("Please enter the price per ticket in £: "))    
    num_of_players = int(input("Please enter number of players: "))
    
    
    player_num_of_tickets = {}
    
    while len(player_num_of_tickets.keys()) < num_of_players:
        for i in range(num_of_players):
            player = input("Please enter the name of player number " + str(i+1) + '- ')
            no_of_tickets = input("How many tickets do you want {0}? ".format(player))
            player_num_of_tickets[player] = int(no_of_tickets)
        
    
    
    total_pot = sum(player_num_of_tickets.values()) * ticket_price
    print()
    print("Total pot for this game is: £{0}".format(total_pot))
    
    benchmarks = {FAST_FIVE:0.1, TOP_LINE:0.15, MIDDLE_LINE:0.15, BOTTOM_LINE:0.15, FULL_HOUSE:0.45}
    benchmarks_Prize = {}
    benchmarks_Winner = {}
    print()  
    print("Winnings for this game are as follows:")
    print() 
    
    for game,percent in benchmarks.items():
        benchmarks_Prize[game] = round(percent*total_pot, 2)
        print("{0} - £{1}".format(game, benchmarks_Prize[game]))
        print() 
        
    player_tickets = {}
        
    for player,tickets in player_num_of_tickets.items():
        print("{0} here are your tickets: ".format(player))
        print()
        for i in range(tickets):
            ticket = generate_ticket()
            if player in player_tickets:
                player_tickets[player].append(ticket)
            else:
                player_tickets[player] = [ticket]
            print()
            print()
           
    print("Let's play HOUSIE!!!")
    print()
    
    output_numbers = random.sample(range(1, 100), 99)
    prev_numbers = []
    
    for number in output_numbers:
        # print(number)
        prev_numbers.append(number)
        board_display(prev_numbers)
        mark_tickets(prev_numbers[-1], player_tickets)
        # print(player_tickets)
        
        # check winner for Fast Five
        for benchmark in benchmarks_Prize:
            if(benchmark == FAST_FIVE):
                if(benchmark not in benchmarks_Winner):
                    winner = fast_five(player_tickets)
                    if(winner):
                        benchmarks_Winner[FAST_FIVE] = winner
            else:
                if benchmark not in benchmarks_Winner:
                    winner = row_winner(player_tickets, benchmark)
                    if(winner):
                        benchmarks_Winner[benchmark] = winner
                        if benchmark == FULL_HOUSE:
                            print("Game is over")
                            break
                        
        if FULL_HOUSE in benchmarks_Winner.keys():
            #print("I SAID Game is over")
            break;
        else:
            input()
        
    print("Results:-")
    #print(player_tickets)    
    print(benchmarks_Winner)
    print()
    print('Amount won:-')
    print(benchmarks_Prize)

def mark_tickets(curr_num, player_tickets):
    for player,tickets in player_tickets.items():
        for ticket in tickets:
            for item in ticket:
                if(item[1] == curr_num):
                    item[2] = True
                                                
def fast_five(player_tickets):
    for player,tickets in player_tickets.items():
        for index,ticket in enumerate(tickets):
            count = 0
            for item in ticket:
                if(item[2]):
                    count += 1
                    if(count == 5):
                        print("{0} is the winner of Fast Five for ticket number {1}!!".format(player, index+1))
                        print(ticket)
                        # break
                        return player
        
def row_winner(player_tickets, benchmark):    
    for player,tickets in player_tickets.items():        
        for index,ticket in enumerate(tickets): 
            
            flag = False
            numbers = []
            if benchmark == TOP_LINE:
                numbers = ticket[0:5]
            elif benchmark == MIDDLE_LINE:
                numbers = ticket[5:10]
            elif benchmark == BOTTOM_LINE:
                numbers = ticket[10:15]
            else:
                numbers = ticket[0:15]
                
            for item in numbers:                
                if item[2] == False:
                    flag = True;
                    break;
            
            if flag == False:
                print("{0} is the winner of {2} for ticket number {1}!!".format(player, index+1, benchmark))
                print(ticket)
                return player          

   
    
main()
# print(generate_ticket())
# board_display([1,34])

