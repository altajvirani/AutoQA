AutoQA – an automatic question answering bot has been developed to tackle the
problems of the existing system. It answers to the user’s questions, and provides the most
accurate answer from the data repository which is basically a text file containing a list of
sentences. A domain of apps that are focused towards taking and storing user information also
include notes-taking apps. Notes-taking apps do not usually provide with AI based features like
context-based searching about something that the user might have taken notes of. Considering
the complexities and nuances of the language, a term or phrase might have multiple meanings,
depending on what context it is used in. So, searching becomes meaningless, if the computer
doesn’t understand your intent. Therefore, understanding the input and breaking down until the
subject or root of the sentence is found is very necessary. This is done by using NLP - the
branch of artificial intelligence or AI—concerned with giving computers the ability to
understand text and spoken words in much the same way human beings can. So the developed
system is an intelligent system.
The application is a simple system with a modern design and intuitive UI, that gives the
output in text-to-speech, gives advantage of better user experience. Also, to have best
performance, the application is developed all-in-all in a single programming language –
Python. It will have no need of any markup or scripting languages, and the backend logic, too,
is written in python. Also, database is the file itself that the user provides; it doesn’t require any
other databases. All the operations are performed on the client side itself, which eliminates the
need of transmitting the data over the internet, and thereby, it does eliminate the risks of cybersecurity such as data stealth and hacking. Also, the performance is ensured to be the best that is
possible.

