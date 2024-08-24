s=""

t=""
k=0


m=min(len(s),len(t))
if len(s)==0 or len(t)==0:
    if max(len(s),len(t))<=k:
        print("Yes")
    else:
        print("No")
for i in range(m):
    if s[i]!=t[i] :
        ch1=s[i::]
        ch2=t[i::]

        if (len(ch1)+len(ch2))>k:
            print ("No")
        else:
            print ("Yes")
    if i==(m-1):
        ch1=s[i+1::]
        ch2=t[i+1::]

        if (len(ch1)+len(ch2))>k:
            print ('No')
        else:
            print ("Yes")



