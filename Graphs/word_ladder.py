
from collections import defaultdict

def convert_adj_list(curr_word, word_list):
    adj_list = defaultdict(set)
    word_set = set(word_list)  # Convert to set for O(1) lookups

    def helper(parent_word, remaining_words):
        if not remaining_words:
            return

        child_words = {word for word in remaining_words if len(set(parent_word) - set(word)) == 1}

        for child_word in child_words:
            adj_list[parent_word].add(child_word)
            
            # Avoid modifying the list in place, use a new list instead
            new_remaining_words = remaining_words - {child_word}
            helper(child_word, new_remaining_words)

    helper(curr_word, word_set)
    return adj_list

def dfs(curr_word, end_word, adj_list):
    visited = set()

    def helper(curr_word, end_word):
        if curr_word == end_word:
            return 0
        
        if len(visited) == len(adj_list):
            return 0
        
        min_depth = float('inf')

        for child_word in adj_list[curr_word]:
            if child_word in visited:
                continue
            visited.add(child_word)
            min_depth = min(min_depth, helper(child_word, end_word) + 1)
    
        return min_depth

    return helper(curr_word, end_word)

class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list) -> int:
        word_list = set(word_list)  # Ensure word_list is a set for O(1) lookups
        if end_word not in word_list:
            return 0

        adj_list = convert_adj_list(begin_word, word_list)
        print(adj_list)
        return dfs(begin_word, end_word, adj_list)

obj = Solution()
l = ["a", "b", "c"]
print(obj.ladderLength("a", "c", l))
