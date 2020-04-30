# write your code here
global states
states = [[' ' for x in range(3)] for x in range(3)]
coordinates = [(3,1), (2,1), (1,1), (3,2), (2,2), (1,2), (3,3), (2,3), (1,3)]


def create_visual_board():
    print('---------')
    for row in range(3):
        print(f'| {states[row][0]} {states[row][1]} {states[row][2]} |')
    print('---------')


def check_game_status(symbol):
    winner_counter = 0
    # Check rows
    for row in range(3):
        if states[row] == list(symbol * 3):
            winner_counter += 1
    
    # Check columns
    for column in range(3):
        if states[0][column] + states[1][column] + states[2][column] == symbol * 3:
            winner_counter += 1
    
    # Check diagonals
    if (states[0][0] + states[1][1] + states[2][2] == symbol * 3) or (states[0][2] + states[2][2] + states[2][1] == symbol * 3):
        winner_counter += 1
    
    return winner_counter  


def count_xs_and_os():
    x_count = 0
    o_count = 0
    for row in states:
        for state in row:
            if state == 'X':
                x_count += 1
            elif state == 'O':
                o_count += 1
    return x_count, o_count


def check_game_won(x_win_count, o_win_count):
    if x_win_count == 1 and o_win_count == 0:
        print('X wins')
        return True
    elif o_win_count == 1 and x_win_count == 0:
        print('O wins') 
        return True
    return False               


def check_impossible(x_win_count, o_win_count, x_count, o_count):
    if x_win_count == o_win_count == 1 or abs(o_count - x_count) >= 2:
        #print('Impossible') 
        return True
    return False                  


def check_unfinished(x_win_count, o_win_count, x_count, o_count):
    if x_win_count == o_win_count == 0 and x_count + o_count < len(states):
        if not check_impossible(x_win_count, o_win_count, x_count, o_count):
            #print('Game not finished')
            return True
    return False        


def check_draw(x_win_count, o_win_count, x_count, o_count):
    if x_win_count == o_win_count == 0 and x_count + o_count == 9:
        print('Draw') 
        return True 
    return False     


def user_input_check(row, column):
    # Check the coordinates     
    if row >= 4 or column >= 4 or row <= 0 or column <= 0:
        print('Coordinates should be from 1 to 3!')
        return False
        
    # Check cell occupation
    coord = (row - 1) * 3 + column - 1
    cell = states[coordinates[coord][0] - 1][coordinates[coord][1] - 1]
    if cell == 'X' or cell == 'O':
        print('This cell is occupied! Choose another one!')
        return False
        
    # Check if the inputs are integers
    if not (type(row) == int or type(column) == int):
        print('You should enter numbers!')   
        return False
    
    return True 


def get_user_input(symbol):
    row, column = list(map(int, input().split()))   
    while not user_input_check(row, column):
        row, column = list(map(int, input().split()))
    coord = (row - 1) * 3 + column - 1
    states[coordinates[coord][0] - 1][coordinates[coord][1] - 1] = symbol
    create_visual_board()


def check_all_possible_states():
    x_count, o_count = count_xs_and_os()
    x_win_count = check_game_status('X')
    o_win_count = check_game_status('O')  
    won = check_game_won(x_win_count, o_win_count)
    impossible = check_impossible(x_win_count, o_win_count, x_count, o_count)
    not_finished = check_unfinished(x_win_count, o_win_count, x_count, o_count)
    draw = check_draw(x_win_count, o_win_count, x_count, o_count)
    return {
        'won': won,
        'impossible': impossible, 
        'not_finished': not_finished, 
        'draw': draw
        }


def main():
    create_visual_board()
    symbol = 'O'
    get_user_input(symbol)
    state = check_all_possible_states()
    while not (state['won'] or state['draw']):
        if symbol == 'X':
            symbol = 'O'
        elif symbol == 'O':
            symbol = 'X'    
        get_user_input(symbol)
        state = check_all_possible_states()              
    print(states)

if __name__ == '__main__':
    main()                                 

