'''
ex02.py

1.신용카드의 16자리 숫자에서 맨 우측 수부터 세어 홀수 번째 수는 그대로 두고, 짝수 번째 수를 2배로 만든다.
2.2배로 만든 짝수 번째 수가 10 이상인 경우, 각 자리의 숫자를 더하고 그 수로 대체한다.
3.이와 같이 얻은 모든 자리의 수를 더한다.
4.그 합이 10으로 나뉘면 “정당한 번호”(유효)이고 그렇지 않으면 “부당한 번호”(유효하지 않음)로 판정된다.

ex)
2720992711828767    T
3444063910462763    F
o o o o o o o o
6011733895106094    T
'''
def cardnumber(word):
    if len(word) != 16:
        return False
    
    total = 0
    for i in range(len(word) - 1, -1, -1):        
        if i % 2 == 0:
            num = int(word[i])
            num = num * 2            
            if num >= 10:
                num = num // 10 + num % 10
                total += num                
            else:
                total += num                
        else:
            total += int(word[i])
        
    return (total % 10 == 0) and 'This is valid card number.' or 'This is invalid card number.'
    
        

print(cardnumber('2720992711828767'))
print(cardnumber('1234567812345678'))