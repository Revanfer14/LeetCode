class Solution:
    def reverse(self, x: int) -> int:
        res = ""
        flag = False

        for nums in (str(x)[::-1]):
            if nums == 0:
                continue
            elif nums.isdigit() == False:
                flag = True
                continue

            res += nums

        if flag:
            res = "-" + res

        INT32_MIN = -(1 << 31)      # -2147483648
        INT32_MAX = (1 << 31) - 1   # 2147483647
        
        return 0 if (int(res) > INT32_MAX or int(res) < INT32_MIN) else int(res)