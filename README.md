# Eskom-Data-Functions
 Functions used to calculate metrics using Eskom data

## Building this package locally

python setup.py sdist

## Installing this package from GitHub
```bash
pip install git+https://github.com/Ndu3000/Eskom-Data-Functions.git
```
## Updating this package from GitHub
```bash
pip install --upgrade git+https://github.com/Ndu3000/Eskom-Data-Functions.git
```
## Usage
```python
from lightpackage import lightbulb as lb

lb.five_num_summary([1,2,3,4,5]) # returns {'max': 5, 'median': 3.0, 'min': 1, 'q1': 2.0, 'q3': 4.0} 
```
## Function 1: dictionary_of_metrics

The summary statistics are calculated using the following formulae:

<center><img src="https://render.githubusercontent.com/render/math?math=\bar{x}=\frac{1}{n}\displaystyle\sum_{i=1}^n x_i"></center>


Where:<br>
<img src="https://render.githubusercontent.com/render/math?math=\bar{x}"> is the mean of the observations<br> 
<img src="https://render.githubusercontent.com/render/math?math=n"> is the total number of observations in the data set, and<br>
<img src="https://render.githubusercontent.com/render/math?math=x_{i}"> is the observation at <img src="https://render.githubusercontent.com/render/math?math=i">

Add ddof=1 to make the standard deviation and variance same as expected output. it easier to use numpy on this function. 

<center><img src="https://render.githubusercontent.com/render/math?math=\s^2=\frac{\displaystyle\sum_{i=1}^n (x_{i}-\bar{x})^2}{n-1}"></center><br>

<img src="https://render.githubusercontent.com/render/math?math=s^2"> is the variance

<center><img src="https://render.githubusercontent.com/render/math?math=s=\sqrt{\frac{\displaystyle\sum_{i=1}^n (x_{i}-\bar{x})^2}{n-1}}"></center>

<img src="https://render.githubusercontent.com/render/math?math=s"> is the standard deviation

<img src="https://render.githubusercontent.com/render/math?math=X_{max}=max\{\x_1,x_2,x_3,x_4,...,x_n\}"><br> 
<img src="https://render.githubusercontent.com/render/math?math=X_{min}=min\{\x_1,x_2,x_3,x_4,...,x_n\}"><br>
Where <img src="https://render.githubusercontent.com/render/math?math=X_{max}"> and <img src="https://render.githubusercontent.com/render/math?math=X_{min}"> are the maximum value and minimum value of a list of length <img src="https://render.githubusercontent.com/render/math?math=n"> respectively.



## Function 2: five_num_summary

Function takes a list (or data range) of electricification by province (EBP) data as numerical values and returns maximum, median, minimum, first quartile and third quartile summary statistics as numerical values that are then rounded to two decimal places. To easily understand this, please view figure 1 below.
 
<b>Figure 1.</b> Five number summary boxplot image
 <img src="https://www.siyavula.com/read/maths/grade-10/statistics/images/5498b5406028c512c20f952d1d2f386b.png"> <br>
 <b>Source:</b> Siyavula.com. (2020)

## Function 3: date_parser
 
Function takes a list of date-time strings and converts it into a list of strings with only the date.

## Function 4: extract_municipality_hashtags

Function takes a dataframe and returns a modified dataframe with two new columns appended, "municipality" and "hashtags". Input must contain a column named "Tweets". Information is extracted from twitter data that includes the municipality and the list of hashtags referred to in each tweet, respectively. 

## Function 5: number_of_tweets_per_day

Function takes a dataframe and returns a dataframe with dates as the index and number of tweets on the given day. Input must contain columns named "Tweets" and "Date".

## Function 6: word_splitter

Function takes a dataframe and returns a modified dataframe with one additional column of tokenized tweets named "Split Tweets". Input must contain a column named "Tweets".

## Function 7: stop_words_remover

Function takes a dataframe and returns a modified dataframe with one additional column of tokenized tweets ("Without Stop Words") with stop words and url links removed from the tweets. Stop words are identified through a pre-loaded dictionary. Input must contain a column named "Tweets".

## Authors

* Selebogo Mosoeu
* Nompilo Nhlabathi
* Caryn Pialat
* Nduduzo Phili

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgements

The authors thank Joanne Moonsamy for all the support, advice and expertise given throughout the development of this package.
