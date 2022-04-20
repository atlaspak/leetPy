class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = {}
        op_done = True
        
        for course in prerequisites:
            if(course[0] in course_map):
                course_map[course[0]].append(course[1])
            else:
                course_map[course[0]] = [course[1]]
            if(course[1] not in course_map):
                course_map[course[1]] = []
                
        def is_cycle(key):
            while course_map[key]:
                check_for = course_map[key].pop()
                if check_for in visited:
                    return True                    
                if course_map[check_for]:
                    visited.add(check_for)
                    return is_cycle(check_for)
            return False
        
        visited = set()
        for course in prerequisites:
            visited.add(course[0])
            if is_cycle(course[0]):
                return False
            visited.clear()
            
        return True
            
        
        
        
