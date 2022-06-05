class Solution:
    def test(self):
        a = [1, 4, 2, 5, 2, 3, 5]
        self.sorted(a)
        print(a)

    def sorted(self, arr, key=None):
        self.quickSort(arr, 0, len(arr) - 1)

    def quickSort(self, arr, i, j):
        if i >= j:
            return

        middle = j // 2
        self.swap(arr, i, middle)

        left, right = i + 1, j
        while left < right:

            swap_left, swap_right = -1, -1
            while swap_left == -1 or swap_right == -1:
                if swap_left == -1:
                    if j <= left:
                        swap_left = left - 1
                    else:
                        if arr[i] < arr[left]:
                            swap_left = left
                        else:
                            left += 1
                if swap_right == -1:
                    if right <= i:
                        swap_right = right + 1
                    else:
                        if arr[right] < arr[i]:
                            swap_right = right
                        else:
                            right -= 1
            self.swap(arr, swap_left, swap_right)
            i, j = left + 1, right - 1
        self.swap(arr, i, right)

        self.quickSort(arr, i, right - 1)
        self.quickSort(arr, right + 1, j)

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    s = Solution()
    s.test()