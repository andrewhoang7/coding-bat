#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

# double_char

# Given a string, return a string where for every char in the original, there are two chars.


# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'

def double_char(str):
  result=''
  for i in str:
    result+=i*2
  return result


#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

# count_hi

# Return the number of times that the string "hi" appears anywhere in the given string.


# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2

def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    if str[i:i+2] == 'hi':
      count += 1
  return count

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

# cat_dog

# Return True if the string "cat" and "dog" appear the same number of times in the given string.


# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(str):
  count_dog = 0
  count_cat = 0
  for i in range(len(str)-1):
    if str[i:i+3] == 'dog':
      count_dog +=1
    if str[i:i+3] == 'cat':
      count_cat +=1
  return count_dog == count_cat

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

# count_code

# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.


count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2

def count_code(str):
  count=0
  for i in range(len(str)-3):
    if str[i] == "c" and str[i+1] == "o" and str[i+3] == "e": 
      count+=1
  return count

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

# end_other

# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.


end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True

def end_other(a, b):


#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

