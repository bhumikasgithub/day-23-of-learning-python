#!
def list_operation(x, y, n):
    return [i for i in range(x, y + 1) if i % n == 0]

# Example test cases
print(list_operation(1, 10, 3))   # ➞ [3, 6, 9]
print(list_operation(7, 9, 2))    # ➞ [8]
print(list_operation(15, 20, 7))  # ➞ []

#2
def simon_says(list1, list2):
    return list1[:-1] == list2[1:]

print(simon_says([1, 2], [5, 1]))             # ➞ True
print(simon_says([1, 2], [5, 5]))             # ➞ False
print(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))  # ➞ True
print(simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]))  # ➞ False

#3
def society_name(names):
    # Step 1: Take the first letter of each name
    first_letters = [name[0] for name in names]
    
    # Step 2: Sort the letters alphabetically
    sorted_letters = sorted(first_letters)
    
    # Step 3: Join them to form a single string
    return ''.join(sorted_letters)
print(society_name(["Adam", "Sarah", "Malcolm"]))           # ➞ "AMS"
print(society_name(["Harry", "Newt", "Luna", "Cho"]))       # ➞ "CHLN"
print(society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]))  # ➞ "CJMPPR"

#4
def is_isogram(word):
    # Convert to lowercase to make it case-insensitive
    word = word.lower()
    
    # Check if the number of unique letters is equal to total letters
    return len(set(word)) == len(word)
print(is_isogram("Algorism"))     # ➞ True
print(is_isogram("PasSword"))     # ➞ False
print(is_isogram("Consecutive"))  # ➞ False
print(is_isogram("Machine"))      # ➞ True
print(is_isogram("Alphabet"))     # ➞ False


