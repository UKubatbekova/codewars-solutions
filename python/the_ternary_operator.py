# https://www.codewars.com/kata/56f3f6a82010832b02000f38

def describe_age(age):
 return"You're a(n) "+("kid"if age<=12 else"teenager"if age<=17 else"adult"if age<=64 else"elderly")