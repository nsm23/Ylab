from itertools import combinations

def bananas(s: str) -> set:
    res = set()
    word = 'banana'
    count = len(s) - len(word)
    pool_words = combinations(range(len(s)), count)
    for i in pool_words:
        temp_lst = list(s)
        for a in i:
            temp_lst[a] = '-'
        update_str = ''.join(temp_lst)
        if update_str.replace('-', '') == word:
            res.add(update_str)
    return res
    


    
