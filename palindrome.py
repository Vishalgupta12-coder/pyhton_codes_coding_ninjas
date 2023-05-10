
from sys import stdin


def isPalindrome(string) :
	# Your code goes here
    rev_string=string[::-1]
    if string == rev_string:
        return True


#main
string = stdin.readline().strip();
ans = isPalindrome(string)

if ans :
    print('true')
else :
    print('false')

