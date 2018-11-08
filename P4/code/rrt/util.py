import random
from math import sqrt,cos,sin,atan2, acos

class Util:
    ########################################
    #   Mandatory functions for the rrt    #
    ########################################

    # Tests if the new_node is close enough to the goal to consider it a goal
    def winCondition(self,new_node,goal_node,WIN_RADIUS):
        """
        new_node - newly generated node we are checking
        goal_node - goal node
        WIN_RADIUS - constant representing how close we have to be to the goal to
            consider the new_node a 'win'
        """
        isWin = WIN_RADIUS > self.getDistance(new_node, goal_node)
        return isWin

    # Find the nearest node in our list of nodes that is closest to the new_node
    # Hint: If your solution appears to be drawing squiggles instead of the fractal like pattern 
    #       of striaght lines you are probably extending from the last point not the closest point!
    def nearestNode(self,nodes,new_node):
        """
        nodes - a list of nodes in the RRT
        new_node - a node generated from getNewPoint
        """
        closest_node = 0
        closest_dist = 100000000
        for n in nodes:
            dist = self.getDistance(new_node, n)
            if dist < closest_dist:
                closest_dist = dist
                closest_node = n
        # print "Close"
        # print closest_node
        return closest_node

    # Find a new point in space to move towards uniformally randomly but with
    # probability 0.05, sample the goal. This promotes movement to the goal.
    # For the autograder to work you MUST use the already imported
    # random.random() as your random number generator.
    def getNewPoint(self,XDIM,YDIM,XY_GOAL):
        """
        XDIM - constant representing the width of the game aka grid of (0,XDIM)
        YDIM - constant representing the height of the game aka grid of (0,YDIM)
        XY_GOAL - node (tuple of integers) representing the location of the goal
        """
        #return XY_GOAL
        if random.random() < 0.05:
            return XY_GOAL
        else:
            point = (random.random() * XDIM, random.random() * YDIM)
        return point

    # Extend (by at most distance delta) in the direction of the new_point and place
    # a new node there
    def extend(self,current_node,new_point,delta):
        """
        current_node - node from which we extend
        new_point - point in space which we are extending toward
        delta - maximum distance we extend by
        """
        if(self.getDistance(current_node, new_point) < delta):
            return new_point
        cx, cy = current_node
        nx, ny = new_point

        # Choose a delta within (0, 0.5 * delta)
        #delta = (random.random() + 1)/2 * delta
        #delta = random.random() * delta/2

        slope = (ny-cy)/(nx-cx)
        sq = sqrt(slope**2 + 1)
        change = delta/sq
        # print "Change"
        # print change
        # print slope

        changex = change * (nx-cx)/abs((nx-cx))
        changey = change * slope * (nx-cx)/abs((nx-cx))

        # print "New Point"
        # print (cx + changex, cy + changey)
        # print changex, changey
        # print new_point
        # print "Old Point"
        # print current_node
        # print "Delta"
        # print delta

        return (cx + changex, cy + changey)


    # iterate throught the obstacles and check that our point is not in any of them
    def isCollisionFree(self,obstacles,point,obs_line_width):
        """
        obstacles - a dictionary with multiple entries, where each entry is a list of
            points which define line segments of width obs_line_width
        point - the location in space that we are checking is not in the obstacles
        obs_line_width - the length of the line segments that define each obstacle's
            boundary
        """
        for k, val in obstacles.iteritems():
            for i in range(len(val) - 1):
                v = (val[i-1], val[i])
                dist = self.distToLine(v[0], v[1], point)
                dist1 = self.getDistance(v[0], v[1])
                dist2 = self.getDistance(v[0], point)
                dist3 = self.getDistance(v[1], point)
                if (dist >= -obs_line_width/2 and dist < obs_line_width/2 and (dist2 < dist1 and dist3 < dist1)):
                    return False
        return True


    ################################################
    #  Any other helper functions you need go here #
    ################################################

    def getDistance(self, node1, node2):
        return sqrt((node1[0] - node2[0])**2 + (node1[1] - node2[1])**2)

    def distToLine(self, linePt1, linePt2, point):
        numerator = ((linePt2[1] - linePt1[1]) * point[0] - (linePt2[0] - linePt1[0]) * point[1] + linePt2[0]*linePt1[1] \
            - linePt2[1]*linePt1[0])
        denom = sqrt((linePt2[1] - linePt1[1])**2 + (linePt2[0] - linePt1[0])**2)
        return numerator/denom

    # Find angle
    def length(self, v):
        return sqrt(self.dotproduct(v, v))

    def angle(self, v1, v2):
        return self.dotproduct(v1, v2) / (self.length(v1) * self.length(v2))

    def dotproduct(self, v1, v2):
        return sum((a * b) for a, b in zip(v1, v2))
