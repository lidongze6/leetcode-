class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ""
        i = 0
        l = len(s)
        while i < l:
            # 若为（'10#' - '26#'）按2bit解码
            if i + 2 < l and s[i + 2] == '#':
                res += chr(int(s[i:i + 2]) + ord('j') - 10)
                i += 3
            # 否则（'1' - '9'）按1bit解码
            else:
                res += chr(int(s[i]) + ord('a') - 1)
                i += 1
        return res
