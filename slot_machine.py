import random
import time

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 10

ROWS = 3
COLS = 3

Symbols_count = {
    '🍒':9,
    '🍉':8,
    '🍌':7,
    '🔔':6,
    '💲':4
}

Symbols_values = {
    '🍒':2,
    '🍉':4,
    '🍌':6,
    '🔔':8,
    '💲':10
}


def check_win(columns,lines,bet,values):
    winnings =0
    win_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol!=symbol_to_check :
                break
        else:                   #this is implimentation of for else loop,where if we use a break in a if statement inside a for loop we use else outside the loop as if loop breaks,else will direcly execute
            winnings += values[symbol]*bet
            win_line.append(line+1)
    return winnings,win_line

def slot_spin(rows,cols,Symbols):
    all_symbols = []
    for symbols,symbols_count in Symbols.items():
        for _ in range(symbols_count): # here '_' is used as place holder since we don't need a counter or index
            all_symbols.append(symbols)
    columns = []
    for _ in range(cols):
        column = []
        curr_symbols = all_symbols[:] # here [:] is a slicing operation used here to copy the list,if we dont use it than curr_symbols will remain a refrence variable to object of all-symbols not a separate copy object
        for _ in range(rows):
            value = random.choice(curr_symbols)
            curr_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def slop_print(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):#enumerate makes the list iterate through both index and calue
            if(i!=len(column)-1):
                print(column[row],end ="|")
            else:
                print(column[row],end ="")
        print()

def deposit():
    while(True):
        amount = input("Enter the amount to deposit in $: ")
        try:
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a number.")
            continue

    return amount

def get_number_of_lines():
    while(True):
        lines = input("Enter the lines to bet on (1-"+ str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("The lines must be valid")
        else:
            print("Please enter a valid number of lines")
    return lines

def place_bet():
    while(True):
        bet = input("Enter the amount you want to bet each line: ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET<=bet<=MAX_BET:
                break
            else:
                print(f"Bet amount must be between ${MIN_BET}-{MAX_BET}.")
        else:
            print("Enter a valid number.")
    return bet

def bet_conf(total):
    while(True):
        flag = input("DO YOU CONFIRM (y/n)?: ")
        if flag == 'y':
            print(f"Placing bet of ${total}...")
            time.sleep(1)
            break
        elif flag == 'n':
            print(f"Please re-check and re-enter")
            print()
            starter()
            break
        else:
            print("please take this Seriously!!")

def game(balance):
    lines = get_number_of_lines()
    bet = place_bet()
    while(True):
        total_bet = bet*lines
        if total_bet>balance :
            print(f"You can't bet,your total bet amount ${total_bet} exceeds your balance ${SlotBalance} ")
        else:
            break
    print(f"You are betting ${bet} on each of {lines} lines,total bet is ${total_bet}")
    bet_conf(total_bet)
    slots = slot_spin(ROWS,COLS,Symbols_count)
    slop_print(slots)

    winnings,win_line = check_win(slots,lines,bet,Symbols_values)
    print(f"you won ${winnings}")
    print(f"you won in lines:",*win_line) # '*'  this is splat or unpack operator that prints every single line in win_line list
    return winnings-total_bet

def starter():
    SlotBalance = deposit()
    while True:
        print(f"current balance is ${SlotBalance}")
        spin = input("Press enter to play the game (q to quit and a to add balance)")
        if spin == 'q':
            break
        if spin =='a':
            add = input("How much money do you want to add in $: ")
            SlotBalance+=int(add)
            print(f"Your current balnace is ${SlotBalance}")
            continue
        SlotBalance+=game(SlotBalance)
   

def main():
    print("***************************")
    print("Welcome to MY SLot Machine")
    print("Symbols: 🍒 🍉 🍌 🔔 💲 ")
    print("***************************")
    starter()
    
if __name__ == "__main__":
    main()
