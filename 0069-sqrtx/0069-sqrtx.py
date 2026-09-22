class Solution:
    def mySqrt(self, x: int) -> int:

        if x <= 1:
            return x

        left = 1
        right = x
        answer = 0

        while left <= right:

            mid = left + (right - left) // 2
            midsq = mid * mid

            if midsq == x:
                return mid

            elif midsq < x:
                answer = mid
                left = mid + 1

            else:
                right = mid - 1

        return answer