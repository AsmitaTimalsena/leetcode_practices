class Solution:
    def findComplement(self, num: int) -> int:
        x = format(num, 'b')
        x_com = ''

        for i in x:
            if i == '0':
                res = '1'
                x_com = x_com + res

            if i == '1':
                res = '0'
                x_com = x_com +res

        

        return  int(x_com,2)
