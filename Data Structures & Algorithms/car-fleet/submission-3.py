class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        count = 0
        for pos, s in zip(position, speed):
            cars.append((pos, s))
        cars = sorted(cars, key = lambda x : -x[0])
        #print(cars)
        stack = []
        for pos, s in cars:
            if not stack:
                stack.append((pos, s))
                count += 1
            else:
                time1 = (target - stack[-1][0]) / stack[-1][1]
                time2 = (target - pos) / s
                if time1 >= time2:
                    continue
                else:
                    stack.pop()
                    stack.append((pos, s))
                    count += 1                
        return count
        
        

            
