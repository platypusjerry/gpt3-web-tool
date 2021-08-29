# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 04:09:22 2021

@author: ADI
"""
import openai
import os
from operator import itemgetter
import streamlit as st

from gpt3 import *



#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"

gpt_1 = GPT(engine="davinci-instruct-beta",
                temperature=0.7,           
                max_tokens=100,
                top_p=1,
                frequency_penalty=0.5,
                presence_penalty=0.5,
                append_output_prefix_to_query=True)

gpt_2 = GPT(engine="davinci-instruct-beta",
            temperature=0.7,
            max_tokens=125,
            top_p=1,
            frequency_penalty=0.7,
            presence_penalty=0.5,
            output_suffix="\n\n",
            stop=["\n\n"])


gpt_3 = GPT(engine="curie-instruct-beta",
            temperature=0,
            max_tokens=10,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            output_prefix="Class: ",
            output_suffix="\n```\n",
            stop=["```"]
            )


gpt_int = Semantic(engine= "curie",
                   documents = ['High Interest if they are excited or interested or asking for information regarding pricing or other details',
                     'High interest if they are excited, they provide their contact information, they are available for a call/talk/chat',
                     'High Interest if they are looking for something similar',
                     'Low Interest if they are not interested',
                     'Low interest if they want to be contacted later',
                     'Low interest if it is not relevant to them',
                     'Low interest if it is a wrong contact',
                     'Low interest if they already have it managed']
                 )

gpt_high = Semantic(engine = "babbage",
                    documents = ['Pricing',
                    'it is an opportunity because they are giving the contact number',               
                    'Referral if ask to contact another person',
                    'Requesting Information if they want more information, they want pricing information, they want a proposal',
                    'it is an opportunity if they are interested']
                    )

gpt_low = Semantic(engine = "babbage",
                   documents = ['Pricing issue', 
                    'Not Qualified', 
                    'Opportunity if they can still explore our proposal', 
                    'Bad Timing if they are not interested right now, or they are unable to accept right now, or if they want to explore next quarter or next year, timing is not right for them, they want to contact later',
                    'Competitor Mention because they are already working with another company, or they make a comparison with another company, or want information regarding another company',
                    'Wrong Contact if they are not the right person or they are from a different department',
                    'Wrong Contact if they do not work at the company anymore',
                    'Referral if ask to contact another person',
                    'Requesting Information',
                    'Unsubscribe if they want them to be taken off our list',
                    'Request for unsubscription because they do not find it relevant',
                    'Do not need this because already have a better product or they have managed it internally']
                   )



gpt_4 = GPT(engine="davinci-instruct-beta",
            temperature=0.7,
            max_tokens=200,
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



gpt_3.add_example(Example('Classify the following emails into the following classes - Pricing, Opportunity, Bad Timing, Competitor Mention, Wrong Contact, Referral, Unsubscribe, Not Qualified;\n```\nEmail: Hey thanks, you can reach me on 8334080360',
                        'Opportunity'))
gpt_3.add_example(Example('Email: Hi Soham, thanks for reaching out, this is something we are looking at for next quarter. Can you send me some more info?',
                        'Requesting Information'))
gpt_3.add_example(Example('Email: Hi Soham, thanks for reaching out, we can look at this next quarter.',
                        'Bad Timing'))
gpt_3.add_example(Example('Email: Hi Vivek, looping in my head of sales who would be able to handle this better.',
                        'Referral'))
gpt_3.add_example(Example('Email: I am not the right person for this Raj, try reaching out to Rahul',
                        'Wrong Contact'))
gpt_3.add_example(Example('Email: We can look at this next quarter but right now it is not a priority. Good luck with your outreach!',
                        'Bad Timing'))
gpt_3.add_example(Example('Email: We are working with Lavender already but I can explore your proposal',
                        'Competitor Mention'))
gpt_3.add_example(Example('Email: Where did you get my contact? Take me off your list!  ',
                        'Unsubscribe'))
gpt_3.add_example(Example('Email: Can you provide me with your pricing structure? This is something we can look at. ',
                        'Pricing'))
gpt_3.add_example(Example('Email: We are already working with SalesLoft, what are you offering regarding this that could be an alternative?',
                        'Competitor Mention'))
gpt_3.add_example(Example('Email: Do you work with companies that handle this project differently?',
                        'Requesting Information'))
gpt_3.add_example(Example('Email: sure, happy to. You can get in touch on Whatsapp.',
                        'Opportunity'))
gpt_3.add_example(Example('Email: Thanks but we have this managed internally.',
                        'Not Qualified'))
gpt_3.add_example(Example('Email: Thanks for getting in touch but I am in a different department, CCing Ashutosh who can help you out. Good luck with your outreach!',
                        'Referral'))
gpt_3.add_example(Example('Email: Interesting concept Ayush, but I am not in the sales department. I have CCed Parminder in the loop, he is our Head of Sales. Good Luck.',
                        'Referral'))
gpt_3.add_example(Example('Email: Hi Soham, Thanks for reaching out. We are currently handling this by our services so unfortunately we will have to pass on this. Best of luck building the product.',
                        'Not Qualified'))
gpt_3.add_example(Example('Email:  Hi Soham, that would be great. Are you available sometime in the second half of Monday- around 2:30 PM?',
                        'Opportunity'))
gpt_3.add_example(Example('Email: Hi, Thanks for reaching out to us. We discussed it internally but it did not fit our thesis. Wish you all the best in your venture! Thanks, Team Titan Capital',
                        'Not Qualified'))

prime = """Classify the following emails into one of the following topics:
                            1. Pricing
                            2. Opportunity
                            3. Bad Timing
                            4. Competitor Mention
                            5. Wrong Contact
                            6. Referral
                            7. Requesting Information
                            8. Unsubscribe
                            9. Not Qualified
                            Email:
                            Hey thanks, you can reach me on 8334080360
                            The topic of this email is:
                            Opportunity
                            ===
                            Classify the following emails into one of the following topics:
                            1. Pricing
                            2. Opportunity
                            3. Bad Timing
                            4. Competitor Mention
                            5. Wrong Contact
                            6. Referral
                            7. Requesting Information
                            8. Unsubscribe
                            9. Not Qualified
                            Email:
                            Hi Soham, I'm available next Tuesday, you can call me at 8334080360
                            The topic of this email is:
                            Opportunity
                            ===
                            Classify the following emails into one of the following topics:
                            1. Pricing
                            2. Opportunity
                            3. Bad Timing
                            4. Competitor Mention
                            5. Wrong Contact
                            6. Referral
                            7. Requesting Information
                            8. Unsubscribe
                            9. Not Qualified
                            Email:
                            Hi Soham, thanks for reaching out, this is something we are looking at for next quarter. Can you send me some more info?
                            The topic of this email is:
                            Opportunity, Bad Timing, Requesting Information
                            ===
                            Classify the following emails into one of the following topics:
                            1. Pricing
                            2. Opportunity
                            3. Bad Timing
                            4. Competitor Mention
                            5. Wrong Contact
                            6. Referral
                            7. Requesting Information
                            8. Unsubscribe
                            9. Not Qualified
                            Email:
                            Thanks for reaching out Soham, you can book a time with me next week so I can learn more.
                            The topic of this email is:
                            Opportunity
                            ===
                            Classify the following emails into one of the following topics:
                            1. Pricing
                            2. Opportunity
                            3. Bad Timing
                            4. Competitor Mention
                            5. Wrong Contact
                            6. Referral
                            7. Requesting Information
                            8. Unsubscribe
                            9. Not Qualified
                            Email:
                            Do you work with companies that handle this project differently?
                            The topic of this email is:
                            Requesting Information
                            ===
                            Classify the following emails into one of the following topics:
                            1. Pricing
                            2. Opportunity
                            3. Bad Timing
                            4. Competitor Mention
                            5. Wrong Contact
                            6. Referral
                            7. Requesting Information
                            8. Unsubscribe
                            9. Not Qualified
                            Email:
                            Hi Soham, looping in my head of sales who would be able to handle this better.
                            The topic of this email is:
                            Referral
                            ===
                            Classify the following emails into one of the following topics:
                            1. Pricing
                            2. Opportunity
                            3. Bad Timing
                            4. Competitor Mention
                            5. Wrong Contact
                            6. Referral
                            7. Requesting Information
                            8. Unsubscribe
                            9. Not Qualified
                            Email:
                            I'm not the right person for this Soham, try reaching out to Rahul
                            The topic of this email is:
                            Wrong Contract
                            ===
                            Classify the following emails into one of the following topics:
                            1. Pricing
                            2. Opportunity
                            3. Bad Timing
                            4. Competitor Mention
                            5. Wrong Contact
                            6. Referral
                            7. Requesting Information
                            8. Unsubscribe
                            9. Not Qualified
                            Email:
                            We can look at this next quarter but right now it's not a priority. Good luck with your outreach!
                            The topic of this email is:
                            Bad Timing
                            ===
                            Classify the following emails into one of the following topics:
                            1. Pricing
                            2. Opportunity
                            3. Bad Timing
                            4. Competitor Mention
                            5. Wrong Contact
                            6. Referral
                            7. Requesting Information
                            8. Unsubscribe
                            9. Not Qualified
                            Email:
                            We are working with Lavender already but I can explore your proposal
                            The topic of this email is:
                            Competitor Mention
                            ===
                            Classify the following emails into one of the following topics:
                            1. Pricing
                            2. Opportunity
                            3. Bad Timing
                            4. Competitor Mention
                            5. Wrong Contact
                            6. Referral
                            7. Requesting Information
                            8. Unsubscribe
                            9. Not Qualified
                            Email:
                            Where did you get my contact? Take me off your list!
                            The topic of this email is:
                            Unsubscribe
                            ===
                            Classify the following emails into one of the following topics:
                            1. Pricing
                            2. Opportunity
                            3. Bad Timing
                            4. Competitor Mention
                            5. Wrong Contact
                            6. Referral
                            7. Requesting Information
                            8. Unsubscribe
                            9. Not Qualified
                            Email:
                            Can you provide me with your pricing structure? This is something we can look at.
                            The topic of this email is:
                            Pricing
                            ===
                            Classify the following emails into one of the following topics:
                            1. Pricing
                            2. Opportunity
                            3. Bad Timing
                            4. Competitor Mention
                            5. Wrong Contact
                            6. Referral
                            7. Requesting Information
                            8. Unsubscribe
                            9. Not Qualified
                            Email:
                            We are already working with SalesLoft, what are you offering regarding this that could be an alternative?
                            The topic of this email is:
                            Competitor Mention
                            ===
                            Classify the following emails into one of the following topics:
                            1. Pricing
                            2. Opportunity
                            3. Bad Timing
                            4. Competitor Mention
                            5. Wrong Contact
                            6. Referral
                            7. Requesting Information
                            8. Unsubscribe
                            9. Not Qualified
                            Email: """  
prime = prime.replace('\n                            ','\n')
suff = """\nThe topic of the email is:"""

J1 = Jurassic(primer = prime, suffix = suff, numresult=1, temp=0.0, stopseq= ["==="])



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
box = st.sidebar.selectbox(" ", ["E-mail Generation", "Sentence Paraphrasing", "Semantic Search", "Email Reply Classification", "Custom Email"])

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
    
    if st.button("submit text"):    
        interest = gpt_int.get_score(q)
        sorted_interest = sorted(interest, key=itemgetter('score'), reverse=True)
        top_interest = sorted_interest[0]['text']
        
        if top_interest != 'High Interest if they are excited or interested or asking for information regarding pricing or other details' and top_interest != 'High Interest if they are looking for something similar' and top_interest != 'High interest if they are excited, they provide their contact information, they are available for a call/talk/chat':
            intent_score =  gpt_low.get_score(q)
            for a in range(len(intent_score)):
                if intent_score[a]["text"] == 'Opportunity if they can still explore our proposal':
                    intent_score[a]["text"] = 'Opportunity'
                elif intent_score[a]["text"] == 'Bad Timing if they are not interested right now, or they are unable to accept right now, or if they want to explore next quarter or next year, timing is not right for them, they want to contact later':
                    intent_score[a]["text"] = 'Bad timing'
                elif intent_score[a]["text"] == 'Competitor Mention because they are already working with another company, or they make a comparison with another company, or want information regarding another company':
                    intent_score[a]["text"] ='Competitor mention'
                elif intent_score[a]["text"] == 'Wrong Contact if they are not the right person or they are from a different department':
                    intent_score[a]["text"] = 'wrong contact'
                elif intent_score[a]["text"] == 'Wrong Contact if they do not work at the company anymore':
                    intent_score[a]["text"] = 'Wrong Contact'
                elif intent_score[a]["text"] == 'Referral if ask to contact another person':
                    intent_score[a]["text"] = 'Referral'
                elif intent_score[a]["text"] == 'Unsubscribe if they want them to be taken off our list':
                    intent_score[a]["text"] = 'Unsubscribe'
                elif intent_score[a]["text"] == 'Request for unsubscription because they do not find it relevant':
                    intent_score[a]["text"] = 'Unsubscribe'
                elif intent_score[a]["text"] == 'Do not need this because already have a better product or they have managed it internally':
                    intent_score[a]["text"] = 'Not interested'
                else:
                    intent_score[a]["text"] = intent_score[a]["text"]     
                   
            intent_result = gpt_low.intent_filtering(intent_score)

        else:
            intent_score = gpt_high.get_score(q)
            for a in range(len(intent_score)):
                if intent_score[a]["text"] == 'it is an opportunity because they are giving the contact number': 
                    intent_score[a]["text"] = 'Opportunity'
                elif intent_score[a]["text"] == 'it is an opportunity if they are interested':
                    intent_score[a]["text"] = 'Opportunity'
                elif intent_score[a]["text"] == 'Referral if ask to contact another person':
                    intent_score[a]["text"] = 'Referral'
                elif intent_score[a]["text"] == 'Requesting Information if they want more information, they want pricing information, they want a proposal':
                    intent_score[a]["text"] = 'Requesting information'
                else:
                    intent_score[a]["text"] = intent_score[a]["text"]
            
            st.text(intent_score)
            intent_result = gpt_high.intent_filtering(intent_score)

        st.text("top intents classified:")
        st.info(intent_result)
        
          
     
elif box == 'Email Reply Classification':
    st.markdown('#')
    st.title("Email Reply Classification")
    model = st.selectbox("Select language model", ["GPT-3", "Jurassic-1"])
    if model == "GPT-3":
        st.markdown("Enter email text to classify")
        q = st.text_area(" ", height=160)
        q = "Email: " + q
        if st.button("submit text"):
            #test = gpt_3.craft_query(q)
            #st.text(test)
            output = gpt_3.submit_request(q, 0)
            result4 = output.choices[0].text
            st.text("Email Label: ")
            result4 = result4.replace('Class: ', '')
            st.info(result4)
            
    else:
         st.markdown("Enter email text to classify")
         q = st.text_area(" ", height=160)
         if st.button("submit text"):
             #ex = J1.get_prompt(q)
             result5 = J1.submit_req(prompt=q, testing=J1)
             st.text("Email Label: ")
             st.info(result5)
         
         

        
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

        


