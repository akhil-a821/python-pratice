while True:
    try:
      symbol=input("enter the symbol:")
      row=int(input("enter the number of rows:"))
      for i in range (row+1):
        print(" "*(row-i)+f"{symbol}"*((2*i)-1))
    except ValueError:
          print("Please enter a valid integer for the number of rows.")
          