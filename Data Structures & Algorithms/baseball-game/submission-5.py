class Solution:
    def calPoints(self, operations):

        st = []

        for op in operations:

            if op.lstrip("-").isdigit():
                st.append(int(op))

            elif op == "+":
                st.append(st[-1] + st[-2])

            elif op == "D":
                st.append(2 * st[-1])

            elif op == "C":
                st.pop()

        return sum(st)