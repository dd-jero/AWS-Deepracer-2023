import math

def reward_function(params):

    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    steps = params['steps']
    is_offtrack=params['is_offtrack']
    progress = params['progress']
    all_wheels_on_track = params['all_wheels_on_track']
    is_left_of_center = params['is_left_of_center']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    
    SPEED_THRESHOLD_straight=3.0 # 직진 코스에서 속도 기준
    DIRECTION_THRESHOLD = 3.0

    # 직진 웨이포인트 
    straight_waypoints=[12,13,14,15,16,17,18,19,20,21,22,23,32,33,34,
                        49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,
                        109,110,111,112,113,114,115,116,117,118,119,
                        131,132,133,134,135,136,137,138]
    
    left_waypoints = [93,94,95,152,153,154]
    right_waypoints = [125,126,127]
    center_right_waypoints = [24,25,26,27,28,29,30,31]
    
    expect_time = 10.0 # 원하는 시간 
    expect_steps = 145 # 원하는 스텝
    reward = 0.0

    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # 에이전트와 트랙의 각도 
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0]) 
    # degree로 변환
    track_direction = math.degrees(track_direction)
    # 트랙 각도와 에이전트 yaw 방향의 각도 차이 
    direction_diff = abs(track_direction - heading)

    # 차이가 너무 크면 패널티 
    direction_bonus = 1

    if direction_diff > DIRECTION_THRESHOLD or not all_wheels_on_track:

        direction_bonus=1-(direction_diff/15)

        if direction_bonus<0 or direction_bonus>1:
            direction_bonus = 0

        reward *= direction_bonus

    else:
        if next_point in (straight_waypoints):

            if speed >= SPEED_THRESHOLD_straight:
                reward += 10
            else:
                reward += 1e-3

        elif next_point in (left_waypoints):
            if is_left_of_center and ((distance_from_center/track_width)>0.25 and (distance_from_center/track_width)<0.48):
                reward += 10
            else:
                reward += 1e-3
        elif (next_point in right_waypoints):
            if (not is_left_of_center) and (distance_from_center/track_width)>0.25 and (distance_from_center/track_width)<0.48:
                reward += 10
            else:
                reward += 1e-3
        elif (next_point in center_right_waypoints):
            if (distance_from_center/track_width)<=0.25 and (not is_left_of_center):
                reward += 10
            else:
                reward += 1e-3
        else:
            if speed >= 2.0:
                reward += 10
            else:
                reward += 1e-3
    
    
    # 50steps마다 더 큰 보상 -> 더 빠르게 학습하기 위해 
    if (steps % 50) == 0 and progress >= (steps / expect_steps) * 100 :
        reward += 30.0

    # 트랙 완주에 가까워질수록 더 큰 보상 
    if progress == 100: # 완주 시
        if steps < expect_time * 15: # 기대 시간보다 15배 이내로 완주한 경우
            reward += 100 * (expect_time * 15 / steps)
        else:
            reward += 100

    elif is_offtrack: # 트랙 이탈시 
        reward -= 50   
    
    return float(reward)