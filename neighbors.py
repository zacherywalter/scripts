import sys
import enchant

def get_neighbors(word, dictionaries):
    neighbors = set()
    alphabet = 'aäbcdefghijklmnoöpqrstuüvwxyz'
    
    for i in range(len(word)):
        for char in alphabet:
            if char != word[i]:
                neighbor = word[:i] + char + word[i+1:]
                # Check against all dictionaries provided
                for d in dictionaries:
                    if d.check(neighbor):
                        neighbors.add(neighbor)
                        
    return list(neighbors)

if __name__ == "__main__":
    # Check if a word was provided via command line
    if len(sys.argv) < 2:
        print("Usage: neighbors.py <word>")
        sys.exit(1)
        
    target_word = sys.argv[1]
    
    # You can pass multiple dictionaries in a list/tuple
    dicts = (enchant.Dict("en_UK"), enchant.Dict("en_US"), enchant.Dict("de_DE"))
    
    valid_neighbors = get_neighbors(target_word, dicts)
    print(valid_neighbors)
