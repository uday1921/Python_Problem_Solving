import datetime as dt
#Fitst Method

NO_OF_CHARS = 256
def countchars(input_string):
    count = [0]*NO_OF_CHARS
    for i in input_string:
        count[ord(i)] +=1
    return count
def FirstNonRepeatingCharacter(original_str):
    count = countchars(original_str)
    #print(count)
    print(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    for i in original_str:
        if(count[ord(i)]==1):
            print(i)
            break;
s = "baaacccaaabq"
FirstNonRepeatingCharacter(s)

#Second Method

'''count_dir = {z:s.count(z) for z in s}
for k,v in count_dir.items():
    if(v==1):
        print(k)
        break;'''
