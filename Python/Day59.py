def palindrome(word):
  word = word.lower()
  if len(word) <= 1:
    return True
  if word[0] != word[-1]:
    return False
  return palindrome(word[1:-1])


print(palindrome("racecar"))
print(palindrome("mom"))
print(palindrome("racecars"))
print(palindrome("Racecar"))
