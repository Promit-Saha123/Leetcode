class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        groups = {}
        
        for word in strs: # n

            count = [0] * 26 

            for char in word: # m
                count[ord(char) - ord("a")] += 1 # running tally of letter frequencies
            
            key = tuple(count) # allows as key because it is now immutable

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values()) # converts dictionary values into a list


        # O(m*n) Space: m*n

