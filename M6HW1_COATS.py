# Brandon Coats
# CTI 110
# M6HW1
# 11/10/17

def calc_average( score1, score2, score3, score4, score5 ):
           average = ( score1 + score2 + score3 + score4 + score5 ) / 5
           return average

def determineGrade( userScore ):
           if ( userScore < 60 ):
               return "F"
           elif( userScore < 70 ):
               return "D"
           elif( userScore < 80 ):
               return "C"
           elif( userScore < 90):
               return "B"
           elif( userScore < 101):
               return "A"

def askScores():
           score1 = float( input( "Please enter score 1: " ) )
           score2 = float( input( "Please enter score 2: " ) )
           score3 = float( input( "Please enter score 3: " ) )
           score4 = float( input( "Please enter score 4: " ) )
           score5 = float( input( "Please enter score 5: " ) )

           return score1, score2, score3, score4, score5

def printResults( score1, score2, score3, score4, score5 ):
           print( "Score\tLetter Grade" )
           print( str( score1 ) + "\t" + determineGrade( score1 ), \
                  str( score2 ) + "\t" + determineGrade( score2 ), \
                  str( score3 ) + "\t" + determineGrade( score3 ), \
                  str( score4 ) + "\t" + determineGrade( score4 ), \
                  str( score5 ) + "\t" + determineGrade( score5 ), sep = "\n" )

def main():
         score1, score2, score3, score4, score5 = askScores()
         printResults( score1, score2, score3, score4, score5 )
         print('Your average is',calc_average( score1, score2, score3, score4,score5 ) )

main()
