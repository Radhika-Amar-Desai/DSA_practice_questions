def count_of_partitions_with_target_diff ( nums : list , target_diff : int ):
    dp = [ [ -1 for _ in range ( sum ( nums ) + 1 ) ] for _ in range ( len ( nums ) + 1 ) ]
    
    n = len ( nums )
    sum_of_nums = sum ( nums )

    def initialize_dp ():
        nonlocal dp

        for num_index in range ( n + 1 ):
            for subsum in range ( sum_of_nums ):

                if num_index == 0 and subsum != 0:
                    dp [ num_index ] [ subsum ] = 0

                if subsum == 0:
                    dp [ num_index ] [ subsum ] = 1

    def fill_dp ():
        nonlocal dp

        for num_index in range ( 1 , n + 1 ):
            for subsum in range ( 1 , sum_of_nums + 1 ):

                if nums [ num_index - 1 ] <= subsum:
                    dp [ num_index ] [ subsum ] = dp [ num_index - 1 ] [ subsum - nums [ num_index - 1 ] ] +\
                                                    dp [ num_index - 1 ] [ subsum ]
                    
                else:
                    dp [ num_index ] [ subsum ] = dp [ num_index - 1 ] [ subsum ]

    def get_sums_of_first_partition():
        initialize_dp ()
        fill_dp ()

        sums_of_subsets = [ subsum for subsum in range ( sum_of_nums + 1 ) if dp [ n ] [ subsum ] > 0 ]

        return sums_of_subsets [ : len ( sums_of_subsets ) // 2 ]
    
    num_of_partitions_with_target_diff = 0

    for first_partition_sum in get_sums_of_first_partition():
        #print ( first_partition_sum )
        if sum_of_nums - 2 * first_partition_sum == target_diff:
            print ( first_partition_sum )
            num_of_partitions_with_target_diff += dp [ n ] [ first_partition_sum ]   
    
    return num_of_partitions_with_target_diff
    
nums = [ 2, 3, 5, 8, 10 ]
answer = count_of_partitions_with_target_diff ( nums , 8 )
print ( answer )