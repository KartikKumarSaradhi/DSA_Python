vowel = ['a','e','i','o','u']
ch = input("enter a character")

# if(ch.isalpha()):
#     ch = ch.lower()
#     if(ch in vowel):
#         print("vowel")
#     else:
#         print("consonant")
# else:
#     print("Not an alphabet")



if(ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
    if(ch in vowel):
        print("vowel")
    else:
        print("Consonant")
else:
    print("not an alphabet")