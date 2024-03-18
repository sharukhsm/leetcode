class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
   
   #Sort the array by the starting values of the intervals
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]] #example 1: merged = [[1,3]]

        for interval in intervals:
    #If the ending value of the first interval is less than the starting value of the second interval.
            if merged[-1][1] < interval[0]: 
                merged.append(interval)
            else:
    #If the ending value of the first interval is greater than the starting value of the second interval.
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

#we sort by starting values bc intervals can be in any order.
# The logic here is if the second value of the first interval is less than the first value of the second interval append it to the merged list, else there is a merge/overlap, now compare the second value of the merged list to the second value of the interval and update the second value of  
#merged[-1][1]: 
#here [-1]: last array of the merged list -> [1,3]. 
#here [1]: gives the ending value of the array.
#merged[-1][1]: [1,3]->3
#Syntax: merged[lastArray][endingValue]
# interval = [1,3]
# interval[0] = [1]

# Note: in else, the first iteration in the merged list will compare to the first iteration itself, 
# it's only a one ecxtra iteration, so it's not a big deal.