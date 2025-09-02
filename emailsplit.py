while True:
 if True:
  try:
   email=input("enter  your email:")
   index=email.index("@")
   username=email[:index]
   domain=email[index:]
   print(f"username:{username} and domain:{domain}")
   break
  except ValueError:
   print("invalid email")
 