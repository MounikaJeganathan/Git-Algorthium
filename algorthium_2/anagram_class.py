def is_anagram(s1,s2):
    if len(s1)!= len(s2):
        print("False")
        return

    if sorted(s1)==sorted(s2):
        print("True")
    else:
        print("False")



is_anagram("abcd", "dbca") #True
is_anagram("abcdf", "dfbca") #True
is_anagram("abcd", "aaca") #False
is_anagram("abcd", "cdca") #False
is_anagram("abcd", "dbc") #False
is_anagram("abcd", "1234") #False
is_anagram("abcd", "Adbc") #False
is_anagram("", "") #True



