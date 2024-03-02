def reverse(num):
  L=[]
  x=str(num)
  L1=list(x)

  for i in L1:
    L.insert(0,i)
    print ('the reversed num is:')

  x=''
  for i in L:
    x.join(i)
    return x
