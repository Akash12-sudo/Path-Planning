
from controller import Robot
import math

def run_robot(robot):

    time_step = 32
    max_speed = 3
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    
    left_ir = robot.getDevice('ir_left')
    right_ir = robot.getDevice('ir_right')
    left_ir.enable(time_step)
    right_ir.enable(time_step)
    
    left1_ir = robot.getDevice('ir_left1')
    right1_ir = robot.getDevice('ir_right1')
    left1_ir.enable(time_step)
    right1_ir.enable(time_step)
    
    distance_between_wheels=8.8
    
    while robot.step(time_step) != -1:
    
        current_time = robot.getTime()
        start_time = robot.getTime()   
        turn_duration=math.pi*distance_between_wheels/(4*max_speed);
        left_ir_value = left_ir.getValue()
        right_ir_value = right_ir.getValue()
        left1_ir_value = left1_ir.getValue()
        right1_ir_value = right1_ir.getValue()
        print("left: {} left_middle: {} right_middle: {} right: {}".format(left_ir_value, left1_ir_value, right1_ir_value, right_ir_value))
        
        left_speed = max_speed
        right_speed = max_speed
        

        movement_duration = 25/max_speed
 

        
        if((left_ir_value > right_ir_value)and((left_ir_value >7 and right_ir_value<4))):
     
            left_speed = -max_speed
  
        if((left1_ir_value > 7 and right1_ir_value < 5)):
            
            left_speed = (-0.5)*max_speed
        
        if((left1_ir_value < 6 and right1_ir_value < 8)):
            right_speed = (-0.6)*max_speed
        
        if((left_ir_value < 3 and right_ir_value < 3) and (left1_ir_value <7 and right1_ir_value <4)):
            right_speed = -max_speed
            
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)       
        


if __name__ == '__main__':
    my_robot = Robot()
    run_robot(my_robot)
