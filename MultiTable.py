
string = '*\t| '
for i in range( 0 , 11, 1):
    string = string + str( i ) + '\t'
print( string )
print( '-------------------------------------------------------------------------------------------------' )

for i in range( 0 , 11, 1):
    string = str(i) + '\t| '
    for j in range( 0 , 11, 1):
        string = string + str( i*j ) + '\t'
    print( string )
