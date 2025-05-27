class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)

        candy = { }
        for i in candyType:
            if i in candy:
                candy[i] += 1
            else:
                candy[i] = 1
        
        # for key,value in candy.items():
        #     if value == 1:
        #         return (n // 2)
            
        # return len(candy)

        return min( len(candy), (n // 2))
      
