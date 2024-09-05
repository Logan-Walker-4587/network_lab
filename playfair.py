def search(mat, element):
    for i in range(5):
        for j in range(5):
            if(mat[i][j] == element):
                return i, j


key = input("Enter a key : ")
plain_text = input("Enter a plain text : ")
plain_text = plain_text.replace(" ","x")
new_text = ""

for i in range(len(plain_text)):
        if i<len(plain_text)-1 and plain_text[i]==plain_text[i+1]:
            new_text += plain_text[i]
            new_text += 'x'
            i+=1
        else:
            new_text += plain_text[i]
if (len(plain_text)%2==1):
    new_text+= 'x'
text_before = new_text
for i in range(len(new_text)):
        if new_text[i]=='j':
            new_text[i]='i'
plain_text = new_text

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
digraph = []
group = 0
matrix = []

for i in range (2,len(plain_text),2):
        digraph.append(plain_text[group:i])
        group = i
        
digraph.append(plain_text[group:])

key_letters = []

for i in range (0,len(key)):
        if key[i] not in key_letters:
             key_letters.append(key[i])
        
print (f"plain text = {plain_text} and key letters = {key_letters}")
print (f"digraph is {digraph}")

count = 0
row_list = []

for letter in key_letters:
        if count<5:
           row_list.append(letter)
           count+=1
        if count == 5:
           matrix.append(row_list)
           row_list = []
           count = 0
for letter in list1:
         if letter not in key_letters:
           if count<5:
               row_list.append(letter)
               count+=1
           if count==5:
               matrix.append(row_list)
               row_list = []
               count = 0

print(f"matrix is {matrix}")

row_count = 0
col_count = 0
i = 0
ciphertext = ""

#print (f"digraph elements are {digraph[0][0]} {digraph[0][1]}")
for i in range (len(digraph)):
       if len(digraph[i])==0:
             break
       if len(digraph[i])!=0:
             row1,col1 = search(matrix,digraph[i][0])
       if len(digraph[i])==2:
             row2,col2 = search(matrix,digraph[i][1])
       
       
       if row1==row2 :
            #print(f"{digraph[i][0]} and {digraph[i][1]} are in same row")
            if col1!=4  and col2 != 4:
                ciphertext += matrix[row1][col1+1]
                ciphertext += matrix[row2][col2+1]
            else :
                if col1==4:
                     ciphertext += matrix[row1][0]
                     ciphertext += matrix[row2][col2+1]
                else:
                     ciphertext += matrix[row1][col1+1]
                     ciphertext += matrix[row2][0]                   
       elif col1==col2 :
            #print(f"{digraph[i][0]} and {digraph[i][1]} are in same col")
            if row1!=4  and row2 != 4:
                ciphertext += matrix[row1+1][col1]
                ciphertext += matrix[row2+1][col2]
            else :
                if row1==4:
                     ciphertext += matrix[0][col1]
                     ciphertext += matrix[row2+1][col2]
                else:
                     ciphertext += matrix[0][col2]
                     ciphertext += matrix[row1+1][col1]
       else:
               #print(f"{digraph[i][0]} and {digraph[i][1]} are diagonals")
               ciphertext += matrix[row1][col2]
               ciphertext += matrix[row2][col1]
               
print(f"Cipher text = {ciphertext}")
                     
        
#Key text: Monarchy
#Plain text: instruments
#Cipher text: gatlmzclrqtx          
       
