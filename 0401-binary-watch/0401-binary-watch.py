class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def curr(turnedOn, left):
            choices = []
            if left == 1:
                result = 1 if turnedOn else 0
                return [result]
            if turnedOn == 0:
                children_0 = curr(turnedOn, left - 1)
                return [
                    0 + child_0*2 for child_0 in children_0
                ]
            if turnedOn < left:
                
                children_0 = curr(turnedOn, left - 1 )
                children_1 = curr(turnedOn -1, left - 1)
                return [
                    child_0*2 for child_0 in children_0
                ] + [2*child_1 + 1 for child_1 in children_1]
            else: 
                children_1 = curr(turnedOn -1, left - 1)
                return [2*child_1 + 1 for child_1 in children_1]
        binary_choices = curr(turnedOn, 10)
        binary_choices.sort()
        result = []
        for c in binary_choices:
            hour = c >> 6
            minute = c & (2**6 - 1)    
            if hour >= 12 or minute >= 60:
                continue            
            r = str(hour) + ":" + str(minute).rjust(2, "0")
            result.append(r)
        return result
