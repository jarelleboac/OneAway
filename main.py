#One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given TWO strings, write a function to check if THEY are ONE edit (or zero edits) away.
#EXAMPLE
#pale, ple -> true
#pales, pale -> true
#pale, bale -> true
#pale, bae -> false


#check if can REMOVE character
#check if can ADD character
#checK if can REPLACE character
#check if strings are EQUAL 

def oneAway(string1, string2):
  matches = 0
  #first check if strings are EQUAL
  if(string1==string2):
    return True
  else:
    length1 = len(string1)
    length2 = len(string2)
    length2_rem = length2-1
    length2_add = length2+1
    print(length2)
    print(length2_rem)
    if(length1 == length2):
      #possibly 1 character replaced
      #number of matching chars should equal the lengths-1
      #for loop run through string1
      #for loop run through string 2
      
      for i in range(len(string1)):
          #print(string1[i])
          #print(string2[i])
          if(string1[i]==string2[i]):
            matches+= 1
      #print(matches)
      if(matches == length2_rem):
        print("1 character replaced")
        return True
    elif length1 == length2_rem:
      #possibly 1 character can be added to string1
      #possibly 1 character can be removed from string2

      #test1: (appl, apple)
      #test2: (apple, appl)

      #still need to compare if most of the letters are matching
      #also the letters can be removed in ANY INDEX in the string

      #for loop iterate through 1st and 2nd and then if different, check if next elem in strin1 is equal to the one currently at string2
      print("hi")
    elif length1 == length2_add:
      print("hi")
      #possibly 1 character can be removed from string1
      #possibly 1 character can be removed from string2
      #test3: (aaple, apple)
    elif:
      return False




test1= "applf"
test2= "apple"
if(oneAway(test1, test2)):
  print("they ARE one edit away")
else:
  print("they are NOT one edit away")
