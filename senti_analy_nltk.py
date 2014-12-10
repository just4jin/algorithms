'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
 Simple Twitter sentiment analysis using Python and NLTK

 Goal:
 automatically classify a tweet as positive or negative
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import nltk

# la ist contain positive tweets
pos_tweets = [('I love this car','positive'),
              ('This view is great','positive'),
              ('I feel great this moring','positive'),
              ('I am very excited to be here','positive'),
              ('He is my best friend','positive')]
              
# a list of negative tweets
neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative')]

# take both lists to create a single list of tuples 
# each contain two elements. One - array with words; 
# Two - type of sentiment. 
# (remove words <2 characters and make everything lowercase)

tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e)>=3]
    tweets.append((words_filtered, sentiment))

# list of tweets with sentiment
print tweets
'''
tweets = [
    (['love', 'this', 'car'], 'positive'),
    (['this', 'view', 'amazing'], 'positive'),
    (['feel', 'great', 'this', 'morning'], 'positive'),
    (['excited', 'about', 'the', 'concert'], 'positive'),
    (['best', 'friend'], 'positive'),
    (['not', 'like', 'this', 'car'], 'negative'),
    (['this', 'view', 'horrible'], 'negative'),
    (['feel', 'tired', 'this', 'morning'], 'negative'),
    (['not', 'looking', 'forward', 'the', 'concert'], 'negative'),
    (['enemy'], 'negative')]
'''
# list with test tweets for classification
test_tweets = [
    (['feel', 'happy', 'this', 'morning'], 'positive'),
    (['larry', 'friend'], 'positive'),
    (['not', 'like', 'that', 'man'], 'negative'),
    (['house', 'not', 'great'], 'negative'),
    (['your', 'song', 'annoying'], 'negative')]
    
# classifier

# list of features need to be extracted from tweets
# which is a list with every distinct words ordered by frequency of appearance
# following function is to use to get the list

word_features = get_word_features(get_words_in_tweets(tweets))

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words
    
def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features
    
print word_features
# sort with descending order of frequency
'''
word_features = 
['moring', 'love', 'concert', 'tired', 'feel', 'best', 'looking', 'horrible', 'forward', 'excited', 'friend', 'very', 'here', 'not', 'enemy', 'great', 'like', 'this', 'car', 'morning', 'the', 'view']
'''

# feature extractor to decide which features are relevant
# The one we are going to use returns a dictionary indicating what words # # are contained in the input passed. Here, the input is the tweet. We use # # the word features list defined above along with the input to create the # # dictionary.

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(/%s)' % word] = (word in document_words)
    return features

extract_features(['love', 'this', 'car'] )
'''
{'contains(/car)': True, 'contains(/moring)': False, 'contains(/enemy)': False, 'contains(/looking)': False, 'contains(/morning)': False, 'contains(/view)': False, 'contains(/feel)': False, 'contains(/great)': False, 'contains(/horrible)': False, 'contains(/this)': True, 'contains(/concert)': False, 'contains(/the)': False, 'contains(/forward)': False, 'contains(/like)': False, 'contains(/very)': False, 'contains(/love)': True, 'contains(/here)': False, 'contains(/excited)': False, 'contains(/best)': False, 'contains(/not)': False, 'contains(/tired)': False, 'contains(/friend)': False}
'''

# apply the features to our classifier using the method apply_features
# pass feature extractor along with tweets list defined above

training_set = nltk.classify.apply_features(extract_features, tweets)

# training set contains the labeled features set.
# it is a list of tuples which each tuple containing the feature 
# dictionary and sentiment labels for each tweet. 
print training_set

[({'contains(/car)': True, 'contains(/moring)': False, 'contains(/enemy)': False, 'contains(/looking)': False, 'contains(/morning)': False, 'contains(/view)': False, 'contains(/feel)': False, 'contains(/great)': False, 'contains(/horrible)': False, 'contains(/this)': True, 'contains(/concert)': False, 'contains(/the)': False, 'contains(/forward)': False, 'contains(/like)': False, 'contains(/very)': False, 'contains(/love)': True, 'contains(/here)': False, 'contains(/excited)': False, 'contains(/best)': False, 'contains(/not)': False, 'contains(/tired)': False, 'contains(/friend)': False}, 'positive'), ({'contains(/car)': False, 'contains(/moring)': False, 'contains(/enemy)': False, 'contains(/looking)': False, 'contains(/morning)': False, 'contains(/view)': True, 'contains(/feel)': False, 'contains(/great)': True, 'contains(/horrible)': False, 'contains(/this)': True, 'contains(/concert)': False, 'contains(/the)': False, 'contains(/forward)': False, 'contains(/like)': False, 'contains(/very)': False, 'contains(/love)': False, 'contains(/here)': False, 'contains(/excited)': False, 'contains(/best)': False, 'contains(/not)': False, 'contains(/tired)': False, 'contains(/friend)': False}, 'positive'), ...]

# train classifier with naive bayes classifier
classifier = nltk.NaiveBayesClassifier.train(training_set)

'''
The Naive Bayes classifier uses the prior probability of each label which is the frequency of each label in the training set, and the contribution from each feature. In our case, the frequency of each label is the same for ‘positive’ and ‘negative’. The word ‘amazing’ appears in 1 of 5 of the positive tweets and none of the negative tweets. This means that the likelihood of the ‘positive’ label will be multiplied by 0.2 when this word is seen as part of the input.
'''
# display the most informative features for classifier
# we see that if the input does not contain the word ‘not’ then the positive ratio is 1.6.
print classifier.show_most_informative_features(32)
'''
Most Informative Features
          contains(/not) = False          positi : negati =      1.6 : 1.0
        contains(/great) = False          negati : positi =      1.6 : 1.0
      contains(/looking) = False          positi : negati =      1.2 : 1.0
          contains(/the) = False          positi : negati =      1.2 : 1.0
       contains(/friend) = False          negati : positi =      1.2 : 1.0
       contains(/moring) = False          negati : positi =      1.2 : 1.0
      contains(/forward) = False          positi : negati =      1.2 : 1.0
     contains(/horrible) = False          positi : negati =      1.2 : 1.0
         contains(/like) = False          positi : negati =      1.2 : 1.0
         contains(/love) = False          negati : positi =      1.2 : 1.0
      contains(/concert) = False          positi : negati =      1.2 : 1.0
         contains(/very) = False          negati : positi =      1.2 : 1.0
      contains(/excited) = False          negati : positi =      1.2 : 1.0
        contains(/enemy) = False          positi : negati =      1.2 : 1.0
      contains(/morning) = False          positi : negati =      1.2 : 1.0
        contains(/tired) = False          positi : negati =      1.2 : 1.0
         contains(/best) = False          negati : positi =      1.2 : 1.0
         contains(/here) = False          negati : positi =      1.2 : 1.0
         contains(/this) = True           negati : positi =      1.0 : 1.0
         contains(/feel) = False          negati : positi =      1.0 : 1.0
         contains(/feel) = True           negati : positi =      1.0 : 1.0
None
'''

# Classify the future tweets to predict sentiment
tweet = 'larry is my friend'
print classifier.classifier(extract_features(tweet.split())) # positive

tweet = 'larry is not a bad guy'
print classifier.classify(extract_features(tweet.split())) # negative

tweet = 'larry is an interesting person
print classifier.classify(extract_features(tweet.split())) # negative


'''
There is an accuracy method we can use to check the quality of our classifier by using our test tweets. We get 0.8 in our case which is high because we picked our test tweets for this article. 

The key is to have a very large number of manually classified positive and negative tweets.
'''
