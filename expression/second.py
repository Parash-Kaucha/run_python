# 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total
# wholesale cost for 60 copies?

cover_price = 24.95
discount_percent = 40
normal_shipping_cost = 3
additional_shipping_cost = 0.75
total_copies = 60

additional_copies = total_copies - 1
cost_after_discounted_price = (cover_price-(cover_price*40/100))*total_copies
print(cost_after_discounted_price)
final_cost = cost_after_discounted_price + additional_shipping_cost*additional_copies + normal_shipping_cost

print(f"The final cost for {total_copies} is ${final_cost}" )