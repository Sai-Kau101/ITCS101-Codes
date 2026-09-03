money = 2560
print("Money to be deposited =", money)
thousand = money // 1000
thousand_change = thousand % 1000

five_h = thousand_change // 500
five_change = five_h % 500

print("1000 =", thousand)
print("500 =", five_h)
