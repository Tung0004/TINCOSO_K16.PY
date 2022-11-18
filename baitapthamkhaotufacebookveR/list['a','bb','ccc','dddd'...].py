A=["a","b","c","d","e","f","g","h","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
B=[]
for i in range(len(A)):
    B.append((i+1)*A[i])
    print(B[i])
    