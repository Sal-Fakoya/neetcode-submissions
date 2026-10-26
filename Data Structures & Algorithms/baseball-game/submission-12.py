
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # create a new record and start with zero
        record = [0]
        
        # get length of operations
        length = len(operations) 


        if length == 0:
            return 0

        else:
            for i in range(0, length):
                score = operations[i]

                # if score is an operator
                if score == "C":
                    record.pop()
                elif score == "D":
                    record.append(int(record[-1]) * 2)
                elif score == "+":
                    two_nums = record[-1] + record[-2]
                    record.append(two_nums)
                else:
                    # apparently, negative numbers are not numeric numbers
                    record.append(int(score))

            return sum(record)














