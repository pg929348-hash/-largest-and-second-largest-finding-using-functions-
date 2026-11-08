def second_bigggest(a):
          largest=a[0]     
          second=a[1]
          for i in a:
              if i>largest:
                    second=largest
                    largest=i
              elif i>second and i !=largest:
                    second=i
                    
          return largest,second
a=[1,2,3,4,5]
print(second_bigggest(a))
a=[99, 1, 5]
print(second_bigggest(a))
a=[5,4,3,2,1]
print(second_bigggest(a))
a=[5, 5, 3]
print(second_bigggest(a))
a=[7, 2]
print(second_bigggest(a))

