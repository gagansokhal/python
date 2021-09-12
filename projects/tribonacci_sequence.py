def tribonacci(signature, n):
    i=0
    if n > len(signature):
        for i in range(n-3):
            signature.append(signature[-1]+signature[-2]+signature[-3])
            i+=1
        return signature
            
    else: 
        j=0
        new_lst=[]
        for j in range (0,n):
            new_lst.append(signature[j])
            j+=1
        return new_lst
