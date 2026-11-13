from collections import deque
from typing import List


class Solution:

  def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
    ans = 0
    cost = 0
    # Store indices of elements that act as running maximums (non-increasing values)
    dq = deque()
    j = len(nums) - 1

    # Iterate backwards from right to left
    for i in range(len(nums) - 1, -1, -1):
      num = nums[i]

      # Pop smaller elements from the back as `num` becomes the new governing maximum
      while dq and nums[dq[-1]] < num:
        l = dq.pop()
        r = dq[-1] if dq else j + 1
        # Increase cost for all elements in range [l, r - 1]
        cost += (r - l) * (num - nums[l])

      dq.append(i)

      # Shrink window from the right if operations exceed k
      while cost > k:
        # nums[dq[0]] is always the maximum value in the current window [i, j]
        cost -= nums[dq[0]] - nums[j]
        if dq[0] == j:
          dq.popleft()
        j -= 1

      # All subarrays starting at i and ending between i and j are valid
      ans += j - i + 1

    return ans
