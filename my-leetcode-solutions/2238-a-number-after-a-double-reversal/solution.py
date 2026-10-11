class Solution:
    def isSameAfterReversals(self, num: int) -> bool:

        string_num = str(num)
        string_rev = string_num[::-1]
        rev = int(string_rev)

        string_rev = str(rev)
        string_rev_2 = string_rev[::-1]
        rev_2 = int(string_rev_2) 
        
        if(num == rev_2):
            return True
        else:
            return False
                           
