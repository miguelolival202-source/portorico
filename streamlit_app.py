```python
import streamlit as st

st.set_page_config(
    page_title="Quiz sobre Puerto Rico",
    page_icon="🇵🇷"
)

st.title("🇵🇷 Quiz sobre Puerto Rico 🇵🇷")

st.markdown("""
## 📖 Texto Informativo

Puerto Rico es un territorio de los Estados Unidos ubicado en el mar Caribe.
Su capital es San Juan y su moneda oficial es el dólar estadounidense.

La isla es famosa por sus hermosas playas, su rica cultura, la música
reggaetón, el Bosque Nacional El Yunque y el pequeño sapo Coquí,
considerado uno de los símbolos más importantes de Puerto Rico.

El español es el idioma más hablado, aunque el inglés también es ampliamente utilizado.
Puerto Rico participa en los Juegos Olímpicos con delegación propia y posee algunas de las bahías bioluminiscentes más impresionantes del mundo.

Lee atentamente la información y luego responde las preguntas.
""")

perguntas = [

    ("¿Cuál es la capital de Puerto Rico?",
     ["Ponce", "San Juan", "Mayagüez"],
     "San Juan"),

    ("¿Puerto Rico es un territorio de qué país?",
     ["España", "México", "Estados Unidos"],
     "Estados Unidos"),

    ("¿Qué moneda se utiliza en Puerto Rico?",
     ["Euro", "Peso", "Dólar estadounidense"],
     "Dólar estadounidense"),

    ("¿En qué región se encuentra Puerto Rico?",
     ["Europa", "Caribe", "Asia"],
     "Caribe"),

    ("¿Cuál es el bosque tropical más famoso de Puerto Rico?",
     ["Amazonía", "El Yunque", "Bosque Negro"],
     "El Yunque"),

    ("¿Qué ciudad histórica es muy visitada por los turistas?",
     ["Bayamón", "Caguas", "Old San Juan"],
     "Old San Juan"),

    ("¿Qué atrae a muchos turistas a Puerto Rico?",
     ["Nieve", "Playas y cultura", "Volcanes activos"],
     "Playas y cultura"),

    ("¿Cuál de estas playas es famosa en Puerto Rico?",
     ["Copacabana", "Waikiki", "Flamenco Beach"],
     "Flamenco Beach"),

    ("¿Qué estilo musical es muy popular en Puerto Rico?",
     ["Reggaetón", "Samba", "K-pop"],
     "Reggaetón"),

    ("¿Qué instrumento es tradicional en la música puertorriqueña?",
     ["Violín", "Cuatro", "Gaita"],
     "Cuatro"),

    ("¿Cuál es una comida típica de Puerto Rico?",
     ["Sushi", "Tacos", "Mofongo"],
     "Mofongo"),

    ("Las fiestas puertorriqueñas suelen tener:",
     ["Danza y música", "Silencio total", "Solo deportes"],
     "Danza y música"),

    ("¿Cuál es el idioma más hablado en Puerto Rico?",
     ["Francés", "Español", "Italiano"],
     "Español"),

    ("¿Cómo se dice 'hola' en español?",
     ["Bonjour", "Hello", "Hola"],
     "Hola"),

    ("¿Qué otro idioma también es ampliamente utilizado?",
     ["Inglés", "Japonés", "Alemán"],
     "Inglés"),

    ("¿Qué significa 'gracias'?",
     ["Buenos días", "Gracias", "Hasta luego"],
     "Gracias"),

    ("Las playas que brillan por la noche lo hacen debido a:",
     ["Lava", "Bioluminiscencia", "Oro en el agua"],
     "Bioluminiscencia"),

    ("¿Puerto Rico participa en los Juegos Olímpicos con equipo propio?",
     ["Sí", "No", "A veces"],
     "Sí"),

    ("¿Cuál es el animal símbolo de Puerto Rico?",
     ["Coquí", "Canguro", "Panda"],
     "Coquí"),

    ("Puerto Rico es una:",
     ["Isla", "Montaña", "Península"],
     "Isla"),

    ("PREGUNTA BONUS: ¿Qué famoso cantante nació en Puerto Rico?",
     ["Shakira", "Jennifer Lopez", "Ricky Martin"],
     "Ricky Martin")
]

respostas = []

for i, (pergunta, opcoes, correta) in enumerate(perguntas):
    resposta = st.radio(
        f"{i+1}. {pergunta}",
        opcoes,
        key=i
    )
    respostas.append(resposta)

if st.button("✅ Finalizar Quiz"):

    pontos = 0

    st.markdown("---")
    st.subheader("📋 Resultados")

    for i, (pergunta, opcoes, correta) in enumerate(perguntas):

        if respostas[i] == correta:
            pontos += 1
            st.success(f"✅ {i+1}. Correcta")
        else:
            st.error(
                f"❌ {i+1}. Incorrecta\n\n"
                f"Tu respuesta: {respostas[i]}\n\n"
                f"Respuesta correcta: {correta}"
            )

    st.markdown("---")
    st.header(f"🎯 Puntuación: {pontos}/{len(perguntas)}")

    if pontos == len(perguntas):
        st.balloons()
        st.success("🏆 ¡Perfecto! ¡Eres un experto en Puerto Rico!")
    elif pontos >= 16:
        st.success("🔥 ¡Excelente desempeño!")
    elif pontos >= 11:
        st.warning("👍 ¡Buen trabajo!")
    else:
        st.error("📚 Puedes estudiar un poco más e intentarlo nuevamente.")

    st.markdown("---")
    st.subheader("📖 Gabarito Completo")

    for i, (pergunta, opcoes, correta) in enumerate(perguntas):
        st.write(f"{i+1}. {pergunta}")
        st.write(f"✅ {correta}")
```
