paths = []

def get_next_squares ( curr_sq, maze ):
    
    def does_sq_exist_in_maze ( sq ):
        return 0 <= sq[0] <= len(maze) - 1 and 0 <= sq[1] <= len(maze) - 1

    potential_next_squares = [ ( curr_sq[0] + 1, curr_sq[1]) , ( curr_sq[0], curr_sq[1] + 1 ) ]
    
    return [ sq for sq in potential_next_squares if does_sq_exist_in_maze ( sq ) ]

def can_navigate ( next_square , maze ):
    return maze[ next_square [ 0 ] ][ next_square [ 1 ] ] == 1

def navigate ( maze : list, seq_of_squares_visited = [], curr_sq = ( 0 , 0 ) ):

    if curr_sq == ( len ( maze ) - 1 , len ( maze [ 0 ] ) - 1 ):

        paths.append ( seq_of_squares_visited.copy() )
        return
    
    for next_square in get_next_squares ( curr_sq, maze ):

        if can_navigate ( next_square , maze ):

            seq_of_squares_visited.append ( next_square )
            navigate ( maze, seq_of_squares_visited , next_square )
            seq_of_squares_visited.remove ( next_square )

    return
    
maze = [ 
    [ 1 , 0, 0, 0],
    [ 1 , 1, 0, 1],
    [ 1 , 1, 0, 0],
    [ 0 , 1, 1, 1]
]

navigate ( maze )
print ( paths )