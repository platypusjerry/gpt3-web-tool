# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 04:09:22 2021

@author: ADI
"""
import openai
import os
import streamlit as st

from gpt3 import *



openai.api_key = os.getenv("OPENAI_API_KEY")





gpt_1 = GPT(engine="curie-instruct-beta",
                temperature=0.7,           
                max_tokens=100,
                top_p=1,
                frequency_penalty=0.5,
                presence_penalty=0.5,
                append_output_prefix_to_query=True)

gpt_2 = GPT(engine="curie-instruct-beta",
            temperature=0.7,
            max_tokens=125,
            top_p=1,
            frequency_penalty=0.7,
            presence_penalty=0.5,
            output_suffix="\n\n")


gpt_3 = semantic(documents = ['Interested', 'Need Information', 'Unsubscribe',
                       'Wrong Person', 'Complaint', 'Inquiry', 'Request',
                       'Feedback', 'Advertisement']
                 )

gpt_4 = GPT(engine="davinci-instruct-beta",
            temperature=0.8,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0.5)




gpt_1.add_example(Example('Write an email with the following traits-\nTone: Tentative, Formal\nTopics: Data engineers are in high demand, companies looking for right data engineers, finding right job is challenging, not many platforms offer multiple jobs in data engineering roles\nSubject: JOB-A-THON',
                        'Dear All,\n\nData engineers are in high demand. In order to help companies find the right data engineer for their company, we present a Job-A-Thon featuring multiple data engineering positions. \nIf you are seeking a career as a Data Engineer, this is the perfect opportunity to explore where your skills can best be utilized.\nWe hope that you will join us on our platform and sign up for our Job-A-Thon!'))
gpt_1.add_example(Example('Write an email with the following traits-\nTone: Excited, Formal\nTopics: hired for July 2021 project team, 1 month internship, work from home, complete the joining process immediately\nSubject: Selected for internship',
                        'We are pleased to inform you that you have been selected for our upcoming 1-month internship. This includes work from home and the opportunity to complete the joining process immediately. \nIf you are looking to learn more about this opportunity or would like to apply for it please email us back at [email address] with your availability and we will get back in touch with you. We look forward to hearing from you!\nGood Luck!'))



gpt_2.add_example(Example('Paraphrase the source text to make it sound in the indicated mood;\n\nSource text: Elon Musk says he’s going to Mars the next month.\nMood: Angry',
                        'This idiot Musk is willing to ruin his life by going to Mars. WTF'))
gpt_2.add_example(Example('Source text: I have two apples and a banana\nMood: Happy',
                        'I have two super-tasty apples and a banana — feeling awesome!'))
gpt_2.add_example(Example('Source text: I continue to define and discover what home can mean here in amsterdam, whenever i feel a pang of home sickness, it is more in line with missing the cultural mindset of american city life which is much different from the cultural mindset of amsterdam.\nMood: Angry',
                        'I hate Amsterdam because everything here is different from what I am used to.'))
gpt_2.add_example(Example('Source text: I have a routine I was doing but I’m on house arrest so I can’t go to the gym.\nMood: Optimistic',
                        'I have a routine I was doing but I’m on house arrest so I can’t go to the gym. It’s not too bad though, because I can still do my workout at home.'))
gpt_2.add_example(Example('Source text: I am currently waiting for the confirmation of my new job offer.\nMood: Happy',
                        'I am so excited waiting for the confirmation of my new job offer!'))









st.title("GPT-3 Webapp by CadenceIQ")
st.header("A handy GPT-3 web application with the given functional tools")
html_temp = """
<div style="background-color:#A7E8AE ;padding:10px">
<ul>
     <li> <h3> Sentence Paraphrasing according to given sentiment </h3> </li>
     <li> <h3> Email generation from tones and topics </h3> </li>
     <li> <h3> Classifying intents by the Semantic Search endpoint </h3> </li>
 </ul>
