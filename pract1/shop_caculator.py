def main():
   items_quantity=int(input("Number of items:"))
   total_price=0
   for i  in range (items_quantity):
       item_price=float(input("Price of item:"))
       total_price+= item_price
   if(total_price>100):
       total_price -= total_price * 10 / 100
   print("Total price for {} item is {:2f}".format(items_quantity,total_price))
main()