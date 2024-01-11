def calculateElectricRate(mon,use):
    if mon==7 or mon==8:
        return seveneight(use)
    elif mon==1 or mon==2 or mon==12:
        return onetwo(use)
    else:
        return other_mon(use)
    
def seveneight(use):
    result=0
    if use<=300:
        result=112.0*use
        return result
    elif use<450:
        result=33600+206.6*(use-300)
        return result
    elif use<1000:
        result=33600+30990+299.3*(use-450)
        return result
    else:
        result=33600+30990+164615+728.8*(use-1000)
        return result

def onetwo(use):
    if use<=200:
        result=112.0*use
        return result
    elif use<=400:
        result=22400+206.6*(use-200)
        return result
    elif use<=1000:
        result=22400+41320+299.3*(use-400)
        return result
    else:
        result=22400+41320+179580+728.8*(use-1000)
        return result
    
def other_mon(use):
    result=0
    if use<=200:
        result=112.0*use
        return result
    elif use<400:
        result=22400+206.6*(use-200)
        return result
    else:
        result=22400+41320+299.3*(use-400)
        return result
    
mon=int(input("지금은 몇월인가요?"))
user_used=int(input('사용량은 몇Kwh인가요?'))

result=calculateElectricRate(mon,user_used)
print(f'전력량요금은{result:.d}원입니다/')