<br>
"""
st.markdown(html_temp, unsafe_allow_html=True)


st.sidebar.header("CHOOSE TASK")
box = st.sidebar.selectbox(" ", ["E-mail Generation", "Sentence Paraphrasing", "Semantic Search", "Custom Email"])

if box == 'E-mail Generation':
    st.markdown('#')
    st.markdown('**Write an email with the following traits and topics-**')
    box2 = st.multiselect("Select tones", ["Happy", "Sad","Excited", "Angry", "Tentative", "Formal", "Informal", "Confused", "Analytical", "Interested", "Uninterested" ])
    topics = [st.text_input("Enter topics", " ")]
    for n in range(4):
        topics.append(st.text_input(label='', key=f'Question {n}'))

    prompt = "Write an email with the following traits-\nTone: " + ', '.join(box2) +  "\nTopics: " + ', '.join(topics)
    #st.text(prompt)
    output = gpt_1.submit_request(prompt, 0.7)

    if st.button("submit text"):
        st.text("GENERATED EMAIL:")
        result = output.choices[0].text
        st.info(result)
        
        
        

elif box == 'Semantic Search':
    st.markdown('#')
    st.markdown('**Classify the top intent(s) of given text using a Semantic Similarity scoring-**')
    q = st.text_area("enter text to classify", height=160)
    user_query = gpt_3.get_query(q)
    
    if st.button("submit text"):    
        int_scores = gpt_3.get_score(user_query)
        intents = gpt_3.intent_filtering(int_scores)
        st.text("top intents classified:")
        st.info(intents)
        
     
        
elif box == 'Custom Email':
    st.markdown('#')
    st.title("Custom Email")
    st.markdown('**Enter your details**')
    
    with st.form(key='user_dat'):
        name = st.text_input("Name")
        comp = st.text_input("Company")
        job = st.text_input("Job title")
        submit = st.form_submit_button("Save responses")
        
    st.markdown("#")
    st.markdown('**Generate an E-Mail with the given template instructions**')
    
    col2, col3 = st.beta_columns(2)
    
    with col2:
         with st.form('Form1'):
                a = st.text_input("Enter recipient's designation")
                b = st.text_input("Reason for emailing")
                c = st.text_input("Intent")
                d = st.text_area("Product details, features and benefits", height=160)
                e = st.selectbox("Call to action", ["Request a meeting", "Ask for a quick chat next week","Ask to hop on a quick call", "Ask if interested in getting more information"])
                submitted1 = st.form_submit_button('Save responses')

    with col3:
        with st.form('Form2'):
            box3 = st.multiselect("Select tones", ["Happy", "Excited", "Tentative", "Formal", "Informal", "Analytical", "Confident", "Interested"])
            slider1 = st.select_slider('Select length of Email', options=['brief', 'regular', 'detailed'])
            slider2 = st.select_slider("Creativity level", options=['Low', 'Medium', 'High'])
            submitted2 = st.form_submit_button('Save settings')

        
    if slider2 == 'Low':
        temp = 0.3
    elif slider2 == 'Medium':
        temp = 0.5
    else:
        temp = 0.7
    
    if slider1 == 'regular':
        prompt_input3 = name + " is the " + job + " of " + comp + ". Write a personalized cold email on behalf of " + name + " with the following features;\n" + "Recipient: " + a + "\nReason for emailing: " + b + "\nIntent: " + c + "\nTone: " + ', '.join(box3) + "\nProduct features and benefits: " + d + "\nCall to action: " + e + "\nEmail:"
    else: 
        prompt_input3 = name + " is the " + job + " of " + comp + ". Write a " + slider1 + " personalized cold email on behalf of " + name + " with the following features;\n" + "Recipient: " + a + "\nReason for emailing: " + b + "\nIntent: " + c + "\nTone: " + ', '.join(box3) + "\nProduct features and benefits: " + d + "\nCall to action: " + e + "\nEmail:"
        
    st.markdown("#")
    st.text(prompt_input3)
                
    if st.button("Generate Email"):
        output3 = gpt_4.submit_request(prompt_input3, temp)
        result3 = output3.choices[0].text
        st.info(result3)
        
    

else:
    st.markdown('#')
    st.markdown('**Paraphrase the source text to make it sound in the indicated mood-**')
    mood_input = st.selectbox("select tone for paraphrasing", ["Sad", "Happy","Excited", "Angry", "Analytical", "Confused", "Uninterested"])
    prompt_input2 = st.text_area("Enter text to paraphrase: ",  height=160)
    
    
    if st.button("submit text"):
        prompt = "Source text: " + prompt_input2.title() + "\nMood: " + mood_input
        st.text(prompt)
        output2 = gpt_2.submit_request(prompt, 0.75)
        st.text("PARAPHRASED SENTENCE:")
        result2 = output2.choices[0].text
        st.info(result2)

        


