# 제3회 대한민국 인공지능 융합 자율주행 경진대회 
# [AWS DeepRacer Championship]  
--온라인 예선전--
1. Classic Race / Live Race : Classic Race
2. Choose race type : Time Trial
3. Name of the racing event : 2023 AWS DeepRacer Championship(ITP)
4. Choose race dates : 9/1(금) ~ 9/10(일)
5. Ranking Method : Total time
6. Competition tracks : Smile Speedway (re:invent 2019)
7. Minimum laps => 5 consecutive Laps
8. Off-track penalty => 3 seconds

Reward Function: 230907_4.py
  - 트랙 웨이포인트 분석을 이용한 보상
  - 트랙 각도와 에이전트 YAW 방향의 각도 차이에 대한 보상
  - 기대 완주 스텝, 기대 완주 시간, 트랙 진행율에 따른 보상
  - off track 시 큰 패널티
    
알집파일: 모델의 로그

온라인 예선 결과
5위(본선진출), 48.189s
![image](https://github.com/dd-jero/AWS-Deepracer-2023/assets/107921434/a6904bd5-3e0e-4e3b-80af-fa081cacb839)  
![ezgif com-optimize](https://github.com/dd-jero/AWS-Deepracer-2023/assets/107921434/cc84d1a5-2b9d-45c7-b2a3-717dbbc81064)  

--오프라인 본선전--
1. Race: Smile Speedway
2. Time Trial
3. 3분동안의 최단 lap time이 기록으로 결정 (총 2번)

Reward Function: 230922_1.py
  - 온라인, 오프라인 주행은 약간 다름
  - 완주율 높게 학습해야함.
    
오프라인 본선 결과  
1차 시기: 1위  
2차 시기: 3위  
최종: 3위(인천광역시장상), 10.250 => 빠르되 완주율 높게  
![image](https://github.com/dd-jero/AWS-Deepracer-2023/assets/107921434/227749b7-05f7-4895-8492-49a5fa0ae287)



