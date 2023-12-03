def shortest_palindrome_bruteforce(s):
    n = len(s)
    s_rev = s[::-1]

    for i in range(n, 0, -1):
        if s[:i] == s[:i][::-1]:
            return s_rev[:n-i] + s
    return s_rev + s  # If s has no palindrome substring at all.
