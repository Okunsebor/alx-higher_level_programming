#!/usr/bin/python3
def remove_char_at(s, n):
    """
    Creates a copy of the string s, removing the character at the position n.
    The index n is 0-based (i.e., the first character is at index 0).

    Args:
    - s: the input string (str)
    - n: the index of the character to remove (int)

    Returns:
    A new string that is a copy of s with the character at index n removed.
    If n is out of range (i.e., negative or greater than or equal to the length
    of s), returns s as is.
    """
	if n < 0 or n >= len(s):
        # n is out of range, return s as is
		return s
	else:
        # concatenate the substring before and after the character to remove
		return s[:n] + s[n+1:]
