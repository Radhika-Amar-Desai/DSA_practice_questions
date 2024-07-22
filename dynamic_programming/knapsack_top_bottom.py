class Item:
    def __init__ ( self , weight, price ) -> None:
        self.weight = weight
        self.price = price

def knapsack( items : list, max_capacity : int, num_of_items : int ):
    dp = [ [ -1 for _ in range ( max_capacity ) ] for _ in range ( num_of_items ) ]
    
    for num in range ( num_of_items ):
        for capacity in range ( max_capacity ):
            if num == 0 or capacity == 0:
                dp [ num ] [ capacity ] = 0

    max_price = 0

    for num in range ( num_of_items ):
        for capacity in range ( max_capacity ):
            if items [ num ].weight <= capacity:
                dp [ num ][ capacity ] = max ( items [ num-1 ].price + dp [ num - 1 ][ capacity - items [ num ].weight ], 
                                              dp [ num - 1 ][ capacity ])
    
                max_price = max ( max_price , dp [ num ][ capacity ] )

    return max_price
    
items = [ Item ( 2, 40 ), Item ( 3, 10 ), Item ( 5, 20 ) ]
capacity = 8

print ( knapsack ( items , 8, 3 ) )