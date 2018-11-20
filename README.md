# 2018ht12041-dsa
DataStructues and Algorithms Assigment Code

Below Code will accept two comma seperated string, one for arrival and one for departure
ex: Arrival:   "0900","0915","1030","1045" 
    Departure: "0930","1300","1100","1145"
    
    To Execute Code run below command
    python NumberOfPlatforms.py "0900","0915","1030","1045" "0930","1300","1100","1145"
    runfile('C:/Users/mahes/NumberOfPlatforms.py', args='"0900","0915","1030","1045" "0930","1300","1100","1145"', wdir='C:/Users/mahes')   
    [900, 915, 1030, 1045]
    [930, 1300, 1100, 1145]
    Minimum Number of Platforms Required =  3
    
    
    If Arrival and Departure Counts are not maching it will throw below message
    python NumberOfPlatforms.py "0900","0915","1030","1045" "0930","1100","1145"
    runfile('C:/Users/mahes/NumberOfPlatforms.py', args='"0900","0915","1030","1045" "0930","1100","1145"', wdir='C:/Users/mahes')
    [900, 915, 1030, 1045]
    [930, 1100, 1145]
    Arrival and Departure Count is not Matching
