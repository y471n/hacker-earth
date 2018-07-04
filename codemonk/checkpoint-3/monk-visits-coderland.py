test_cases = int(input())

for i in range(test_cases):
    n = int(input())
    price_list = list(map(int, input().split()))
    quantity_list = list(map(int, input().split()))
    cost = 0
    end = n
    local_min_price = min(price_list)
    while local_min_price < price_list[0]:
        k = price_list.index(local_min_price)
        cost = cost + local_min_price * sum(quantity_list[k:end])
        local_min_price = min(price_list[0:k])
        end = k
    cost = cost + local_min_price * sum(quantity_list[:end])
    print(cost)
