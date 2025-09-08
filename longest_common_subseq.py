class LCSClass:
    """...write comment for this class...
    Class to calculate the Longest Common Subsequence length between two strings using DP 

    Examples from Instructions:
        abca is a subsequence of abccefa with a length of 4
        adf is a subsequence of abcdef with a length of 3
        ebcf is a subsequence of aeebbefc with a length of 3
        vc is not a subsequence of asdf
    """

    def __init__(self):
        """...write comment about this method...
        Initialize the LCSClass
        """
        pass

    
    def find(self, x, y): 
        """...write comment about this method...
        Find the length of the longest common subsequence

        Params:
        x: str --> first test string
        y: str --> second string (possible subsequence string)

        Returns: int --> the length of the LCS
        """
        #TODO: function logic

        m = len(x)
        n = len(y)

        # create 2D DP tbl
        dp = [[0] * (n+1) for _ in range(m+1)]

        # Fill tbl bottom-up
        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1]:
                    # If characters match, extend subsequence
                    dp[i][j] = dp[i-1][j-1] +1
                else:
                    # Otherwise, take max by ignoring one char
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]
    


    ''' Assignment Question:
    As part of the assignment, describe how the algorithms can be 
    implemented using recursive and how it would perform.

    The algorithm can be implemented using recursion by comparing the
    last charaters of the two strings. If they match, we can add 1 to the 
    LCS counter and then check the smaller parts of both strings. If 
    they don't match, then we can either ignore the last character of the first string
    or the last character of the second string and take whichever result is
    bigger. If one of the strings are empty then we would just return 0. I believe the
    runtime for this one o(2^n) since it is running through the same
    substrings multiple times (much slower). '''