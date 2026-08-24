class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        A = nums1
        B = nums2

        m = len(A)
        n = len(B)

        low = 0
        high = m

        half = (m + n + 1) // 2

        while low <= high:
            i = (low + high) // 2
            j = half - i

            Aleft = float("-inf") if i == 0 else A[i - 1]
            Aright = float("inf") if i == m else A[i]

            Bleft = float("-inf") if j == 0 else B[j - 1]
            Bright = float("inf") if j == n else B[j]

          
            if Aleft <= Bright and Bleft <= Aright:

              
                if (m + n) % 2 == 1:
                    return max(Aleft, Bleft)

              
                return (
                    max(Aleft, Bleft) +
                    min(Aright, Bright)
                ) / 2

           
            elif Aleft > Bright:
                high = i - 1

            else:
                low = i + 1