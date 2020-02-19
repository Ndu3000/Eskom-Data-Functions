from lightpackage import lightbulb

assert lightbulb.dictionary_of_metrics(gauteng) == {'mean': 26244.42,
                                   'median': 24403.5,
                                   'variance': 108160153.17,
                                   'standard deviation': 10400.01,
                                   'min': 8842.0,
                                   'max': 39660.0}, 'incorrect'

assert lightbulb.five_num_summary(gauteng) == {'max': 39660.0,
                                    'median': 24403.5,
                                    'min': 8842.0,
                                    'q1': 18576.0,
                                    'q3': 36720.0}, 'incorrect'

assert lightbulb.date_parser(dates[:3]) == ['2019-11-29', '2019-11-29', '2019-11-29'], 'incorrect'
assert lightbulb.date_parser(dates[-3:]) == ['2019-11-20', '2019-11-20', '2019-11-20'], 'incorrect'

assert lightbulb.extract_municipality_hashtags(twitter_df.copy()).loc[4, "hashtags"] == ['#eskomfreestate', '#mediastatement'], 'incorrect'
assert lightbulb.extract_municipality_hashtags(twitter_df.copy()).loc[5, "municipality"] == ['Johannesburg'], 'incorrect'

assert lightbulb.number_of_tweets_per_day(twitter_df.copy()).iloc[0][0] == 18, 'incorrect'
assert lightbulb.number_of_tweets_per_day(twitter_df.copy()).iloc[1][0] == 11, 'incorrect'

assert lightbulb.word_splitter(twitter_df.copy()).loc[0, "Split Tweets"] == ['@bongadlulane',
                             'please',
                             'send',
                             'an',
                             'email',
                             'to',
                             'mediadesk@eskom.co.za'], 'incorrect'
assert lightbulb.word_splitter(twitter_df.copy()).loc[1, "Split Tweets"] == ['@saucy_mamiie', 'pls', 'log', 'a',
                                                                             'call', 'on', '0860037566'], 'incorrect'

assert lightbulb.stop_words_remover(twitter_df.copy()).loc[0, "Without Stop Words"] == ['@bongadlulane', 'send', 'email', 
                                                                                        'mediadesk@eskom.co.za'], 'incorrect'
assert lightbulb.stop_words_remover(twitter_df.copy()).loc[1, "Without Stop Words"] == ['@saucy_mamiie', 'pls', 
                                                                                        'log', '0860037566'], 'incorrect'
