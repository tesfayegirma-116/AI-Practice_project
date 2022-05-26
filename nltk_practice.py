# import nltk 
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize

# example_string = """ Muad'Dib learned rapidly because his first training was in how to learn.
# And the first lesson of all was the basic trust that he could learn.
# It's shocking to find how many people do not believe they can learn,
# and how many more believe learning to be difficult."""

# # print(sent_tokenize(example_string))

# print(word_tokenize(example_string))


#filter out stop words
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords

# worf_quote = "Sir, I protest. I am not a merry man!"

# words_in_quote = word_tokenize(worf_quote)

# # print(words_in_quote

# stop_words = set(stopwords.words("english"))

# filtered_list = []

# for word in words_in_quote:
#     if word.casefold() not in stop_words:
#         filtered_list.append(word)



# print(filtered_list)



#stemming ex. helping and helper share the same root word  (help) 

# from nltk.stem import PorterStemmer
# from nltk.tokenize import word_tokenize

# steemer = PorterStemmer()
# string_to_stemming = """The crew of the USS Discovery discovered many discoveries.
# Discovering is what explorers do."""

# words = word_tokenize(string_to_stemming)

# print(words)

# stemmed_words = [ steemer.stem(word) for word in words]
# print(stemmed_words)



#Tagging Parts of Speech (POS) ex, noun, verb, adjective, adverb

# from nltk.tokenize import word_tokenize
# import nltk

# segan_quote = """If you wish to make an apple pie from scratch,
# you must first invent the universe."""

# words_in_segan_quote = word_tokenize(segan_quote)

# pos = nltk.pos_tag(words_in_segan_quote)

# print(pos , nltk.help.upenn_tagset())




#Lemmatization ex, For example, if you were to look up the word “blending” in a dictionary, then you’d need to look at the entry for “blend,” but you would find “blending” listed in that entry.
# from nltk.stem import WordNetLemmatizer
# import nltk


# lemmatizer = WordNetLemmatizer()
# ans = lemmatizer.lemmatize("scarves")
# # print(ans)


# string_for_lemmatizing = "The friends of DeSoto love scarves."

# words = nltk.word_tokenize(string_for_lemmatizing)

# # print(words)

# lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

# # print(lemmatized_words)

# print(lemmatizer.lemmatize("worst", pos="a"))



#Chunking ex. allows you to identify phrases.
# from nltk.tokenize import word_tokenize
# import nltk


# lotr_quote = "It's a dangerous business, Frodo, going out your door."

# words_in_lotr_quote = word_tokenize(lotr_quote)
# # print( words_in_lotr_quote)


# lotr_pos_tags = nltk.pos_tag(words_in_lotr_quote)

# # print(lotr_pos_tags)

# grammar = "NP: {<DT>?<JJ>*<NN>}"

# chunk_parser = nltk.RegexpParser(grammar)
# tree = chunk_parser.parse(lotr_pos_tags)

# print( tree.draw())   


#Using Named entity Recognition ex, location ,org, date, time its recognize from text
# import nltk

# tree = """
#         Men like Schiaparelli watched the red planet—it is odd, by-the-bye, that
#         for countless centuries Mars has been the star of war—but failed to
#         interpret the fluctuating appearances of the markings they mapped so well.
#         All that time the Martians must have been getting ready.

#         During the opposition of 1894 a great light was seen on the illuminated
#         part of the disk, first at the Lick Observatory, then by Perrotin of Nice,
#         and then by other observers. English readers heard of it first in the
#         issue of Nature dated August 2."""

# ans = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(tree)))

# print(ans.draw())

# import nltk
# from nltk.tokenize import word_tokenize

# quote = """
# Men like Schiaparelli watched the red planet—it is odd, by-the-bye, that
# for countless centuries Mars has been the star of war—but failed to
# interpret the fluctuating appearances of the markings they mapped so well.
# All that time the Martians must have been getting ready.

# During the opposition of 1894 a great light was seen on the illuminated
# part of the disk, first at the Lick Observatory, then by Perrotin of Nice,
# and then by other observers. English readers heard of it first in the
# issue of Nature dated August 2."""

# def extract_ne(quote):
#     words = word_tokenize(quote, language="english")
#     tags = nltk.pos_tag(words)
#     tree = nltk.ne_chunk(tags, binary=True)
#     return set(
#         " ".join(i[0] for i in t)
#         for t in tree
#         if hasattr(t, "label") and t.label() == "NE"
#     )

# ans = extract_ne(quote)
# print(ans)















#Getting Text to Analyze ex. 
# from nltk.book import *

# # print(text8.concordance("woman"))

# ans = text8.dispersion_plot(
#     ["woman", "lady", "girl", "gal", "man", "gentleman", "boy", "guy"]
# )

# # print(ans)

# ans2 = text2.dispersion_plot(["Allenham", "Whitwell", "Cleveland", "Combe"])

# print(ans2)





#Making a Frequency Distribution
# from nltk.book import *
# from nltk import FreqDist
# from nltk.corpus import stopwords

# frequency_distribution = FreqDist(text8)

# ans = frequency_distribution.most_common(20)

# graph = frequency_distribution.plot(20, cumulative=True)
# print(ans, graph)



# Finding Collocations  is a sequence of words that shows up often.
from nltk.book import *

ans = text8.collocations()
print(ans)