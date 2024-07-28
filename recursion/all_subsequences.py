all_subseqs = []

def subseq ( string : str, output = "" ):
    if string == "":
        if output not in all_subseqs:
            all_subseqs.append ( output )
            return

    for ch_index, ch in enumerate ( string ):

        remaining_string = "".join ( [ char for index , char in enumerate(string) if index > ch_index ] )
        subseq ( remaining_string, output + ch )
        subseq ( remaining_string, output )

text = "abc"
subseq ( text )
print ( all_subseqs )