from random import randint
quick_picks=int(input("How many quick picks:"))
quick_picks_list=[[randint(1,45)for number in range(0,6)]for i in range(0,quick_picks)]
for quick_picks in quick_picks_list:
    (quick_picks.sort())
    print(str(quick_picks)[1:-1])