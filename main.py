import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbolcount = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbolvalues = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def getslotmachinespin(rows, cols, symbols):
    allsymbols = []
    for symbol, symbolcount in symbols.items():
        for _ in range(symbolcount):
            allsymbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        currentsymbols = allsymbols[:]
        for _ in range(rows):
            value = random.choice(allsymbols)
            currentsymbols.remove(value)
            column.append(value)
            
        columns.append(column)
        
    return columns

def checkwinnings(columns, lines, bet, values):
    winnings = 0
    winninglines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symboltocheck = column[line]
            if symbol != symboltocheck:
                break
        else:
            winnings += values[symbol] * bet
            winninglines.append(line + 1)
            
    return winnings, winninglines

def printslotmachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                    print(column[row], end= " | ")
            else:
                print(column[row], end="")
                
        print()

def deposit():
    while True:
        amount = input("How much would you like to bet on? ")

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Amount must be a number.")
            
    return amount

def getnumberoflines():
    while True:
        lines = input("How many lines would you like to bet on? (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    
    return lines

def getbet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    
    return amount
    
def spin(balance):
    lines = getnumberoflines()
    while True:
        bet = getbet()
        totalbet = bet * lines
        
        if totalbet > balance:
            print(f"You do not have enough money to bet that amount. Your current balance is: ${balance}")
        else:
            break
        
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${totalbet}.")
    
    slots = getslotmachinespin(ROWS, COLS, symbolcount)
    printslotmachine(slots)
    winnings, winninglines = checkwinnings(slots, lines, bet, symbolvalues)
    print(f"You Won! {winnings}.")
    print(f"You won on lines: ", *winninglines)
    return winnings - totalbet
    
def main():
    balance = deposit()
    while True:
        print(f"Current Balance is ${balance}")
        answer = input("Press ENTER to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
        
    print("You left with ${balance}.")
    

main()