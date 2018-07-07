def check_anagram(string_1, string_2):
    dict_1 = {}
    dict_2 = {}
    string_1 = string_1.lower()
    string_2 = string_2.lower()

    for x in string_1:
        if x != " ":
            if x in dict_1:
                dict_1[x] += 1
            else:
                dict_1[x] = 1

    for x in string_2:
        if x != " ":
            if x in dict_2:
                dict_2[x] += 1
            else:
                dict_2[x] = 1

    return dict_1 == dict_2


print("anagram, nagaram      "+str(check_anagram("anagram", "nagaram")))
print("Keep, Peek      "+str(check_anagram("Keep", "Peek")))
print("Mother In Law, Hitler Woman      "+str(check_anagram("Mother In Law", "Hitler Woman")))
print("School Master,  The Classroom     "+str(check_anagram("School Master", "The Classroom")))
print("ASTRONOMERS,  NO MORE STARS     "+str(check_anagram("ASTRONOMERS", "NO MORE STARS")))
print("Toss, Shot      "+str(check_anagram("Toss", "Shot")))
print("Debit Card, Bad Credit      "+str(check_anagram("Debit Card", "Bad Credit")))
print("joy, enjoy      "+str(check_anagram("joy", "enjoy")))
print("SiLeNt CAT,  LisTen AcT     "+str(check_anagram("SiLeNt CAT", "LisTen AcT")))
print("Dormitory,  Dirty Room     "+str(check_anagram("Dormitory", "Dirty Room")))


# Test case2: Keep, Peek – true
# Test case3: Mother In Law, Hitler Woman – true
# Test case4: School Master, The Classroom – true
# Test case5: ASTRONOMERS, NO MORE STARS – true
# Test case6: Toss, Shot – false
# Test case7: joy, enjoy – false
# Test case8: Debit Card, Bad Credit – true
# Test case9: SiLeNt CAT, LisTen AcT – true
# Test case10: Dormitory, Dirty Room – true
