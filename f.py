M=raw_input()
if .isalpha():
 print("invalid")
else:
  M=int(M)
  count=0
    while M!=0:
      M=int(M/10)
      count=count+1
   print(count)
