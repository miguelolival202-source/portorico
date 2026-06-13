import streamlit as st

st.set_page_config(page_title="Quiz sobre Porto Rico", page_icon="🇵🇷")

st.title("Quiz sobre Porto Rico")

# Texto informativo inicial (5-8 linhas)
st.markdown("""
**Descubre Puerto Rico**, un bello territorio ubicado en el Caribe.  
Es un territorio estadounidense con una rica historia, playas impresionantes y una cultura vibrante.  
Su capital, **San Juan**, es famosa por el colorido barrio histórico de Old San Juan.  
El país cuenta con la **Floresta Nacional El Yunque**, la única selva tropical del Sistema Forestal Nacional de EE.UU.  
Puerto Rico es conocido por el **reggaetón**, el **mofongo** y el símbolo nacional: el **coquí**.  
Además, sus playas bioluminiscentes y su hospitalario pueblo lo convierten en un destino único en el Caribe.
""")

st.divider()

# Perguntas
questions = [
    {
        "section": "Datos Generales",
        "q": "1. ¿Cuál es la capital de Puerto Rico?",
        "options": ["Ponce", "San Juan", "Mayagüez"],
        "answer": "San Juan"
    },
    {
       "section":"Datos Generales",
        "q": "2. Puerto Rico es un territorio de cuál país?",
        "options": ["España", "México", "Estados Unidos"],
        "answer": "Estados Unidos"
    },
    {
        "section": "Datos Generales",
        "q": "3. ¿Cuál moneda se usa en Puerto Rico?",
        "options": ["Euro", "Peso", "Dólar estadounidense"],
        "answer": "Dólar estadounidense"
    },
    {
        "section": "Datos Generales",
        "q": "4. ¿En cuál región se ubica Puerto Rico?",
        "options": ["Europa", "Caribe", "Asia"],
        "answer": "Caribe"
    },
    {
        "section": "Turismo y Lugares Importantes",
        "q": "5. ¿Cuál selva tropical famosa existe en Puerto Rico?",
        "options": ["Amazonas", "Bosque Nacional El Yunque", "Selva Negra"],
        "answer": "Bosque Nacional El Yunque"
    },
    {
        "section": "Turismo y Lugares Importantes",
        "q": "6. ¿Cuál ciudad histórica es muy visitada por turistas?",
        "options": ["Bayamón", "Caguas", "Old San Juan"],
        "answer": "Old San Juan"
    },
    {
        "section": "Turismo y Lugares Importantes",
        "q": "7. ¿Qué atrae a muchos turistas a Puerto Rico?",
        "options": ["Nieve", "Playas y cultura", "Volcanes activos"],
        "answer": "Playas y cultura"
    },
    {
        "section": "Turismo y Lugares Importantes",
        "q": "8. ¿Cuál de estas playas es famosa en Puerto Rico?",
        "options": ["Copacabana", "Waikiki", "Flamenco Beach"],
        "answer": "Flamenco Beach"
    },
    {
        "section": "Cultura y Tradiciones",
        "q": "9. ¿Cuál estilo musical es muy popular en Puerto Rico?",
        "options": ["Reggaetón", "Samba", "K-pop"],
        "answer": "Reggaetón"
    },
    {
        "section": "Cultura y Tradiciones",
        "q": "10. ¿Cuál instrumento es tradicional en la música puertorriqueña?",
        "options": ["Violín", "Cuatro", "Gaita"],
        "answer": "Cuatro"
    },
    {
        "section": "Cultura y Tradiciones",
        "q": "11. Una comida típica de Puerto Rico es:",
        "options": ["Sushi", "Tacos", "Mofongo"],
        "answer": "Mofongo"
    },
    {
        "section": "Cultura y Tradiciones",
        "q": "12. Las fiestas puertorriqueñas suelen tener:",
        "options": ["Baile y música", "Silencio total", "Solo deportes"],
        "answer": "Baile y música"
    },
    {
        "section": "Lenguaje y Expresiones",
        "q": "13. ¿Cuál idioma es más hablado en Puerto Rico?",
        "options": ["Francés", "Español", "Italiano"],
        "answer": "Español"
    },
    {
        "section": "Lenguaje y Expresiones",
        "q": "14. ¿Cómo se dice 'Olá' en español?",
        "options": ["Bonjour", "Hello", "Hola"],
        "answer": "Hola"
    },
    {
        "section": "Lenguaje y Expresiones",
        "q": "15. ¿Cuál otro idioma también se usa bastante en Puerto Rico?",
        "options": ["Inglés", "Japonés", "Alemán"],
        "answer": "Inglés"
    },
    {
        "section": "Lenguaje y Expresiones",
        "q": "16. ¿Qué significa 'gracias'?",
        "options": ["Bom dia", "De nada", "Obrigado"],
        "answer": "Obrigado"
    },
    {    
        "section": "Curiosidades y Datos Interesantes",
        "q": "17. Puerto Rico tiene playas que brillan de noche debido a:",
        "options": ["Lava", "Bioluminiscencia", "Oro en el agua"],
        "answer": "Bioluminiscencia"
    },
    {
        "section": "Curiosidades y Datos Interesantes",
        "q": "18. ¿Puerto Rico participa en los Juegos Olímpicos con equipo propio?",
        "options": ["Sí", "No"],
        "answer": "Sí"
    },
    {
        "section": "Curiosidades y Datos Interesantes",
        "q": "19. ¿Cuál animal es símbolo famoso de Puerto Rico?",
        "options": ["Coquí", "Canguro", "Panda"],
        "answer": "Coquí"
    },
    {
        "section": "Curiosidades y Datos Interesantes",
        "q": "20. Puerto Rico es:",
        "options": ["Una isla", "Una montaña", "Una península"],
        "answer": "Una isla"
    },
    {
        "section": "Desafío Bonus",
        "q": "21. ¿Qué famosa cantante y actriz nació en Puerto Rico?",
        "options": ["Shakira", "Jennifer Lopez", "Ricky Martin"],
        "answer": "Ricky Martin"
    }
]

# Inicializar estado
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}

if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Mostrar preguntas
for i, q in enumerate(questions):
    st.subheader(q["section"])
    st.write(f"**{q['q']}**")
    
    selected = st.radio(
        label="",
        options=q["options"],
        key=f"q_{i}",
        index=None,
        horizontal=True
    )
    
    st.session_state.user_answers[i] = selected
    st.write("")

st.divider()

# Botão de envio
if st.button("Enviar Respuestas", type="primary"):
    st.session_state.submitted = True

# Resultados e gabarito
if st.session_state.submitted:
    st.header("📊 Resultados")
    
    correct = 0
    total = len(questions)
    
    for i, q in enumerate(questions):
        user_ans = st.session_state.user_answers.get(i)
        correct_ans = q["answer"]
        
        if user_ans == correct_ans:
            correct += 1
            st.success(f"**{q['q']}** ✅ Correcta: {correct_ans}")
        else:
            st.error(f"**{q['q']}** ❌ Tu respuesta: {user_ans} | Correcta: {correct_ans}")
    
    st.subheader(f"Tu puntuación: {correct} / {total} ({int(correct/total*100)}%)")
    
    st.divider()
    
    # Gabarito
    st.header("📝 Gabarito")
    
    for q in questions:
        st.write(f"**{q['q']}** → **{q['answer']}**")
