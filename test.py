def max_profit(price, n):
    # Khởi tạo mảng dp với n+1 phần tử, ban đầu là 0
    dp = [0] * (n + 1)
    l=[]

    # Tính giá trị lớn nhất cho mỗi độ dài từ 1 đến n
    for i in range(1, n + 1):
        max_val = 0
        for j in range(i):
            max_val = max(max_val, price[j] + dp[i - j - 1])
            if max_val > max(dp):
                l.append(j)
        dp[i] = max_val
    
    return dp[n],l

price = [1, 5, 8, 12, 13, 17, 20, 22]

# Chiều dài đoạn dây
n = 8


# Tính lợi nhuận tối đa
result = max_profit(price, n)
print(f"Lợi nhuận tối đa có thể đạt được: {result} VNĐ")
