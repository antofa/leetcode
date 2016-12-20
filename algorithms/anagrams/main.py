class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for i, s in enumerate(strs):
            x = ''.join(j for j in sorted(s))
            print x
            if x not in d:
                d[x] = [s]
            else:
                d[x].append(s)
        
        r = []
        for key in sorted(d):
            r.append(sorted(d[key]))
        return sorted(r, reverse=True)      