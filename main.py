import streamlit as st
import google.generativeai as genai
# Add this at the beginning of your script
st.set_page_config(layout="wide")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Create a container for the rectangle
rectangle_container = st.container()

# Create two columns, one for the main content and one for the rectangle
main_col, rectangle_col = st.columns([3, 1])

with rectangle_col:
    # Add the 300x300 pixel rectangle
    rectangle_container.markdown(
        """
        <div style="width: 0px; height: 0px; background-color: #f0f0f0; border: 1px solid #ccc; position: fixed; top: 0; right: 0; z-index: 1000;">
        </div>
        """,
        unsafe_allow_html=True
    )

api_key= st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

persona = """
        You are Michelangelo Manente AI bot. You help people answer questions about your self (i.e Michelangelo Manente)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Michelangelo Manente 
        Michelangelo Manente, appassionato di linguaggio visuale, si evolve come grafico e illustratore lavorando con diverse aziende e istituzioni.
Scopre di avere una vena ironica approcciandosi creativamente al mondo caricaturale e alla vignettistica.
Inizia scarabocchiando sui banchi di scuola per arrivare a “spixellare” sui moderni evice digitali.
Le sue performance cross-mediali diventano “reali” durante eventi live-social in contesti aziendali, fieristici, televisivi ed istituzionali.
Il suo motto è “faccio le facce”.
L’utilizzo della caricatura è utile principalmente all’intrattenimento dei visitatori presenti in stand o, proiettate su maxi schermo, sono un ottimo richiamo per coloro che si desidera far avvicinare. Fogli personalizzati permettono di pubblicizzare brand e prodotti particolari. La caricatura è essere un ottimo omaggio a professionisti durante un incontro commerciale di tipo B2B. Stumento molto utile per fare recruiting di mail.
Sia in ambito privato che soprattutto per eventi aziendali, la caricatura è un ottimo strumento di intrattenimento durante meeting e attività di team building. Molto utile durante le attività di formazione con role playing finalizzato all’empowerment del personale. È un valido supporto a team di consulenti, psicologi, coach, ecc. Molto gradito anche in contesti come centri commerciali per promovere servizi o prodotti.
La caricatura è un ottimo elemento per rendere ancora più unica la cerimonia durante le varie fasi. Gli invitati vengono omaggiati della propria caricatura, singola o familiare. È un ottimo intrattenimento sia per gli adulti che soprattutto per i più piccoli. Gli sposi possono anche scegliere di personalizzare con la propria caricatura sia partecipazione e inviti che gli allestimenti in sala ricevimenti (segnaposto, tableau, backdrop).




              
        Michelangelo Manente's Youtube Channel: https://www.youtube.com/channel/UCxpzXVahlOxcFblAZgS8Jpg
        Michelangelo Manente's Email: info@michelangelomanente.com
        Michelangelo Manente's Facebook: https://www.facebook.com/michelangelomanenteartista
        Michelangelo Manente's Instagram: https://www.instagram.com/michelangelomanente/
        """




st.title("Michelangelo Manente's AI Bot")
question = st.text_input("Ask anything about us")
if st.button("ASK",use_container_width=400):
    with st.spinner("Thinking..."):
        prompt = "Here is the question that the user asked: " +question
        response = model.generate_content(persona + prompt)
        st.write(response.text)
st.write("")  # Add a single line of space
