# https://takeuforward.org/practice/dsa/accounts-merge
# TC: 
# Space: O(2*N)
class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)

    def findParent(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.findParent(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        parent_u = self.findParent(u)
        parent_v = self.findParent(v)
        
        if parent_u != parent_v:
            # parent with bigger rank becomes parent
            if self.rank[parent_u] < self.rank[parent_v]:
                self.parent[parent_u] = parent_v
            elif self.rank[parent_u] > self.rank[parent_v]:
                self.parent[parent_v] = parent_u
            else:
                self.rank[parent_u] += 1
                self.parent[parent_v] = parent_u

class Solution:
    def accountsMerge(self, accounts):
        n = len(accounts)
        dsu = DSU(n)
        # email to index at which they are merged
        emailToNode = {}

        for i in range(n):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                # merge email if it was present in earlier node (index)
                if email in emailToNode:
                    dsu.union(i, emailToNode[email])
                # email occuring first time
                else:
                    emailToNode[email] = i

        mergedEmails = [[] for _ in range(n)]

        # for every email find the parent of the node
        for email, node in emailToNode.items():
            parent = dsu.findParent(node)
            mergedEmails[parent].append(email)

        ans = []
        for i in range(n):
            if not mergedEmails[i]:
                continue
            mergedEmails[i].sort()
            ans.append([accounts[i][0]] + mergedEmails[i])

        ans.sort()
        return ans
        