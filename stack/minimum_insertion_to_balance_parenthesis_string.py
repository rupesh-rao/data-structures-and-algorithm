class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        st = []
        i = 0
        ans = 0
        while i < n:
            # append open bracket
            if s[i] == '(':
                st.append(i)
                i += 1
            # when close bracket
            else:
                # check if next element is present
                if i + 1 < n:
                    # if next element is also closing bracket
                    if s[i + 1] == ')':
                        # check if corresponding open present
                        if len(st) == 0:
                            # if not present add 1 for the open bracket insertion
                            ans += 1
                        else:
                            # add nothing, just pop corresponding open bracket
                            st.pop()
                        # move 2 steps ahead
                        i += 2
                    # if next element is not closing bracket
                    else:
                        # check if corresponding open present
                        if len(st) == 0:
                            # if not present, add 2 for the open bracket and close bracket insertion
                            ans += 2
                        else:
                            # if present, add only one for the close bracket
                            ans += 1
                            st.pop()
                        i += 1
                # at the end of the string
                else:
                    # check if corresponding open present
                    if len(st) == 0:
                        # if not present, add 2 for the open bracket and close bracket insertion
                        ans += 2
                    else:
                        # if present, add only one for the close bracket
                        ans += 1
                        st.pop()
                    i += 1

        ans += len(st) * 2

        return ans

