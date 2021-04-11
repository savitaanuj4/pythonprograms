from stack import Stack
#problem: WAP to reverse a given string using stacks

def solution(stri):
    s = Stack() #creates an empty stack
    for i in stri:
        s.push(i) #push each element in stack
    
    reverse =''
    while not s.is_empty():
        reverse+= s.pop() #pop each element and concatenate in reverse variable
    
    return reverse


if __name__=='__main__':
    st = 'string to reverse!'
    print(solution(st))