import streamlit as st
import pickle

page = st.sidebar.selectbox(
    'Select a page:',
    ('Home', 'About Predictor', 'Make a prediction!'))

if page == 'Home':
    st.title('Welcome to Sports Subreddit Predictor')

    st.header('Find out which subreddit a comment would most likely be in between r/sportsbook and r/dfsports.')
    st.header("What's awesome is you type the comment!")
    st.text('Click the links in the menu to the left to find out more about the predictor')
    st.text('and to predict some comments.')

if page == 'About Predictor':
    st.title('Welcome to Sports Subreddit Predictor')
    st.header('About')
    st.write('The predictor uses logistic regression model to predict your comment.  This model was \n'
    'chosen during a NLP project, to predict a particular subreddit based on comments. \n'
    'Click the link to check out more about the project.')
    st.write("Link to Project [link](https://git.generalassemb.ly/patrickwcudo/Submissions/tree/master/Projects/project_3-master)")

if page == 'Make a prediction!':
    st.title('Welcome to Sports Subreddit Predictor')
    st.header('Predictor')
    st.write('Type in a comment to see if the comment is from r/sportsbook or r/dfsports.')
    # now try to predict some comments
    # import model reading binary
    model = pickle.load(open('model.p', 'rb'))
    # import tfidf feature extraction
    tvec = pickle.load(open('tfidf.p', 'rb'))
    # get user input
    user_text = st.text_input('Input a comment: ')
    # convert user input to list
    test_list = list(user_text.split(sep=' '))
    # convert list to tfidf sparse matrix
    test_tvec = tvec.transform(test_list)
    # get mean of predictions
    str_mean = model.predict(test_tvec).mean()
    # condictional for mean to classify subreddit
    if str_mean >= .5:
        st.write('The comment you enter is more likely to be found on the sportsbooks subreddit.')
    else:
        st.write('The comment you enter is more likely to be found on the dfsports subreddit.')
