import pandas 

# REMOVING PUNCTUATIONS
def RemovePunctuations( splitted ) :

    # REMOVING PUNCTUATIONS IN FRONT
    puncts = [ ',' ,'.', ':', ';', '"', "'" ] 

    for x in range( len(splitted) ) :

        while( splitted[ x ][-1] in puncts ) :

            splitted[x] = splitted[ x ][ : -1 ]

        # print( splitted[x] )

    # REMOVING PUNCTUATIONS IN THE BACK
    for x in range( len(splitted) ) :

        while( splitted[ x ][0] in puncts ) :

            splitted[x] = splitted[ x ][ 1 : ]

        # print( splitted[x] )

    return splitted

# FINDING WORDS WITH ATLEAST 6 LETTERS 
def FindAtleastSixLength( data ) :
    
    six_length = []
    
    for x in data :

        if len( x ) >= 6 : six_length.append( x )
    
    return six_length


# ADDED ALL THE PROCESSED WORDS IN A DICTIONARY WITH THE NUMBER OF THEIR OCCURENCES
# AND DECIDED THE MOST FREQUENT
def FindMostFreq( data ) :

    count = {}

    for i in data :

        if i not in count : 
            count[ i ] = 1

        else : 
            count[ i ] += 1    

    maxwords = []
    keys = count.keys()

    maxword = data[0]

    maxwords.append( maxword )
    print( maxwords )
    
    for i in keys :

        if ( ( count[i] == count[ maxwords[0] ] ) and i not in maxwords ) :

            maxwords.append( i )
        
        elif ( count[i] > count[ maxwords[0] ] ) :
            maxwords = [ ]
            maxwords.append( i )
                
    return maxwords


# START HERE \/
about = ""
with open( "about.txt" ,'r' ) as textfile :
    about = textfile.read()

splitted = about.split()
rem_punct = RemovePunctuations( splitted )

# PANDAS.UNIQUE() TO REMOVE DUPLICATES
print( "Words with atleast 6 letters : ", pandas.unique( FindAtleastSixLength( rem_punct ) ) )

print( "Most occuring word(s) is(are) : ", FindMostFreq( rem_punct ) )
