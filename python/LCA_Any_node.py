# https://www.geeksforgeeks.org/least-common-ancestor-of-any-number-of-nodes-in-binary-tree/


def findKLCA(root, keyNodes):
	nodesSet = set(keyNodes)
	self.res = None
	def helper(root):
		if not root:
			return 0

		matchNodes += helper(root.left) + helper(root.right)
		if root.val in nodesSet:
			matchNodes += 1
		if matchNodes == len(nodesSet):
			self.res = root
		return matchNodes
	return self.res
