```python
import streamlit as st

st.set_page_config(
    page_title="Quiz sobre Puerto Rico",
    page_icon="🇵🇷"
)

st.title("🇵🇷 Quiz sobre Puerto Rico 🇵🇷")

st.markdown("""
# 📖 Conociendo Puerto Rico

Puerto Rico es una isla ubicada en el mar Caribe y un territorio de los
Estados Unidos. Su capital es San Juan, una de las ciudades más antiguas
de América y un importante centro histórico de la región.

La isla posee una rica mezcla cultural formada por influencias taínas,
españolas, africanas y estadounidenses. Esta combinación puede observarse
en la música, la gastronomía, las tradiciones y la arquitectura.

El español es el idioma más hablado, aunque el inglés también es utilizado
ampliamente en la vida cotidiana y en las instituciones oficiales.

Puerto Rico es famoso por sus hermosas playas de arena blanca y aguas
cristalinas. Entre ellas destaca Flamenco Beach, considerada una de las
mejores playas del mundo.

Otro lugar muy importante es el Bosque Nacional El Yunque, una selva
tropical que alberga una gran diversidad de plantas y animales.

La música forma parte esencial de la identidad puertorriqueña. Géneros
como el reguetón han alcanzado fama internacional gracias a artistas de
la isla.

La gastronomía también es muy reconocida. Uno de los platos más típicos
es el mofongo, preparado principalmente con plátano verde.

Uno de los símbolos más queridos de Puerto Rico es el coquí, una pequeña
rana cuyo canto es característico de las noches puertorriqueñas.

La isla también es conocida por sus bahías bioluminiscentes, donde
organismos microscópicos producen un brillo azul verdoso en el agua.

Además, Puerto Rico participa con delegación propia en los Juegos
Olímpicos y en otras competencias internacionales.

¡Ahora pon a prueba tus conocimientos sobre Puerto Rico!
""")

preguntas = (

("¿Cuál es la capital de Puerto Rico?",
 ("Ponce", "San Juan", "Mayagüez"),
 "San Juan"),

("Puerto Rico es un territorio de qué país?",
 ("España", "México", "Estados Unidos"),
 "Estados Unidos"),

("¿Qué moneda se utiliza en Puerto Rico?",
 ("Euro", "Peso", "Dólar estadounidense"),
 "Dólar estadounidense"),

("¿En qué región se encuentra Puerto Rico?",
 ("Europa", "Caribe", "Asia"),
 "Caribe"),

("¿Qué bosque tropical famoso existe en Puerto Rico?",
 ("Amazonía", "Bosque Nacional El Yunque", "Selva Negra"),
 "Bosque Nacional El Yunque"),

("¿Qué ciudad histórica es muy visitada por turistas?",
 ("Bayamón", "Caguas", "Old San Juan"),
 "Old San Juan"),

("¿Qué atrae a muchos turistas a Puerto Rico?",
 ("Nieve", "Playas y cultura", "Volcanes activos"),
 "Playas y cultura"),

("¿Cuál de estas playas es famosa en Puerto Rico?",
 ("Copacabana", "Waikiki", "Flamenco Beach"),
 "Flamenco Beach"),

("¿Qué estilo musical es muy popular en Puerto Rico?",
 ("Reguetón", "Samba", "K-pop"),
 "Reguetón"),

("¿Qué instrumento es tradicional en la música puertorriqueña?",
 ("Violín", "Cuatro", "Gaita"),
 "Cuatro"),

("Una comida típica de Puerto Rico es:",
 ("Sushi", "Tacos", "Mofongo"),
 "Mofongo"),

("Las fiestas puertorriqueñas suelen tener:",
 ("Baile y música", "Silencio total", "Solo deportes"),
 "Baile y música"),

("¿Cuál es el idioma más hablado en Puerto Rico?",
 ("Francés", "Español", "Italiano"),
 "Español"),

("¿Cómo se dice 'hola' en español?",
 ("Bonjour", "Hello", "Hola"),
 "Hola"),

("¿Qué otro idioma también se utiliza mucho en Puerto Rico?",
 ("Inglés", "Japonés", "Alemán"),
 "Inglés"),

("¿Qué significa 'gracias'?",
 ("Buenos días", "Gracias", "Hasta luego"),
 "Gracias"),

("Puerto Rico posee playas que brillan por la noche debido a:",
 ("Lava", "Bioluminiscencia", "Oro en el agua"),
 "Bioluminiscencia"),

("¿Puerto Rico participa en los Juegos Olímpicos con equipo propio?",
 ("Sí", "No", "A veces"),
 "Sí"),

("¿Qué animal es un símbolo famoso de Puerto Rico?",
 ("Coquí", "Canguro", "Panda"),
 "Coquí"),

("Puerto Rico es una:",
 ("Isla", "Montaña", "Península"),
 "Isla"),

("DESAFÍO EXTRA: ¿Qué famoso cantante nació en Puerto Rico?",
 ("Shakira", "Jennifer Lopez", "Ricky Martin"),
 "Ricky Martin")

)

respuestas = ()

for i, pregunta in enumerate(preguntas):
    respuesta = st.radio(
        f"{i + 1}. {pregunta[0]}",
        pregunta[1],
        key=i
    )
    respuestas += (respuesta,)

if st.button("✅ Finalizar Quiz"):

    puntos = 0

    for i in range(len(preguntas)):
        if respuestas[i] == preguntas[i][2]:
            puntos += 1

    st.header(
        f"🎯 Obtuviste {puntos} de {len(preguntas)} puntos"
    )

    if puntos == len(preguntas):
        st.balloons()
        st.success(
            "🏆 ¡Perfecto! Eres un experto en Puerto Rico."
        )

    elif puntos >= 16:
        st.success(
            "🔥 Excelente desempeño."
        )

    elif puntos >= 11:
        st.warning(
            "👍 Buen trabajo."
        )

    else:
        st.error(
            "📚 Te recomendamos repasar el contenido."
        )

    st.subheader("📋 Respuestas Correctas")

    for i in range(len(preguntas)):

        pregunta = preguntas[i][0]
        respuesta_correcta = preguntas[i][2]
        respuesta_usuario = respuestas[i]

        if respuesta_usuario == respuesta_correcta:

            st.success(
                f"{i+1}. {pregunta}\n\n"
                f"Tu respuesta: {respuesta_usuario}\n\n"
                f"✅ Correcta"
            )

        else:

            st.error(
                f"{i+1}. {pregunta}\n\n"
                f"Tu respuesta: {respuesta_usuario}\n\n"
                f"✅ Respuesta correcta: {respuesta_correcta}"
            )
```
