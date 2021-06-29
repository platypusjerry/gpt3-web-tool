# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 04:09:22 2021

@author: ADI
"""
import openai
import os
import streamlit as st


from gpt3 import *

openai.api_key = "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"




generator = GPT(engine="davinci-instruct-beta",
                temperature=0.7,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0.5,
                presence_penalty=0.5,
                append_output_prefix_to_query=True)



generator.add_example(Example('Write an email with the following traits-\nTone: Tentative, Formal\nTopics: Data engineers are in high demand, companies looking for right data engineers, finding right job is challenging, not many platforms offer multiple jobs in data engineering roles\nSubject: JOB-A-THON',
                        'Dear All,\n\nData engineers are in high demand. In order to help companies find the right data engineer for their company, we present a Job-A-Thon featuring multiple data engineering positions. \nIf you are seeking a career as a Data Engineer, this is the perfect opportunity to explore where your skills can best be utilized.\nWe hope that you will join us on our platform and sign up for our Job-A-Thon!'))
generator.add_example(Example('Write an email with the following traits-\nTone: Excited, Formal\nTopics: hired for July 2021 project team, 1 month internship, work from home, complete the joining process immediately\nSubject: Selected for internship',
                        'We are pleased to inform you that you have been selected for our upcoming 1-month internship. This includes work from home and the opportunity to complete the joining process immediately. \nIf you are looking to learn more about this opportunity or would like to apply for it please email us back at [email address] with your availability and we will get back in touch with you. We look forward to hearing from you!\nGood Luck!'))






st.title("GPT-3 Webapp by CadenceIQ")
st.header("A handy GPT-3 webapp to generate accurate emails relevant to your use-case")

html_temp = """
<div style="background-color:#A7E8AE ;padding:10px">
<h2> Email generation from tones and topics: </h2>
<br>
"""
st.markdown(html_temp, unsafe_allow_html=True)

st.markdown('#')
st.markdown('**ENTER YOUR PROMPTS**')
prompt_input = st.text_area(" ", "Write an email with the following traits- \nTone:  \nTopics:  \nSubject:", height=160)

prompt = prompt_input.title()
output = generator.submit_request(prompt)

if st.button("submit text"):
    st.text("GENERATED EMAIL:")
    result = output.choices[0].text
    st.info(result)


































