##Imports

import pandas as pd
import numpy as np

## Data Loading and Preprocessing

### Electricification by province (EBP) data

ebp_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv'
ebp_df = pd.read_csv(ebp_url)

for col, row in ebp_df.iloc[:,1:].iteritems():
    ebp_df[col] = ebp_df[col].str.replace(',','').astype(int)

ebp_df.head()

### Twitter data

twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
twitter_df = pd.read_csv(twitter_url)
twitter_df.head()

## Important Variables

# gauteng ebp data as a list
gauteng = ebp_df['Gauteng'].astype(float).to_list()

# dates for twitter tweets
dates = twitter_df['Date'].to_list()

# dictionary mapping official municipality twitter handles to the municipality name
mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
}

# dictionary of english stopwords
stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose', 
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', 
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', 
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under', 
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves', 
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', 
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', 
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty', 
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', 
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our', 
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', 
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
}

### Function 1
def dictionary_of_metrics(items):
    
    """Returns a dictionary to calculate statistical summary metrics 
    by passing a list of numerical items as an argument.

    Parameters
    ----------
    items: a given list of values
    
    Returns
    -------
    x: Dictionary output, x is a float value rounded to 
    two decimal points
    The result of the numpy methods for calculating mean, median, variance, 
    standard deviation, minimum, and maximum statistical values
    """    
    
    import numpy as np
    x = {'mean': round(np.mean(items),2), #Calculates the list's midpoint float value
         'median': round(np.median(items),2), #Calculates the list's median float value
         'var': round(np.var(items, ddof=1),2), #Calculates the list's variance float value
         'std': round(np.std(items, ddof=1),2), #Calculates the list's standard deviation float value
         'min':round(np.min(items),2), #Calculates the list's minimum float value
         'max':round(np.max(items),2)} #Calculates the list's maximum float value 
         #Display dictionary keys and values using numpy calculation variables as value inputs
    return x #Return dictionary keys and values

### Function 2
def five_num_summary(items):
    
    """Returns a dictionary to calculate five number statistical summary 
   by passing a list of numerical items as an argument.

    Parameters
    ----------
    items: a given list of numerical values.
    
    Returns
    -------
    output: Dictionary output is a float value rounded to 
    two decimal points
    The result of the numpy methods for calculating maximum, 
    median, minimum, first quartile and third quartile 
    statistical values.
    """
    
    import numpy as np
    
    """Import NumPy package to handle arrays"""
    
    maximum = round(np.max(items), 2) #Calculates the list's maximum float value
    median = round(np.median(items), 2) #Calculates the list's midpoint float value
    minimum = round(np.min(items), 2) #Calculates the list's minimum float value
    q1 = round(np.percentile((items), 25), 2) #Calculates the list's first quartile float value
    q3 = round(np.percentile((items), 75), 2) #Calculates the list's third quartile float value
    output = {
        'max': maximum,
        'median': median,
        'min': minimum,
        'q1': q1,
        'q3': q3
    } #Display dictionary keys and values using numpy calculation variables as value inputs

    return output #Return dictionary keys and values

### Function 3
def date_parser(dates):
    
    """Returns a list of dates from a list of date-time strings in the yyyy-mm-dd format."""
    
    mydate = [date_string.split(" ")[0] for date_string in dates]
    return mydate

### Function 4
def extract_municipality_hashtags(df):
    
    """Returns a modified dataframe with two new columns appended, "municipality" and "hashtags". Information is extracted from
    twitter data that includes the municipality and the list of hashtags referred to in each tweet, respectively.
    Input must contain a column named "Tweets".
    
    Parameters
    ----------
    df: dataframe
    
    Returns
    -------
    df_new: modified dataframe 
    """
    
    if type(df) == type(pd.DataFrame()):
        municipality = []
        data = df
        for i in data["Tweets"]:
            data_str = i.replace(":", "") # Remove ":" from the end of municipality keys and hashtags
            data_str = str.split(data_str) # Splits a sentence/multi-word string by white space into a list
            data_muni = [a for a in data_str if a[0] == "@"] # Add words containing the hashtag to new list
            municipality = municipality + [data_muni]
        for j in range(len(municipality)):
            municipality[j] = [i.replace(i, mun_dict[i]) for i in municipality[j] if i in mun_dict]
        for x in range(len(municipality)):
            if municipality[x] == []:
                municipality[x] = (np.nan)

        df_muni = pd.DataFrame({"municipality": municipality})
        df = df.join(df_muni)
    
        data_subset = df
        hashtags = []
        for j, k in data_subset.iterrows(): # Iterate over pd df
            data_subset_str = data_subset.iloc[j,0]
            data_subset_str = str.split(data_subset_str) # Splits a sentence/multi-word string by white space into a list
            data_subset_hashtags = [a for a in data_subset_str if a[0] == "#"] # Add words containing the hashtag to new list
            data_subset_hashtags = list(map(lambda b: str.lower(b), data_subset_hashtags)) # Convert all hashtags in list to lower case
            if data_subset_hashtags == []:
                data_subset_hashtags = (np.nan) # Use () instead of [], resulting nan must not have square brackets in solution
            hashtags = hashtags + [data_subset_hashtags]

        df = data_subset
        df2 = pd.DataFrame({"hashtags": hashtags})
        df = df.join(df2)
        df_new = df
    
    else:
        print("Error: input must be a data frame.")
    return df_new

### Function 5
def number_of_tweets_per_day(df):
    
    """Returns a dataframe of the number of tweets on a given date. Dates form the dataframe index and number of tweets"""
    
    import pandas as pd
    
    df['Day'] = [date.split(" ")[0] for date in df['Date']]
    
    no_of_tweets = df.groupby('Day')['Tweets'].count()  
    mydf = pd.DataFrame(no_of_tweets)
    mydf.index.name = 'Date'
    return mydf

### Function 6
def word_splitter(df):
    
    """Returns a modified dataframe with one additional column of tokenized tweets named "Split Tweets".
    Input must contain a column named "Tweets".
    
    Parameters
    ----------
    df: dataframe
    
    Returns
    -------
    df_new: modified dataframe 
    """
    
    if type(df) == type(pd.DataFrame()):
        words = []
        for j, k in df.iterrows(): # Iterate over pd df
            df_subset_str = df.iloc[j,0]
            df_subset_str = str.split(df_subset_str) # Splits a sentence/multi-word string by white space into a list
            df_subset_words = [a for a in df_subset_str] # Add words to new list
            df_subset_words = list(map(lambda b: str.lower(b), df_subset_words)) # Convert to lower case
            words = words + [df_subset_words]
            
        df_words = pd.DataFrame({"Split Tweets": words})
        df_new = df.join(df_words)
    
    else:
        print("Error: input must be a data frame.")
    return df_new

### Function 7
def stop_words_remover(df):
    
    """docstring needed"""
    
    my_tweets = df['Tweets'].apply(lambda x: x.lower().split())
    df["Without Stop Words"] = my_tweets.apply(lambda x: [word for word in x if word not in stop_words_dict['stopwords']])
    
    return df