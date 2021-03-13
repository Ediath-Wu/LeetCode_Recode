class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        all_list = [[] for i in range(numRows)]
        turn = 1
        num = 1
        count_str = 0
        while True:
            if num >= 1 and num <= numRows:
                all_list[num-1].append(s[count_str])
                count_str += 1
                if count_str == len(s):
                    break
                num += turn
            else:
                turn = -turn
                num += turn
                num += turn

        ret = []

        rstr=''

        for i in range(numRows):
            for j in range(len(all_list[i])):
                rstr+=all_list[i][j]
        return rstr


a = Solution()
print(a.convert('paypalishiring', 3))
