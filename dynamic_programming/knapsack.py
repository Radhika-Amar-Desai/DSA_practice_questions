from functools import lru_cache

class Item:
    def __init__ ( self , weight, price ) -> None:
        self.weight = weight
        self.price = price

max_price = 0

function_call_cache = {}

def knapsack_wrapper ( items : list, capacity : int, num_of_items : int ):

    def knapsack ( capacity : int, num_of_items : int ):
        if num_of_items == 0 or capacity == 0:
            return 0
        
        if items[ num_of_items-1 ].weight <= capacity:
            if items[num_of_items-1] in function_call_cache:
                price_on_including_item , price_on_not_including_item = function_call_cache[items[num_of_items-1]]
                
            else:
                price_on_including_item = items[ num_of_items-1 ].price + knapsack ( capacity-items[ num_of_items-1 ].weight, num_of_items-1 )
                price_on_not_including_item = knapsack ( capacity, num_of_items-1 )
                
                function_call_cache [ items[num_of_items-1] ] = ( price_on_including_item , price_on_not_including_item )

            return max ( price_on_including_item, price_on_not_including_item )
        
        else:
            return knapsack ( capacity, num_of_items-1 )
        
    return knapsack ( capacity, num_of_items )

items = [ Item ( 2, 40 ), Item ( 3, 10 ), Item ( 5, 20 ) ]
capacity = 8
print ( knapsack_wrapper ( items, capacity, 3 ) )