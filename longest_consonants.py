def longest_consonants(string):
    count = 0
    longest_count = 0
    for ch in string:
        if ch.isalpha() and ch.lower() not in 'aeiou':
            count += 1
            if count > longest_count:
                longest_count = count
        else:
            count = 0 
    
    return longest_count

print(longest_consonants("abcdefghijk!!lmnopqrstuvwxyz"))
