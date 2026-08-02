class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1,n2 = len(s),len(t)

        if not t or n2>n1:
            return ""
        
        count_t = Counter(t)
        window = {}

        have ,need = 0, len(count_t)
        res, res_len = [-1,-1], float("inf")
        left = 0

        for right in range(n1):
            window[s[right]] = window.get(s[right],0)+1

            if s[right] in count_t and count_t[s[right]] == window[s[right]]:
                have += 1
            
            while have == need:
                if (right-left+1)<res_len:
                    res = [left,right]
                    res_len = right-left+1
                window[s[left]] -= 1
                if s[left] in count_t and count_t[s[left]] > window[s[left]]:
                    have -= 1
                left += 1
        l,r = res
        return s[l:r+1] if res_len != float("inf") else ""