Car-dealer--python-
===================
Aussie Best Car (ABC) has now decided to award an additional bonus based on the bonus contributed 

by the sales of an individual car type. It decides to award an additional bonus of x% of the bonus 

contributed by the sales of Toyota Kluger, y% of the bonus contributed by the sales of Nissan Patrol 

and z% of the bonus contributed by the sales of Ford Territory. The additional bonus rates (i.e. the 

values of x, y and z) will be determined by the board of directors of ABC.

The Managing Director therefore requests you to extend your program for A2 in order to facilitate the 

calculation of the additional bonus as follows.

The main program should ask a user (the Managing Director or another employee) to input the 

additional bonus rates (i.e. the values of x, y and z) one by one, for the calculation of the additional 

bonus. The program then should pass the additional bonus rate for a car type to a function called 

CalculateAdditionalBonus() which will take two inputs: the car type and bonus contributed by the 

sales of the car type. From the car type information the CalculateAdditionalBonus() function will 

collect the appropriate additional bonus rate. The function will return the additional bonus for a car 

type.

The function CalculateTotalBonus() will call sub-functions to calculate the total bonus as calculated 

in A2. Moreover, CalculateTotalBonus() will callCalculateAdditionalBonus() in a loop to calculate 

the additional bonus for each and every car type. The function will return the grand total bonus (i.e. the 

total bonus plus the total additional bonus).

The Managing Director also informs you that they have different profit rates for the three different car 

types. For example, they have i% profit on Toyota Kluger, j% profit on Nissan Patrol, and k% profit on 

Ford Territory. The profit rates (i.e. the values of i, j and k) will be determined by the board of directors 

of ABC.

Once the grand total bonus is calculated your program should ask the user to enter the profit rates 

(i.e. the values of i, j and k) one by one, for the calculation of the total profit. Your program should also 

calculate the net profit where net profit is equal to the total profit minus the grand total bonus.





<b>Aussie Best Car (ABC) has now decided to award an additional bonus based on the bonus contributed 

by the sales of an individual car type. It decides to award an additional bonus of x% of the bonus 

contributed by the sales of Toyota Kluger, y% of the bonus contributed by the sales of Nissan Patrol 

and z% of the bonus contributed by the sales of Ford Territory. The additional bonus rates (i.e. the 

values of x, y and z) will be determined by the board of directors of ABC.

The Managing Director therefore requests you to extend your program for A2 in order to facilitate the 

calculation of the additional bonus as follows.

The main program should ask a user (the Managing Director or another employee) to input the 

additional bonus rates (i.e. the values of x, y and z) one by one, for the calculation of the additional 

bonus. The program then should pass the additional bonus rate for a car type to a function called 

CalculateAdditionalBonus() which will take two inputs: the car type and bonus contributed by the 

sales of the car type. From the car type information the CalculateAdditionalBonus() function will 

collect the appropriate additional bonus rate. The function will return the additional bonus for a car 

type.

The function CalculateTotalBonus() will call sub-functions to calculate the total bonus as calculated 

in A2. Moreover, CalculateTotalBonus() will callCalculateAdditionalBonus() in a loop to calculate 

the additional bonus for each and every car type. The function will return the grand total bonus (i.e. the 

total bonus plus the total additional bonus).

The Managing Director also informs you that they have different profit rates for the three different car 

types. For example, they have i% profit on Toyota Kluger, j% profit on Nissan Patrol, and k% profit on 

Ford Territory. The profit rates (i.e. the values of i, j and k) will be determined by the board of directors 

of ABC.

Once the grand total bonus is calculated your program should ask the user to enter the profit rates 

(i.e. the values of i, j and k) one by one, for the calculation of the total profit. Your program should also 

calculate the net profit where net profit is equal to the total profit minus the grand total bonus.

<b>Test Data</b>

 Press A to add S to search D to Delete Q to quit

A

Enter Year

2000

Enter Sales Price For Toyata $

20000

Enter Sales Price For Nissan $

30000

Enter Sales Price For Ford $

40000

Enter Number Of Sales For Toyata

3

Enter Number of Sales For Nissan

5

Enter Number Of Sales For Ford

8

Enter Y to Calculate for another Year or N to Exit

Y

Enter Year

2001

Enter Sales Price For Toyata $

29103941

Enter Sales Price For Nissan $

18413

Enter Sales Price For Ford $

1414

Enter Number Of Sales For Toyata

4

Enter Number of Sales For Nissan

2

Enter Number Of Sales For Ford

4

Enter Y to Calculate for another Year or N to Exit

A

Enter Year

13981934

Enter Sales Price For Toyata $

18888891

Enter Sales Price For Nissan $

89811

Enter Sales Price For Ford $

1411

Enter Number Of Sales For Toyata

1

Enter Number of Sales For Nissan

2

Enter Number Of Sales For Ford

3

Enter Y to Calculate for another Year or N to Exit

Y

Enter Year

2002

Enter Sales Price For Toyata $

132134

Enter Sales Price For Nissan $

2423

Enter Sales Price For Ford $

234

Enter Number Of Sales For Toyata

4

Enter Number of Sales For Nissan

5

Enter Number Of Sales For Ford

3

Test Data of Search

Enter Year 

2003

2003

('Contribution Of Toyota $', 3000, 'in Total Sales')

('Contribution Of Nissan $', 12000, 'in Total Sales')

('Contribution Of Ford $', 20000, 'in Total Sales')

('Total Sales for ABC', 35000)

('Total Bonus\n', 35.0)

('Contribution Of Toyota $', 3.0, 'in Total Bonus')

('Contribution Of Nissan $', 12.0, 'in Total Bonus')

('Contribution Of Ford $', 20.0, 'in Total Bonus')

('Additional Bonus for toyota Kluger', 1.75)

('Additional Bonus for nissan Patrol', 1.75)

('Additional Bonus for ford Territoary', 1.05)

('Total Adiitional Bonus is', 4.55)

('Total Bonus distributed is', 39.55)

Abnormal data Test Exception

Press A to add S to search D to Delete Q to quit

A

Enter Year

3.0

>>>
