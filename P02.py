n = int(input("masukkan n: "))
win_count = 0
lose_count = 0
draw_count = 0

for i in range(1, n + 1):
    result = input("hasil match " + str(i) + ":")
    if result == "win":
        win_count += 1
    elif result == "lose":
        lose_count += 1
    elif result == "draw":
        draw_count += 1

print("mr. mik won " + str(win_count) + " times out of " + str(n) + " matches")

most_frequent = "win"
max_count = win_count
if lose_count > max_count:
    most_frequent = "lose"
    max_count = lose_count
if draw_count > max_count: 
    most_frequent = "draw"
    max_count = draw_count
    
print("the most frequent result is " + most_frequent)