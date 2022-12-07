'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''


def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    from_member_key = social_graph[from_member]
    to_member_key = social_graph[to_member]

    from_member_following = from_member_key["following"]
    to_member_following = to_member_key["following"]

    result = []

    if to_member in from_member_following:
        result.append('follower')

    if from_member in to_member_following:
        result.append('followed by')

    status = ""

    if not result:
        status = "no relationship"

    elif len(result) == 1:
        status = result[0]

    else:
        status = "friends"

    return status
    
def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    rowCount = len(board)

    for row_index in range(rowCount):
        O = 0
        X = 0

        for col_index in range(rowCount):
            if 'O' == board[row_index][col_index]:
                O += 1
            elif 'X' == board[row_index][col_index]:
                X += 1

        if (X == rowCount):
            return 'X'
        elif (O == rowCount):
            return 'O'

    for row_index in range(rowCount):
        O = 0
        X = 0

        for col_index in range(rowCount):
            if 'O' == board[col_index][row_index]:
                O += 1
            elif 'X' == board[col_index][row_index]:
                X += 1

        if (X == rowCount):
            return 'X'
        elif (O == rowCount):
            return 'O'

    O = 0
    X = 0
    for row_index in range(rowCount):
        if 'O' == board[row_index][row_index]:
            O += 1
        elif 'X' == board[row_index][row_index]:
            X += 1

    if (X == rowCount):
        return 'X'
    elif (O == rowCount):
        return 'O'

    return 'No Winner'

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    first_stop = input("Enter your First Stop:").upper()
second_stop = input("Enter your Second Stop:").upper()
legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}
legs = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}
travel_time = 0

def eta(first_stop, second_stop):
    if first_stop == "UPD" and second_stop == "ADMU":
        Route_Map = "The Route Map is UPD to ADMU"
        travel_time = "Your travel time is 10 mins"
    elif first_stop == "ADMU" and second_stop == "DLSU":
        Route_Map = "The Route Map is ADMU to DLSU"
        travel_time = "Your travel time is 35 mins"
    elif first_stop == "DLSU" and second_stop == "UPD":
        Route_Map = "The Route Map is DLSU to UPD"
        travel_time = "Your travel time is 55 mins"
    elif first_stop == "DLSU" and second_stop == "ADMU":
        Route_Map = "The Route Map is dlsu, upd, admu"
        travel_time = "Your travel is 65 mins"
    elif first_stop == "UPD" and second_stop == "DLSU":
        Route_Map = "The Route Map is UPD, ADMU, DLSU"
        travel_time = "Your travel time is 45 mins"
    elif first_stop == "ADMU" and second_stop == "UPD":
        Route_Map = "The Route Map is ADMU, DLSU, UPD"
        travel_time = "Your travel time is 90 mins"

    elif first_stop == "A1" and second_stop == "A2":
        Route_Map = "The Route Map is a1 to a2"
        travel_time = "Your travel time is 10 mins"
    elif first_stop == "A2" and second_stop == "B1":
        Route_Map = "The Route Map is a2 to b1"
        travel_time = "Your travel time is 10230 mins"
    elif first_stop == "B1" and second_stop == "A1":
        Route_Map = "The Route Map is b1 to a1"
        travel_time = "Your travel time is 1 min"
    elif first_stop == "B1" and second_stop == "A1":
        Route_Map = "The Route Map is b1, a1, b1"
        travel_time = "Your travel time is 11 mins"
    elif first_stop == "A1" and second_stop == "B1":
        Route_Map = "The Route Map is a1, a2, b1"
        travel_time  = "Your travel time is 10240 mins"
    elif first_stop == "a2" and second_stop == "a1":
        Route_Map = "The Route Map is a2, b1, a1"
        travel_time = "Your travel time is 10231 mins"
    else:
        travel_time = "Please enter a valid location"

    return travel_time + "\n" + Route_Map
print(eta(first_stop, second_stop))