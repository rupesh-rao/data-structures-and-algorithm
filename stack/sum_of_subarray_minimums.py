class Solution:
    # Function to find the indices
    # of next smaller elements
    def findNSE(self, arr):

        # Size of array
        n = len(arr)

        # To store the answer
        ans = [0] * n

        # Stack
        st = []

        # Start traversing from the back
        for i in range(n - 1, -1, -1):

            # Pop the elements in the stack until
            # the stack is not empty and the top
            # element is not the smaller element
            while st and arr[st[-1]] >= arr[i]:
                st.pop()

            # Update the answer
            ans[i] = st[-1] if st else n

            # Push the index of current
            # element in the stack
            st.append(i)

        # Return the answer
        return ans

    # Function to find the indices of
    # previous smaller or equal elements
    def findPSE(self, arr):

        # Size of array
        n = len(arr)

        # To store the answer
        ans = [0] * n

        # Stack

        st = []

        # Traverse on the array
        for i in range(n):

            # Pop the elements in the stack until
            # the stack is not empty and the top
            # elements are greater than the current element
            while st and arr[st[-1]] > arr[i]:
                st.pop()

            # Update the answer
            ans[i] = st[-1] if st else -1

            # Push the index of current
            # element in the stack
            st.append(i)

        # Return the answer
        return ans

    # Function to find the sum of the
    # minimum value in each subarray
    def sumSubarrayMins(self, arr):

        nse = self.findNSE(arr)
        pse = self.findPSE(arr)

        # Size of array
        n = len(arr)

        mod = int(1e9 + 7)  # Mod value

        # To store the sum
        total_sum = 0

        # Traverse on the array
        for i in range(n):
            # Count of first type of subarrays
            left = i - pse[i]

            # Count of second type of subarrays
            right = nse[i] - i

            # Count of subarrays where
            # current element is minimum
            freq = left * right * 1

            # Contribution due to current element
            val = (freq * arr[i]) % mod

            # Updating the sum
            total_sum = (total_sum + val) % mod

        # Return the computed sum
        return total_sum

