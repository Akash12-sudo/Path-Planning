# Path-Planning
import math
from controller import Robot
robot = Robot()
timestep = int(robot.getBasicTimeStep())
left_motor=robot.getDevice('left wheel motor')
right_motor=robot.getDevice('right wheel motor')
right_motor.setPosition(float('inf'))
right_motor.setVelocity(0.0)
left_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
velocity=5.0
distance_between_wheels=8.8

def move(last,now):
    print(now)
    if(last==now):
        pass
    elif((last=='U' and now=='R') or (last=='R' and now=='D') or (last=='D' and now=='L') or(last=='L' and now=='U')):
        rotate(1)
    
    else:
        rotate(0)
    movement_duration=25/velocity;
    start_time=robot.getTime()
    current_time=robot.getTime()
    right_motor.setVelocity(5.0)
    left_motor.setVelocity(5.0)
    while robot.step(timestep) != -1:
        if((current_time-start_time>movement_duration)):
            break;
        current_time=robot.getTime();
    right_motor.setVelocity(0.0)
    left_motor.setVelocity(0.0)
    
def rotate(direction):
    turn_duration=math.pi*distance_between_wheels/(4*velocity);
    start_time=robot.getTime()
    current_time=robot.getTime()
    if(direction==1):
        right_motor.setVelocity(-1*velocity)
        left_motor.setVelocity(velocity)
        while robot.step(timestep) != -1:
            if((current_time-start_time>turn_duration)):
                break;
            current_time=robot.getTime();
        right_motor.setVelocity(0.0)
        left_motor.setVelocity(0.0)
    else:
        right_motor.setVelocity(velocity)
        left_motor.setVelocity(-1*velocity)
        while robot.step(timestep) != -1:
            if((current_time-start_time>turn_duration)):
                break;
            current_time=robot.getTime();
        right_motor.setVelocity(0.0)
        left_motor.setVelocity(0.0)
        
class node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        


goal = node(4, 6)


def calc_heuristic(n1, n2):
    #Diagonal distance
    h = max(abs(n1.x-n2.x),abs(n1.y-n2.y))
    return h
            

        
def start():
    board=[[1,0,-1,0,0,0,0],
           [0,-1,-1,-1,0,-1,0],
           [0,-1,-1,0,0,0,0],
           [0,-1,0,0,0,-1,0],
           [0,0,0,-1,-1,0,0]]
           
    stack=[[0,0]]
    while robot.step(timestep) != -1:
        if(len(stack)==0):
            break
        temp=[]
        for i in stack:
            x = i[0]
            y = i[1]

            val = board[x][y] + 1
            n1 = node(x + 1, y)
            n2 = node(x - 1, y)
            n3 = node(x, y + 1)
            n4 = node(x, y - 1)

            if x + 1 < 5 and board[x + 1][y] != -1 and (board[x + 1][y] > val or board[x + 1][y] == 0):
                temp.append([x + 1, y])
                board[x + 1][y] = val + abs(calc_heuristic(goal, n1))
   

            if x - 1 >= 0 and board[x - 1][y] != -1 and (board[x - 1][y] > val or board[x - 1][y] == 0):
                temp.append([x - 1, y])
                board[x - 1][y] = val + abs(calc_heuristic(goal, n2))


            if y + 1 < 7 and board[x][y + 1] != -1 and (board[x][y + 1] > val or board[x][y + 1] == 0):
                temp.append([x, y + 1])
                board[x][y + 1] = val + (calc_heuristic(goal, n3))
     

            if y - 1 >= 0 and board[x][y - 1] != -1 and (board[x][y - 1] > val or board[x][y - 1] == 0):
                temp.append([x, y - 1])
                board[x][y - 1] = val + abs(calc_heuristic(goal, n4))
        stack = temp
    print(board)
    if(board[4][6]==0):
        print("Cannot reach Destination");
    path=""
    point=[4,6]
    while robot.step(timestep) != -1:
        x=point[0]
        y=point[1]
        temp_node = node(x, y)
        
        val = round((board[x][y] - calc_heuristic(goal, temp_node)-1), 3)
        print(val)
        if(val==1):
            if(x-1>=0 and round(board[x-1][y],3)==val):
                path="D"+path
            if(y-1>=0 and round(board[x][y-1],3)==val):
                path="R"+path
            break
        if(x+1<5 and round(board[x+1][y],3)==val):
            path="U"+path
            point[0]+=1
            continue
        if(x-1>=0 and round(board[x-1][y],3)==val):
            path="D"+path
            point[0]-=1
            continue
        if(y+1<7 and round(board[x][y+1],3)==val):
            path="L"+path
            point[1]+=1
            continue
        if(y-1>=0 and round(board[x][y-1],3)==val):
            path="R"+path
            point[1]-=1
            continue
    print(path)
    for i in range(len(path)):
        if(i==0):
            move("D",path[i])
        else:
            move(path[i-1],path[i])
    
if __name__=="__main__":
    start();
    
