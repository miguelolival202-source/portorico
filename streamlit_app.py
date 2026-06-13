import streamlit as st

st.set_page_config(
    page_title="Quiz sobre Porto Rico",
    page_icon="🇵🇷"
)

st.title("🇵🇷 Quiz sobre Porto Rico 🇵🇷")

st.markdown("""
### 📖 Texto Informativo

Porto Rico é um território dos Estados Unidos localizado no Caribe.
Sua capital é San Juan. O espanhol é o idioma mais falado, mas o inglês
também é amplamente utilizado.

A ilha é famosa por suas praias, pela Floresta Nacional El Yunque,
pela cultura vibrante, pelo reggaeton e pelo famoso sapinho Coquí.
""")

perguntas = (

("Qual é a capital de Porto Rico?",
 ("Ponce", "San Juan", "Mayagüez"),
 "San Juan"),

("Porto Rico é um território de qual país?",
 ("Espanha", "México", "Estados Unidos"),
 "Estados Unidos"),

("Qual moeda é usada em Porto Rico?",
 ("Euro", "Peso", "Dólar americano"),
 "Dólar americano"),

("Em qual região Porto Rico está localizado?",
 ("Europa", "Caribe", "Ásia"),
 "Caribe"),

("Qual floresta tropical famosa existe em Porto Rico?",
 ("Amazônia", "Floresta Nacional El Yunque", "Floresta Negra"),
 "Floresta Nacional El Yunque"),

("Qual cidade histórica é muito visitada por turistas?",
 ("Bayamón", "Caguas", "Old San Juan"),
 "Old San Juan"),

("O que atrai muitos turistas para Porto Rico?",
 ("Neve", "Praias e cultura", "Vulcões ativos"),
 "Praias e cultura"),

("Qual destas praias é famosa em Porto Rico?",
 ("Copacabana", "Waikiki", "Flamenco Beach"),
 "Flamenco Beach"),

("Qual estilo musical é muito popular em Porto Rico?",
 ("Reggaeton", "Samba", "K-pop"),
 "Reggaeton"),

("Qual instrumento é tradicional na música porto-riquenha?",
 ("Violino", "Cuatro", "Gaita"),
 "Cuatro"),

("Uma comida típica de Porto Rico é:",
 ("Sushi", "Tacos", "Mofongo"),
 "Mofongo"),

("As festas porto-riquenhas costumam ter:",
 ("Dança e música", "Silêncio total", "Apenas esportes"),
 "Dança e música"),

("Qual idioma é mais falado em Porto Rico?",
 ("Francês", "Espanhol", "Italiano"),
 "Espanhol"),

("Como se diz 'olá' em espanhol?",
 ("Bonjour", "Hello", "Hola"),
 "Hola"),

("Qual outro idioma também é bastante usado em Porto Rico?",
 ("Inglês", "Japonês", "Alemão"),
 "Inglês"),

("O que significa 'gracias'?",
 ("Bom dia", "Obrigado", "Até logo"),
 "Obrigado"),

("Porto Rico possui praias que brilham à noite devido a:",
 ("Lava", "Bioluminescência", "Ouro na água"),
 "Bioluminescência"),

("Porto Rico participa das Olimpíadas com equipe própria?",
 ("Sim", "Não", "Apenas às vezes"),
 "Sim"),

("Qual animal é símbolo famoso de Porto Rico?",
 ("Coquí", "Canguru", "Panda"),
 "Coquí"),

("Porto Rico é uma:",
 ("Ilha", "Montanha", "Península"),
 "Ilha"),

("DESAFIO BÔNUS: Qual famosa cantora e atriz nasceu em Porto Rico?",
 ("Shakira", "Jennifer Lopez", "Ricky Martin"),
 "Ricky Martin")

)

respostas = ()

for i, pergunta in enumerate(perguntas):
    resposta = st.radio(
        f"{i + 1}. {pergunta[0]}",
        pergunta[1],
        key=i
    )
    respostas += (resposta,)

if st.button("✅ Finalizar Quiz"):

    pontos = 0

    for i in range(len(perguntas)):
        if respostas[i] == perguntas[i][2]:
            pontos += 1

    st.header(f"🎯 Você acertou {pontos} de {len(perguntas)} perguntas!")

    if pontos == len(perguntas):
        st.balloons()
        st.success("🏆 PERFEITO! Você é um especialista em Porto Rico!")
    elif pontos >= 16:
        st.success("🔥 Excelente desempenho!")
    elif pontos >= 11:
        st.warning("👍 Bom trabalho!")
    else:
        st.error("📚 Vale a pena revisar o conteúdo e tentar novamente.")
