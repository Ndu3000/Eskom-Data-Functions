# Eskom-Data-Functions
 Functions used to calculate metrics using Eskom data

## Function 1
The summary statistics are calculated using the following formulae:

<center><img src="https://render.githubusercontent.com/render/math?math=\bar{x}=\frac{1}{n}\displaystyle\sum_{i=1}^n x_i"></center>


Where:<br>
<img src="https://render.githubusercontent.com/render/math?math=\bar{x}"> is the mean of the observations<br> 
<img src="https://render.githubusercontent.com/render/math?math=n"> is the total number of observations in the data set, and<br>
<img src="https://render.githubusercontent.com/render/math?math=x_{i}"> is the observation at <img src="https://render.githubusercontent.com/render/math?math=i">

Add ddof=1 to make the standard deviation and variance same as expected output. it easier to use numpy on this function. 

<center><img src="https://render.githubusercontent.com/render/math?math=\sigma^2=\frac{\displaystyle\sum_{i=1}^n (x_{i}-\bar{x})^2}{n-1}"></center><br>

<img src="https://render.githubusercontent.com/render/math?math=\sigma^2"> is the variance

<center><img src="https://render.githubusercontent.com/render/math?math=\sigma=\sqrt{\frac{\displaystyle\sum_{i=1}^n (x_{i}-\bar{x})^2}{n-1}}"></center>

<img src="https://render.githubusercontent.com/render/math?math=\sigma"> is standard deviation

## Function 2
 Function takes a list of electricification by province (EBP) data as interger numbers and returns maximum, median, minimum, first quartile and third quartile summary statistics as numerical values that are rounded to two decimal places.
 
## Function 3
 Function takes a list of datetime strings and converts
 it into a list of strings with only the date.

## Function 4

## Function 7
  The function removes the stop words and the ur link from a tweet by:
    removing all stop words based on a pre-loaded dictionary, 
    removing url's from the tweets, 
    tokenising a sentence, 
    and labelling the column for the identified strings of stop words as "Without Stop Words".
