def check(str1, str2): 
  
    n1 = len(str1)  
    n2 = len(str2) 
   
    if (n1 < n2): 
        return True
    if (n2 < n1): 
        return False
   
    for i in range(n1): 
        if (str1[i] < str2[i]): 
            return True
        elif (str1[i] > str2[i]): 
            return False
   
    return False



def subt(str1, str2): 
  

    if (check(str1, str2)): 
        aux = str1 
        str1 = str2 
        str2 = aux 
   
   
    str3 = "" 
   
    n1 = len(str1)  
    n2 = len(str2) 
   
 
    str1= str1[::-1] 
    str2 = str2[::-1] 
  
    carry = 0


    for i in range(n2): 
      

           
        sub = ((ord(str1[i])-ord('0'))-(ord(str2[i])-ord('0'))-carry) 
          
        if (sub < 0): 
          
            sub = sub + 10
            carry = 1
              
        else: 
            carry = 0
  
        str3 = str3+str(sub ) 
          
    
    for i in range(n2,n1): 
      
        sub = ((ord(str1[i])-ord('0')) - carry) 
           
      
        if (sub < 0): 
          
            sub = sub + 10
            carry = 1
          
        else: 
            carry = 0
               
        str3 = str3+str(sub) 
   
  
    str3= str3[::-1] 
   
    return str3 


n1 = "1230434"
n2 = "12303940394"
print(subt(n1, n2)) 

