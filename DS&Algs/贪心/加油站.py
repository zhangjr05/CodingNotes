def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    '''一个环形路上有n个加油站 每个加油站有一定量的汽油 求从哪个加油站出发能够环绕一周'''

    total_tank = 0  # 所有加油站的(gas[i]-cost[i])总和
    curr_tank = 0  # 从当前起点出发的累计剩余油量
    starting_station = 0  # 可能的起始站点

    # 贪心地选择剩余油量最少的站点的下一个站作为起点
    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        curr_tank += gas[i] - cost[i]

        if curr_tank < 0:
            starting_station = i + 1  # 将油箱为负时的下一站设为新起点
            curr_tank = 0  # 重置剩余油量

    return starting_station if total_tank >= 0 else -1

# 贪心策略: 如果从站点A出发 在到达站点B时油箱为负 那么从A到B之间的任何站点出发也无法到达B之后的位置
# 直观理解: 如果从A出发在B处油箱为负，那么重新选择B之后的站点作为起点更合理，因为无论如何，从A到B这段路都需要行驶，与其一开始就亏损，不如选择在其他地方累积更多油量后再行驶这段路
