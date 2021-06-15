#配列の中の数字がtargetと一致している物を探し、返す。
#case [2,7,11,15] target 9  return [0,1]

#solution use Hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        temp = 0
        
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in map:
                return [map[temp],i]
            
            map[nums[i]] = i
            
        return 

