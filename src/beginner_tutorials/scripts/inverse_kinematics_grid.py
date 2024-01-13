#!/usr/bin/env python3import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import math

def ik2dof(x,y):

    theta2=math.acos((x**2 + y**2 - 0.545**2 - 0.60**2)/(2*0.545*0.60))
    theta1= math.atan(y/x) + math.atan((0.6* math.sin(theta2))/(0.545+0.6*math.cos(theta2)))

    first=90-math.degrees(theta1)
    second=math.degrees(theta2)-90   
    
    return first,second


def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

def vector_magnitude(v):
    return math.sqrt(sum(x**2 for x in v))

def angle_between_vectors(v1, v2):
    dot_prod = dot_product(v1, v2)
    magnitude_v1 = vector_magnitude(v1)
    magnitude_v2 = vector_magnitude(v2)

    cos_theta = dot_prod / (magnitude_v1 * magnitude_v2)
    
    # Ensure cos_theta is within the valid range [-1, 1] to avoid arccosine domain errors
    cos_theta = max(min(cos_theta, 1.0), -1.0)

    # Use arccosine to find the angle in radians
    angle_rad = math.acos(cos_theta)

    # Convert radians to degrees
    angle_deg = math.degrees(angle_rad)
    
    return angle_deg

def foot_of_perpendicular(point, line_point1, line_point2):
    """
    Finds the foot of the perpendicular from a point to a 3D line.

    Args:
        point: The coordinates of the point (x, y, z).
        line_point1: The coordinates of one point on the line (x1, y1, z1).
        line_point2: The coordinates of another point on the line (x2, y2, z2).

    Returns:
        The coordinates of the foot of the perpendicular (x_foot, y_foot, z_foot).
    """

    line_direction = line_point2 - line_point1
    point_to_line = point - line_point1

    # Project the point onto the line direction
    projection = np.dot(point_to_line, line_direction) / np.dot(line_direction, line_direction) * line_direction

    # Add the projection to the first line point to get the foot of the perpendicular
    foot = line_point1 + projection

    return foot

def ik(p,q,r,a,b,c): 
    """doing calculations for point2 after multiplying by 100 because that seems to be more accurate probably because how python handles floating point numbers,
    could try this with everything but the normal vector will have to stay a unit so will have to account for that too, mendoksai, seems to work for now
    
    base angle probably needs work, will see later"""

    Target=np.array([p,q,r])
    N=np.array([a,b,c])
    N=N/np.linalg.norm(N) #normalizwd

    point1=Target + 0.1*N #have taking this in cm, will probably change to m
    
    #generating points for point2
    num_points = 9999999
    
    radii = 4.3
    #putting values into eqn

    point1=point1*100
    
    x_values = np.random.uniform(point1[0]-5,point1[0]+5, num_points)
    y_values = np.random.uniform(point1[1]-5,point1[1]+5, num_points)
    
    values= (x_values-point1[0])**2  + (y_values-point1[1])**2+(((a*(point1[0]-x_values) + b*(point1[1]-y_values))**2)/(c*c)) - (radii*radii)
    # Filter points that satisfy the equation within a certain tolerance
    tolerance = 0.01
    valid_points = np.where(np.abs(values) < tolerance)

    valid_x = x_values[valid_points]
    valid_y = y_values[valid_points]

    # Calculate the Euclidean dis  tance to the origin for each valid point
    distances = np.sqrt(valid_x**2 + valid_y**2)
    
    # Find the index of the point with the minimum distance
    min_distance_index = np.argmin(distances)

    # Extract the coordinates of the point with the minimum distance
    m = valid_x[min_distance_index]/100
    n = valid_y[min_distance_index]/100
    l= ((a*(point1[0]-m) + b*(point1[1]-n))/c + point1[2])/100

    point2=[m,n,l]

    point1=point1/100

    base=angle_between_vectors([1,0,0],[point2[0],point2[1],0])
    x_apparent=math.sqrt(point2[0]**2 + point2[1]**2) - 0.04
    
    z_apparent=point2[2]-0.155
    # print("apparent", x_apparent, z_apparent)
    first,second = ik2dof(x_apparent, z_apparent)

    joint_pos_apparent = [0.545 * math.sin(math.radians(first)), 0.545*math.cos(math.radians(first)) ]

    # print("joint apparent", joint_pos_apparent)
    joint_pos=np.array([(joint_pos_apparent[0]+0.04)* math.cos(math.radians(base)), (joint_pos_apparent[0]+0.04)* math.sin(math.radians(base)), joint_pos_apparent[1]+0.155])
    
    # print("actual joint position= ",joint_pos)
    # print('joints=', base, first, second)

    arm2_vec=point2-joint_pos
    arm2_vec=arm2_vec/np.linalg.norm(arm2_vec)

    p2_p1_vec= point1-point2
    p2_p1_vec=p2_p1_vec/np.linalg.norm(p2_p1_vec)

    angle2=angle_between_vectors(p2_p1_vec, arm2_vec)
    
    #normal through plane for point2 and z-axis
    norm2=[-point2[1], point2[1],0]
    norm2=norm2/np.linalg.norm(norm2)


    #finding angle 1
    ft=foot_of_perpendicular(Target, point2, joint_pos) 
    
    pq=ft-Target
    pq=pq/np.linalg.norm(pq)
    #perp vector from line to point1

    #for normal of arm2
    ft2=foot_of_perpendicular(np.array([0.04*math.cos(math.radians(base)),0.04*math.sin(math.radians(base)),0]), point2, joint_pos)
    norm_arm2=ft2/np.linalg.norm(ft2)

    angle1=angle_between_vectors(pq,norm_arm2)

    # print("Target=", Target)
    # print("normal= ", N )
    # print("point1=", point1)
    # print("point2=", point2)
    # print("Joint pos apparent =", joint_pos_apparent)
    # print("joint pos= ", joint_pos)
 
    
    return base, first, second, angle1, angle2
