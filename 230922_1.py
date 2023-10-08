def reward_function(params):

    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    is_left_of_center = params['is_left_of_center']
    closest_waypoints = params['closest_waypoints']
    steps = params['steps']
    progress = params['progress']
    expect_time = 10.0 # 원하는 시간 
    expect_steps = 145 # 원하는 스텝
    is_offtrack = params['is_offtrack']
    
    # 최적 주행을 위한 
    right = [120,121,122,123,124,125,126,127,128,129,130,131,132] #완
    
    center_right = [20,21,22,23,24,25,26,27,28,29,30,
                    118,119,
                    133,134] # 완 
    
    left = [7,8,9,10,11,12,13,
            33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,
            85,86,87,88,89,90,
            100,101,102,103,104,105,106,107,108,109,110,
            139,140,141,142,143,144,145,146,147,148,149,150]
    
    center_left = [1,2,3,4,5,6,
                   16,17,18,31,32,
                   52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,
                   70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,
                   91,92,93,94,95,96,97,98,99,
                   111,112,113,114,115,116,117,
                   135,136,137,138,151,152,153,154]

    
    fast_speed = [2,3,4,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,
                  47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,
                  68,69,70,71,72,73,74,75,76,77,78,79,80,
                  96,97,98,99,100,101,102,103,104,105,106,107,
                  110,111,112,113,114,115,116,117,118,
                  123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,
                  152,153,154]
    
    medium_speed = [1,5,6,7,8,9,10,11,12,13,
                    34,35,36,37,38,39,40,41,42,43,44,45,46,
                    81,82,83,86,87,88,89,90,91,92,93,94,95,
                    108,109,119,120,121,122,
                    141,142,143,144,145,146,147,148,149,150,151]
    
    slow_speed = [84,85,139,140]
    
    reward = 0.0
    next_point = max(closest_waypoints[0], closest_waypoints[1])

    # 패널티를 주는 것보다 아주 작은 보상을 부여하는데 학습의 안정성과 수렴성에 좋을 것이라고 판단
    # 차이가 너무 크면 패널티 
    if not is_offtrack:
        if next_point in right:
            if (not is_left_of_center) and (distance_from_center/track_width) > 0.25 and (distance_from_center/track_width) <0.48:
                reward += 10
            else:
                reward += 1e-2
        elif next_point in left:
            if (is_left_of_center) and (distance_from_center/track_width) > 0.25 and (distance_from_center/track_width) <0.48:
                reward += 10
            else:
                reward += 1e-2

        elif next_point in center_right:
            if (not is_left_of_center) and (distance_from_center/track_width <=0.25):
                reward += 10
            elif (is_left_of_center) and (distance_from_center/track_width <=0.25):
                reward += 1e-1
            else:
                reward += 1e-2

        elif next_point in center_left:
            if (is_left_of_center) and (distance_from_center/track_width <=0.25):
                reward += 10
            elif (not is_left_of_center) and (distance_from_center/track_width <=0.25):
                reward += 1e-1
            else:
                reward += 1e-2

        if next_point in fast_speed:
            if speed == 3:
                reward += 10
            else:
                reward += 1e-2

        elif next_point in medium_speed:
            if speed == 2 :
                reward += 10
            else:
                reward += 1e-2

        elif next_point in slow_speed:
            if speed == 1:
                reward += 10
            else:
                reward += 1e-2
    else:
        reward -= 50

    # 50steps마다 더 큰 보상 -> 더 빠르게 학습하기 위해 
    if (steps % 50) == 0 and progress >= (steps / expect_steps) * 100 :
        reward += 10*(steps%50)

    # 트랙 완주에 가까워질수록 더 큰 보상 
    if progress == 100: # 완주 시
        if steps < expect_time * 15: # 기대 시간보다 15배 이내로 완주한 경우
            reward += 100 * (expect_time * 15 / steps)
        else:
            reward += 100
        
    
    return float(reward)