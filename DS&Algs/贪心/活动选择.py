def activity_selection(start: list[int], finish: list[int]) -> int:
    '''给定n个活动 每个活动有开始时间和结束时间 求最多可参加多少个活动'''
    n = len(start)
    
    # 按结束时间排序 每次选择结束最早且不冲突的活动
    activities = sorted(zip(start, finish), key=lambda x: x[1])

    ans = 1  # 最多可参加的活动数
    last_finish = activities[0][1]  # 选择第一个活动 结束时间

    for i in range(1, n):
        if activities[i][0] >= last_finish: # 不冲突 可选
            ans += 1
            last_finish = activities[i][1]
    
    return ans

# 贪心策略： 按活动结束时间排序，每次选择结束最早且不与已选活动冲突的活动