calculator={'1':'1 ','2':'2 ','3':'3 ','4':'4 ','5':'5 ','6':'6 ','7':'7 ','8':'8 ','9':'9 ','0':'0 ','+':'+ ','-':'- ','*':' *','/':' /','%':' %'}
def calculatorz(calculator):
    print(calculator['1']+ '|' + calculator['2']+ '|' + calculator['3'])
    print(calculator['4']+ '|' + calculator['5']+ '|' + calculator['6'])
    print(calculator['7']+ '|' + calculator['8']+ '|' + calculator['9'])
    print(calculator['+']+ '|' + calculator['-']+ '|' + calculator['*'])
    print(calculator['/']+ '|' + calculator['%']+ '|' )
calculatorz(calculator)
print('enter no')
num=int(input())
print('enter operator')
po=input()
print('enter next number')
num2=int(input())
if(po=='+'):
     t=num+num2
elif(po=='-'):
     t=num-num2
elif(po=='*'):
     t=num*num2
elif(po=='/'):
     t=num/num2
elif(po=='%'):
     t=num%num2
elif(po=='^'):
     t=num**num2
print(' = '+str(t))
print('want to calculate more')
ans=input()
if ans=='y':
    calculatorz(calculator)
else:
    print('shut down and exiting')

    
        
    
    
            
