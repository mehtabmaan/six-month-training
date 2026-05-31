class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # Create a DP table with dimensions (m+1) x (n+1) initialized to 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Characters match, add 1 to the diagonal value
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # Characters don't match, take the max of top or left cell
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        # The bottom-right corner contains the length of the LCS
        return dp[m][n]