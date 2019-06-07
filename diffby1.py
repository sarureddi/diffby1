aa2,b2=map(str,input().split())
count1=0
for i1 in range(0,len(aa2)):
  if(aa2[i1]!=b2[i1]):
    count1=count1+1
if(count1==1):
  print("yes")
else:
  print("no")
