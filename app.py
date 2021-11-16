import streamlit as st
import pandas as pd
from io import StringIO
import csv


names = '''Language name
Prototypical negation marking
Negation marking with polarized argument
Example with polarized argument
Gloss for polarized argument
Correct indices for polarized argument
Negation marking with polarized adjunct
Example with polarized
Gloss for polarized adjunct
Correct indices for polarized adjunct'''
columns = names.split('\n')
template = ';'.join(columns)

data = pd.read_csv('database.csv', sep=';', names=columns)
languages = data['Language name']

page = st.sidebar.selectbox('Navigation', options=['Home', 'Search', 'Upload', 'Contacts'])



if page == 'Home':
    st.image('logo.png')
    st.title('Welcome to our Negative Concord Database!')
    st.header('About us')
    st.write('''We are from Linguistics Department of Higher School of Economics, Moscow, Russia
    
**Supervisor** - Alexander Letuchiy, Associate Professor

**Deputy Supervisor** - Roman Tarasov, MA student

**Programming specialists** - Zlata Shkutko and Grigory Kuznetsov, BA students

Roman Tarasov's second thesis was dedicated to typology of negative concord.

To carry out proper research, he had to collect a lot of data about participant negation in different languages.
Almost all the languages were processed with the method of elicitation.

Native speakers or advanced users (of constructed languages) filled in a mini online-questionnaire. It was held using social networks and messengers, some informants were inquired in person.
Questionnaire involved assessing 10 sentences or translating 3 participant negation constructions from English, Russian, or, more rarely, Bulgarian or Ukrainian.

So far, 44 languages were processed. 38 of them are natural, 6 are constructed.
Full list of languages can be found on a Search page (please use navigation menu on the left)''')
    st.header('What is it?')
    st.write('''Negative concord is a participant negation marked both predicatively and on a participant (argument or adjunct).''')

if page == 'Search':
    st.title('Search')
    with st.form('select_lang'):
        selected_lang = st.selectbox('Language', options=languages)
        submitted = st.form_submit_button("Submit")

    if submitted:
        st.table(data[data['Language name'] == selected_lang])

elif page == 'Upload':
    st.title('Upload')
    st.write(f'''
    **File extension:** csv
    
    **Separator:** ;
    
    **Template for columns:**
    
    {template}
    
    It is possible to upload a file with multiple rows. 
    
    **File should not contain column names!**
    ''')
    uploaded_file = st.file_uploader("")
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read()
        data = []
        for i in string_data.split('\r\n'):
            data.append(i.split(';'))
        with open('database.csv', 'a', encoding='utf-8') as file:
            file.write('\n')
            writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(data)
        st.write(f'Uploaded {uploaded_file.name}')

elif page == 'Contacts':
    st.title('Contacts')

    st.write('''Roman Tarasov
    
    e-mail: romantarasov2000@yandex.ru
    ''')
    st.write('''Grigory Kuznetsov
    
    e-mail: truegregkuznetsov@gmail.com
        ''')
    st.write('''Zlata Shkutko
    
    e-mail: zmshkutko@gmail.com
            ''')
