import time as t
class Search:
    def search(self,a,b):
      d=False
      for i in range(len(a)):
          if(b==a[i]):
              print("FOUNDDD!!!!!! index=",i)
              d=True
      if(d==False):
          print("We are Sorry to inform you that the search resulted in NOTHINGG!")


    def time(self,a,b):
        t1=t.time()
        self.search(a,b)
        t2=t.time()
if __name__=='__main__':
  try:
    n=int(input("Eneter the size of the list")) 
    g=[]
  except ValueError:
    print("Please Enter a valid Integer!")
  for i in range(n):
    g.append(input("Enter the Content for the List"))
  m=input("Enter the value to be searched")
  s=Search()
  s.time(g,m)