s = "pwwkew"

map_string = {}
for i in s:
    if i not in map_string:
        map_string[i] = i
    else:
        i+=1
print(len(map_string)) 
        