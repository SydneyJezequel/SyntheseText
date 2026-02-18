import cohere
import streamlit as st



# Commande pour lancer l'application :
# streamlit run app.py


# Initialisation de cohere :
api_key = st.secrets["COHERE_API_KEY"]
co = cohere.ClientV2(api_key)


# Interface utilisateur :
st.title("Résumé de texte avec Cohere.")

st.write("Cette application utilise une API Cohere pour résumer du texte. Renseigner votre texte à résumer ci-dessous.")

user_input = st.text_area("Renseigner votre texte ici :", height = 300)
if st.button("Résumer ce texte"):
    if user_input.strip():
        with st.spinner("Résumé en cours"):
            try:
                # Préparation du prompt :
                message =f"Generate a concise summary of the following text/n{user_input}"
                # Appel API :
                response = co.chat(
                    model="command-r-plus-08-2024",
                    messages=[{"role":"user","content":message}]
                )
                # Affichage du texte résumé :
                resume = response.message.content[0].text
                st.subheader("Résumé de texte.")
                st.write(resume)
            except Exception as e :
                st.error(f"An error occurred : {e}")
    else:
        st.warning("Merci d'entrer un texte à résumer.")

