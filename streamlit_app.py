import streamlit as st

st.set_page_config(page_title="Quiz sobre Puerto Rico")

st.title("Quiz sobre Puerto Rico")

st.markdown("""

## Texto Informativo

Puerto Rico es una isla ubicada en el Caribe y es un territorio de Estados Unidos.
Su capital es San Juan y la moneda utilizada es el dólar estadounidense.
La cultura puertorriqueña es conocida por su música, danza, gastronomía y hermosas playas.
Entre sus lugares turísticos más famosos se encuentran Old San Juan, Flamenco Beach y el Bosque Nacional El Yunque.
Los idiomas más utilizados son el español y el inglés.
Puerto Rico también es conocido por sus bahías bioluminiscentes, que brillan durante la noche.
""")

perguntas = [
{"pergunta": "¿Cuál es la capital de Puerto Rico?", "opcoes": ["Ponce", "San Juan", "Mayagüez"], "resposta": "San Juan"},
{"pergunta": "¿Puerto Rico es un territorio de qué país?", "opcoes": ["España", "México", "Estados Unidos"], "resposta": "Estados Unidos"},
{"pergunta": "¿Qué moneda se utiliza en Puerto Rico?", "opcoes": ["Euro", "Peso", "Dólar estadounidense"], "resposta": "Dólar estadounidense"},
{"pergunta": "¿En qué región se encuentra Puerto Rico?", "opcoes": ["Europa", "Caribe", "Asia"], "resposta": "Caribe"},
{"pergunta": "¿Qué bosque tropical famoso existe en Puerto Rico?", "opcoes": ["Amazonía", "Bosque Nacional El Yunque", "Bosque Negro"], "resposta": "Bosque Nacional El Yunque"},
{"pergunta": "¿Qué ciudad histórica es muy visitada por los turistas?", "opcoes": ["Bayamón", "Caguas", "Old San Juan"], "resposta": "Old San Juan"},
{"pergunta": "¿Qué atrae a muchos turistas a Puerto Rico?", "opcoes": ["Nieve", "Playas y cultura", "Volcanes activos"], "resposta": "Playas y cultura"},
{"pergunta": "¿Cuál de estas playas es famosa en Puerto Rico?", "opcoes": ["Copacabana", "Waikiki", "Flamenco Beach"], "resposta": "Flamenco Beach"},
{"pergunta": "¿Qué estilo musical es muy popular en Puerto Rico?", "opcoes": ["Reggaetón", "Samba", "K-pop"], "resposta": "Reggaetón"},
{"pergunta": "¿Qué instrumento es tradicional en la música puertorriqueña?", "opcoes": ["Violín", "Cuatro", "Gaita"], "resposta": "Cuatro"},
{"pergunta": "¿Cuál es una comida típica de Puerto Rico?", "opcoes": ["Sushi", "Tacos", "Mofongo"], "resposta": "Mofongo"},
{"pergunta": "Las fiestas puertorriqueñas suelen tener:", "opcoes": ["Baile y música", "Silencio total", "Solo deportes"], "resposta": "Baile y música"},
{"pergunta": "¿Cuál es el idioma más hablado en Puerto Rico?", "opcoes": ["Francés", "Español", "Italiano"], "resposta": "Español"},
{"pergunta": "¿Cómo se dice 'olá' en español?", "opcoes": ["Bonjour", "Hello", "Hola"], "resposta": "Hola"},
{"pergunta": "¿Qué otro idioma también es muy utilizado en Puerto Rico?", "opcoes": ["Inglés", "Japonés", "Alemán"], "resposta": "Inglés"},
{"pergunta": "¿Qué significa 'obrigado'?", "opcoes": ["Buenos días", "Gracias", "Hasta luego"], "resposta": "Gracias"},
{"pergunta": "Puerto Rico posee playas que brillan por la noche debido a:", "opcoes": ["Lava", "Bioluminiscencia", "Oro en el agua"], "resposta": "Bioluminiscencia"},
{"pergunta": "¿Puerto Rico participa en los Juegos Olímpicos con equipo propio?", "opcoes": ["Sí", "No", "Solo a veces"], "resposta": "Sí"},
{"pergunta": "¿Qué animal es un símbolo famoso de Puerto Rico?", "opcoes": ["Coquí", "Canguro", "Panda"], "resposta": "Coquí"},
{"pergunta": "Puerto Rico es una:", "opcoes": ["Isla", "Montaña", "Península"], "resposta": "Isla"},
{"pergunta": "¿Qué famoso cantante y actor nació en Puerto Rico?", "opcoes": ["Shakira", "Jennifer Lopez", "Ricky Martin"], "resposta": "Ricky Martin"}
]

respostas_usuario = []

for i, pergunta in enumerate(perguntas):
    resposta = st.radio(
    f"{i+1}. {pergunta['pergunta']}",
    pergunta["opcoes"],
    key=i
    )
    respostas_usuario.append(resposta)

if st.button("Finalizar Quiz"):
    acertos = 0

    
    for i in range(len(perguntas)):
        if respostas_usuario[i] == perguntas[i]["resposta"]:
            acertos += 1

        porcentagem = (acertos / len(perguntas)) * 100

        st.subheader("Resultado")
        st.write(f"Acertaste {acertos} de {len(perguntas)} preguntas.")
        st.write(f"Porcentaje de aciertos: {porcentagem:.1f}%")

        st.subheader("Gabarito")

    for i, pergunta in enumerate(perguntas):
        resposta_usuario = respostas_usuario[i]
        resposta_correta = pergunta["resposta"]

        if resposta_usuario == resposta_correta:
                st.success(
                    f"{i+1}. {pergunta['pergunta']}\n\nTu respuesta: {resposta_usuario}\n\nRespuesta correcta: {resposta_correta}"
        )
        else:
            st.error(
             f"{i+1}. {pergunta['pergunta']}\n\nTu respuesta: {resposta_usuario}\n\nRespuesta correcta: {resposta_correta}"
        )
    

