class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        smaller = nums1 if len(nums1) <= len(nums2) else nums2
        larger = nums1 if len(nums1) > len(nums2) else nums2

        half = (len(smaller) + len(larger) + 1) // 2

        # pointers point to first el in right partitions
        left = 0
        right = len(smaller)

        while left <= right:
            smaller_right_boundary = (left + right) // 2
            larger_right_boundary = half - smaller_right_boundary

            smaller_left = smaller[smaller_right_boundary - 1] if smaller_right_boundary > 0 else float('-inf')
            smaller_right = smaller[smaller_right_boundary] if smaller_right_boundary < len(smaller) else float('inf')

            larger_left = larger[larger_right_boundary - 1] if larger_right_boundary > 0 else float('-inf')
            larger_right = larger[larger_right_boundary] if larger_right_boundary < len(larger) else float('inf')

            if smaller_left > larger_right:
                right = smaller_right_boundary - 1
            elif larger_left > smaller_right:
                left = smaller_right_boundary + 1
            else:
                break

        if (len(smaller) + len(larger)) % 2 == 1:
            return max(smaller_left, larger_left)

        return (max(smaller_left, larger_left) + min(smaller_right, larger_right)) / 2