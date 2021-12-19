class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = [ ]

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])

            else:
                subst = "" # to store string
                k= "" # for int

                #print(stack)
                while stack[-1] != '[':

                    subst = stack.pop() + subst

                stack.pop()

                while stack and  stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(int(k) * subst)

        return "".join(stack)

        