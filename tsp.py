import math
class TravelingSalesmanProblem:
    def euclidian_distance(self,first_point,second_point):
        x1,y1=first_point
        x2,y2=second_point
        return math.sqrt((x2-x1)**2+(y2-y1)**2)
    
    def rout_finding(self,starting_point,list_anotherPoints):
        points_remaining=list_anotherPoints.copy()
        location_rightNow=starting_point
        best_optimalRout=[starting_point]

        while points_remaining:
            next_location=min(points_remaining,key=lambda city:self.euclidian_distance(location_rightNow,city))
            points_remaining.remove(next_location)
            best_optimalRout.append(next_location)
            location_rightNow=next_location
        return best_optimalRout    
    
    def insert_file(self,rout,filename):
        with open(filename,'w') as file:
            for terget in rout:
                file.write(f"({terget[0]},{terget[1]})")

tsp=TravelingSalesmanProblem()

start_uttaraBranch=(23.8728568,90.3984184) 
rest_branches=[
    (23.8513998,90.3944536),
    (23.8330429,90.4092871),
    (23.8679743,90.3840879),
    (23.8248293,90.3551134),
    (23.827149,90.4106238),
    (23.8629078,90.3816318),
    (23.8673789,90.429412),
    (23.8248938,90.3549467),
    (23.813316,90.4147498)
]

expected_rout=tsp.rout_finding(start_uttaraBranch,rest_branches)
tsp.insert_file(expected_rout,'optimal_rout.txt')
print(expected_rout)