![image](https://user-images.githubusercontent.com/85060648/154837997-92725a10-1d66-4ee0-bddc-a57d1ec064dd.png)

Algorithm:

    1. Take user input
    2. Convert input to lowercase
    3. If input is a greeting:
        a. Print randomized greeting response and read it aloud using text-to-speech (TTS)
    4. Else:
        a. Perform NLP operations on the user input:
            i. Sentence Segmentation: Breaking the data apart into separate sentences.
            ii. Word Tokenization: Parsing the text string into different sections
            (tokens).
            iii. Stop Words Identification and Removal: Removing common words from
            text so unique words that offer the most information about the text
            remain.
            iv. Lemmatization: Reducing words to their root forms for processing.
        b. Compute the TF-IDF (or TF*IDF) metric:
            A vector table containing the product of:
            1. Frequency - Frequency of the words of the user input in the sentence
            of the document, divided by total number of words in the sentence.
            2. Uniqueness - The log of the number of sentences divided by the
            number of sentences that contain the words of the user input.
        c. Check the Cosine Similarity of user query with TF-IDF vector of the document
        d. Display Output (Result):
            i. If Result is found:
                    1. Print the output (result) with the highest similarity and read it
                    aloud using text-to-speech (TTS)
            ii. Else:
                    1. Print "I am sorry! I don't understand you" and read it aloud using
                    text-to-speech (TTS)

Process Design:

The libraries and modules that have been used for the development of the application
are as follow:

  i. Kivy Version 2.0.0:
  
      Kivy is a Python library that facilitates the creation of cross-platform
    applications that can run on Windows, Linux, Android, OSX, iOS, and Raspberry Pi,
    too. It is an open source software library for rapid development of applications equipped
    with novel user interfaces, such as multi-touch apps. It is a popular package for creating
    GUI in Python and in recent years, it is gaining a lot of popularity due to its easy-to-use
    nature, good community support, and easy integration of different components.
    
  ii. KivyMD Version 0.104.2:
  
    KivyMD is built on the top of the Kivy library; it is a collection of Material
    Design widgets to be used with Kivy. It offers more elegant-looking components and
    the code is almost the same. In our system, we use KivyMD components for creating
    the UI (User Interface) of the application and Kivy for all the core functionalities such
    as building the app and the front-end logic.
    
  iii. NLTK Version 3.6.2:
  
    The NLTK module is a massive tool kit, aimed at helping you with the entire
    Natural Language Processing (NLP) methodology. It contains text processing libraries
    to perform a variety of tasks such as tokenization, parsing, classification, stemming,
    tagging and semantic reasoning. It also includes graphical demonstrations and sample
    data sets as well as accompanied by a cook book and a book which explains the
    principles behind the underlying language processing tasks that NLTK supports.
    
  iv. SKLearn or Scikit Learn Version 0.24.2:
    
    Scikit-learn, imported as sklearn, is a popular Python library for machine
    learning approaches such as clustering, classification, and regression. In our application,
    we do not need to use machine learning, nevertheless we will be using scikit-learn’s
    TfidfVectorizer and CosineSimilarity.
    
  v. Pyttsx3 Version 2.90:
  
    Pyttsx3 is a cross-platform library for text-to-speech conversion in Python. This
    lets you synthesize text in to audio you can hear. This package works in Windows, Mac,
    and Linux. Unlike alternative libraries, it works offline and is compatible with both
    Python 2 and 3. It uses native speech drivers when available and works completely
    offline
    
    The implementation of the application has been done in a modular approach, wherein
    
the front end and the backend code have been written in separate files: HomeScreen.py (frontend); bot.py, TextToSpeech.py and kbase.txt (backend) respectively.

    1. Front-end:
    
        a. HomeScreen.py:
        
          This file includes all the front-end program code which has been developed using Kivy
          and KivyMD libraries for the design and event-handling of the UI components of the
          applications, such as buttons, menus, text fields, alert boxes, etc.
          The input is taken via the text-field in the front end. Then, appropriate event-handling
          function makes the respective method calls of method in the backend.
        
    2. Back-end:
    
        a. bot.py:
        
            The bot.py file includes all the programming backend logic that makes possible the
            working of the application. It includes various functions of NLP and SKLearn that help in
            performing the core functionality of the bot.
            Once the input has been collected, then the operations of NLP have to be performed on the
            user input for identifying the user’s intent – i.e. the subject of the sentence. For this, NLTK
            library of Python is used. 

            The procedure of NLP is as follows:

                Step 1: Sentence Segmentation:
                    The first step in the NLP pipeline involves breaking apart the data in the document into
                    separate sentences.

                Step 2: Word Tokenization:
                    Once the document has been split into segments of sentences, these sentences can be
                    processed one at a time. The next step is to tokenize these sentences into singular smaller units
                    called tokens – which are words. The words in sentences are split apart wherever there’s space
                    between them.

                Step 3: Stop Words Identification & Removal:
                    In this step, the common and repetitive terms and those having lesser significance such
                    as prepositions (such as to, from), conjunctions (such as and, or, but), articles (a, an, the),
                    auxiliary verbs (is, are, be), etc. are removed from the text so unique words that offer the most
                    information about the text remain.

                Step 4: Lemmatization:

                    In English (and most languages), words appear in different forms. When working with
                    text in a computer, it is helpful to know the base form of each word so that you know that both
                    sentences are talking about the same concept. This process is called lemmatization — figuring
                    out the most basic form or lemma of each word in the sentence. It reduces the words to their
                    root forms to process. It is used to group different inflected forms of the word, called lemma.
                    For example: The words “intelligence”, “intelligent”, and “intelligently” have a root
                    word “intelligent”, which has a meaning.

                    Now that we have performed these operations on the user’s input sentence, we need to
                    compare the input with the data in the knowledge base (document), and find the result which is
                    the most accurate and relevant to the input. There are two ways we can do this first one being
                    the Bag of Words approach:
                      The Bag of Words (BoW) model is the simplest form of text representation in numbers.
                      Like the term itself, we can represent a sentence as a bag of words vector (a string of numbers).
                      It has a drawback, which is that it emphasizes more on how total frequency of the words of
                      source string in the comparison string collectively, rather than computing the individual
                      frequency of every word inside the sentence and in the document, too. This is so, because even
                      when a sentence which is in reality more similar, with uniform frequency of words will be
                      lesser similar than a sentence having higher cumulative frequency but not so uniform
                      frequency.
                    However, these limitations are overcome by another approach known as TF-IDF,
                    which is explained below as follows:

                TF-IDF:
                    We will compute the Term Frequency-Inverse Document Frequency (TF-IDF) vectors
                    for each document. This will give you a matrix where each column represents a word in the
                    overview vocabulary (all the words that appear in at least one document).
                    TF-IDF is the statistical method of evaluating the significance of a word in a given
                    document. It is the product of the TF and IDF scores of the term, where:
                      1. TF — Term Frequency (TF) refers to how many times a given term appears in a
                      document.
                      ![image](https://user-images.githubusercontent.com/85060648/154838500-14e7ba7e-ff8b-4089-a75a-2323b70ba712.png)

                      2. IDF — Inverse Document Frequency (IDF) measures the weight of the word in the
                      document, i.e. if the word is common or rare in the entire document.
                      ![image](https://user-images.githubusercontent.com/85060648/154838520-bdfb519e-8d3e-4ba3-9803-6fc2e8f2e836.png)

                    TF-IDF gives larger values for less frequent words in the document corpus. TF-IDF
                    value is high when both IDF and TF values are high i.e. the word is rare in the whole document
                    but frequent in a document.
                    The TF-IDF intuition follows that the terms that appear frequently in a document are less
                    important than terms that rarely appear. Higher the TF-IDF score, the rarer the term is and viceversa. 
                    The whole idea is to weigh down the frequent terms whilescaling up the rare ones.
                    Fortunately, Scikit Learn gives you a built-in TfIdfVectorizer class that produces the
                    TF-IDF matrix quite easily.
                 Cosine similarity:
                      Now we have this matrix, we can easily
                      compute a similarity score. There are several options to     
                      do this; such as the Euclidean, the Pearson, and the
                      cosine similarity scores. Cosine similarity is a metric
                      used to measure how similar the documents are
                      irrespective of their size. Mathematically, it measures
                      ![image](https://user-images.githubusercontent.com/85060648/154838633-624b9e54-63ff-45f8-9e5e-7707e4867f3e.png)
                      the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine
                      similarity is advantageous because even if the two similar documents are far apart by the
                      Euclidean distance (due to the size of the document), chances are they may still be oriented
                      closer together. The smaller the angle, higher the cosine similarity. This functionality is also
                      provided in the Scikit Learn library.
                      We will be using the cosine similarity to calculate a numeric quantity that denotes the
                      similarity between the two words. You use the cosine similarity score since it is independent of
                      magnitude and is relatively easy and fast to calculate (especially when used in conjunction with 
                      ![image](https://user-images.githubusercontent.com/85060648/154838647-02dbc410-6b67-40e2-9e35-1184b13c6e9c.png)
                      The vector of TF-IDF of the data in the corpus or the knowledge-base is known
                      checked for the cosine similarity with user’s input sentence. The one with highest cosine
                      similarity will be shown as the result to the user. The output will be printed inside the chat.
          b. TextToSpeech.py:
          
              The Python Pyttsx3 text-to-speech (TTS) library will then read the displayed result
              aloud to the user. When no relevant result is found, the bot will display and read, “I am sorry! I
              don't understand you”.
              
          c. kbase.txt:
            
            This file represents the corpus or the knowledge base of the application from where the
            data will be referred for searching, which is a document. It is a text file, which will contain data
            in the form of sentences
The following are the test cases that have been developed to perform experiment on the
application:
![image](https://user-images.githubusercontent.com/85060648/154838763-98344e25-9fea-4ee7-bb33-8493f95cb3c1.png)
![image](https://user-images.githubusercontent.com/85060648/154838775-ba94e4cb-9d8d-44dd-8a0f-2a317c159d34.png)
![image](https://user-images.githubusercontent.com/85060648/154838787-593caa35-1ee2-43a3-9259-41e77c633770.png)
![image](https://user-images.githubusercontent.com/85060648/154838797-9dd6235f-70c4-4524-a16b-ff4bb982f733.png)

Below given are the output snapshots of the application that are the results of the
experiments for the purpose of validation and verification:
![image](https://user-images.githubusercontent.com/85060648/154838833-bbe1726a-35b6-44d5-8d9e-618c2a6fd779.png)

![image](https://user-images.githubusercontent.com/85060648/154838851-44a2d2e4-a37d-4480-b914-4a92f1743031.png)

![image](https://user-images.githubusercontent.com/85060648/154838857-9f652f1d-7476-4421-b2b9-915ad40cccc5.png)

![image](https://user-images.githubusercontent.com/85060648/154838862-e81b2339-389e-456a-9131-55ec6c4814ca.png)






