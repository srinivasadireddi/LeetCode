class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        g=defaultdict(list) #adjaceny list based graph is initialzsed
        courses=prerequisites #for brevity
        UNVISITED=0
        VISITING=1
        VISITED=2
        states=[UNVISITED]*numCourses
        #create graph
        for a,b in courses:
            # g[a]=b #wrong cuz this forces a single neighbour only!
            g[a].append(b)
        
        def dfs(course):
            
            state = states[course]
            if state==VISITED:
                return True
            elif state==VISITING: #cycle
                return False 
            # state= VISITING
            states[course]= VISITING
            for nei in g[course]:
                if not dfs(nei):
                    return False
                # else:
                    # #state==VISITED
                    # states[nei]==VISITED
                    # return True
            states[course]=VISITED
            return True


        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
#TC: O(V+E)
#SC: O(V+E)