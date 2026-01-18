def coinChange (coins, amount):
    solution=[amount+1]*(amount+1)
    solution[0]=0

    last_coin=[0]*(amount+1)
    min_coin_list=[]
    currentAmount=amount

    for i in range (0, amount+1):
        for coin in coins:
            if coin<=i:
                if solution[i] >= (solution[i-coin]+1):
                    solution[i] = solution[i-coin]+1
                    last_coin[i]=coin 

    if solution[amount]>amount:
        return -1

    while currentAmount>0:
        min_coin_list.append(last_coin[currentAmount])
        currentAmount-=last_coin[currentAmount]
        

    return solution[amount], min_coin_list


print(coinChange([1, 4, 6], 9))

