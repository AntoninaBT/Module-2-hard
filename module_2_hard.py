# Teplova //
n = int(input("Enter a number from 3 to 20: ")) # input 3 to 20, transfer to a number - use int
password = ''
#1
for i in range(1,n): # i from 1 to n. n - entered number from the user
    for j in range(i, n): #  the second number from i to the entered number
        if n % (i+j) == 0 and i != j: # remember i != j and the sum of i and j has aт integer division
            password = password + str(i) + str(j) # need to stick two numbers and transfer to a string
print(n, "password:", password)
#2
while n >= 3 and n < 21: # the number is restricted
    password = ""
    for i in range(1,n):
        for j in range(i+1,n):
            if n % (i+j) == 0:
                password = password+ str(i) + str(j)
    print(n, "пароль:", password)
    break
#3
def get_password(n):
    password = ''
    for i in range(1, n):
        for j in range(i+1, n):
            if n % (i + j) == 0:
                password = password+ str(i) + str(j)
    return password
print(n, 'PASSWORD:', password)