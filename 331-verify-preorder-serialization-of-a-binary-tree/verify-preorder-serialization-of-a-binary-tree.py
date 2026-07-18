class Solution:
    def isValidSerialization(self, preorder):
        nodes = preorder.split(",")
        slots = 1  # start with one slot for the root
        
        for node in nodes:
            slots -= 1  # every node uses one slot
            if slots < 0:
                return False
            if node != "#":
                slots += 2  # non-null node creates two slots
        
        return slots == 0
