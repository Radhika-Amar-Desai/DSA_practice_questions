def get_min_diff_subsets ( nums : list ):
    n = len ( nums )
    dp = [ [ True for _ in range ( sum ( nums ) + 1 ) ] for _ in range ( n + 1 ) ]

    for num_index in range ( n + 1 ):
        for subsum in range ( sum ( nums ) + 1 ):
            
            if subsum == 0 and num_index != 0:
                dp [ num_index ] [ subsum ] = 0

            if num_index == 0:
                dp [ num_index ] [ subsum ] = 1

    
    for num_index in range ( 1 , n + 1 ):
        for subsum in range ( 1 , sum ( nums ) + 1 ):

            if nums [ num_index - 1 ] <= subsum :
                dp [ num_index ] [ subsum ] = dp [ num_index - 1 ] [ subsum - nums [ num_index - 1 ] ] or\
                                                dp [ num_index - 1 ] [ subsum ]
            
            else:
                dp [num_index ] [ subsum ] = dp [ num_index - 1 ] [ subsum ]

    sums_of_subsets = [ sum_of_subset for sum_of_subset in range ( sum ( nums ) + 1 ) \
                       if dp [ n ] [ sum_of_subset ] ]
    
    sorted_sums_of_subsets = sorted ( sums_of_subsets )

    return sorted_sums_of_subsets [ len ( sums_of_subsets ) // 2 ] - \
            sorted_sums_of_subsets [ len ( sums_of_subsets ) // 2 - 1 ]


nums = [ 2, 3, 6, 8, 10 ]

min_diff = get_min_diff_subsets ( nums )
print ( min_diff )