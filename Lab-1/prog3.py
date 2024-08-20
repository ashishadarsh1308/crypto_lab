def is_isogram(s):
    clean_string = s.lower().replace(" ", "").replace("-", "")

    char_set = set(clean_string)

    return len(char_set) == len(clean_string)

# Test cases
print(is_isogram(""))  
print(is_isogram("uncopyrightable"))  
print(is_isogram("First# Clan!")) 
print(is_isogram("BackGround"))  
print(is_isogram("isograms"))  
