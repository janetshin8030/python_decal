#2.1 
list_1= []
i=0
while i<21:
    list_1.append(i)
    i+=1
print(list_1)

#2.2
def square_function(): 
    square_list = []
    for num in list_1:
        square_num= num ** 2
        square_list.append(square_num)
    return square_list #why do I have to return this function instead of calling it later
square_list= square_function()
print(square_list)

#2.3
def num_first15():
    fifteen = square_list[0:15]
    print(fifteen)
num_first15()

#2.4
def striding_list():
    striding= square_list[4::5]
    print(striding)
striding_list()

#2.5
def slicing_reverse():
    reverse_list= square_list[20::-1]
    slicing_pt2= reverse_list[::3]
    print(slicing_pt2)
slicing_reverse()

#3.1 creating a 5x5 2D List
def create_matrix():
    matrix= []
    count=1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(count)
            count+=1
        matrix.append(row)
    return matrix #had to return the matrix instead of just print it
    print(matrix)
create_matrix()

#3.2 replacing 2D list with '?'
def replace_question(matrix): #I dont understand when to put in what in parenthesis
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] %3 ==0: #forgot colon
                matrix[i][j] = '?' #forgot intend
    return matrix
matrix = create_matrix()
matrix_with_questions= replace_question(matrix)

for row in matrix_with_questions:
    print(row)

#3.3 Summing None 
def summing_matrix(matrix):
    new_matrix= []
    for row in matrix:
        if isinstance(row,list):
            for i in row:
                if i != '?':
                    new_matrix.append(i)
    return sum(new_matrix)
result= summing_matrix(matrix)
print(result)