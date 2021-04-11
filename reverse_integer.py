t = int(input())

for i in range(t):
    temp_input = input().split()
    var = temp_input[0] - temp_input[1]
    if var >temp_input[2]:
        print("Case #{i}:" var)
    else:
        print(f"Case #{i}:", var-temp_input[2]+1)
