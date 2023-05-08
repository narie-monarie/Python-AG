"""
You are given a binary string s and an integer m.
You need to return an integer r. Where r = k%m, k 
is the binary equivalent of string s.

Input:
s = "101" 
m = 2
Output:
1
Explanation: Here k=5 because (101)2 = (5)10.
Hence 5 mod 2 = 1.

"""


class Solution():
    def modulo(self, s, m):
        return int(s, 2) % m

# Driver Code Starts
# Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        s, m = input().split()
        m = int(m)
        print(Solution().modulo(s, m))

# } Driver Code Ends
