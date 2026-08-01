class Solution(object):
    def isValid(self, s):
        stack=[]
        mapping ={")":"(","}":"{", "]":"[" }
        for i in s:
            if i in mapping:
                top_elem=stack.pop() if stack else "#"

                if mapping[i] != top_elem:
                    return False

            else:   
                stack.append(i)

        return not stack