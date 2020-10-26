words = input().split()
searched_palindrome = input()

palindromes = [word for word in words if word[::-1] == word]
found_palindrome_count = palindromes.count(searched_palindrome)

print(palindromes)
print(f"Found palindrome {found_palindrome_count} times")
