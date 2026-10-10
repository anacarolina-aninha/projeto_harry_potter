import streamlit as st
import requests

# URL da API com todos os personagens
url = "https://hp-api.onrender.com/api/characters"
st.set_page_config(layout='wide')
# Faz a requisição para pegar os dados
resposta = requests.get(url)
dados = resposta.json()
print (dados [0]['name'])

# Pega apenas os nomes dos personagens , a partir de uma lista vazia
nomes_personagens = []
for personagem in dados:
    nomes_personagens.append(personagem["name"])


# Ordena os nomes em ordem alfabética
nomes_personagens.sort()


# Título do app
st.title("busca bruxo - o lugar onde encintrará todas as informações dos bruxos.🧙‍♂️")


# Sidebar com a lista de nomes
escolha = st.sidebar.selectbox("Escolha um personagem/bruxo", nomes_personagens)



# Procura o personagem escolhido na lista de dados
personagem_selecionado = None
for p in dados:
    if p["name"] == escolha:
        personagem_selecionado = p
        break


# Mostra o nome do personagem
st.subheader(personagem_selecionado["name"])
st.header(f'nome do personagem {personagem['name']}')


# ===== IMAGEM EM DESTAQUE =====
# Verifica se o personagem tem imagem
if personagem_selecionado.get("image"):
    st.image(personagem_selecionado["image"], width=500)
else:
    st.write("📷 este personagem não possui imagem")


# Linha divisória
st.divider()



# Informações principais
st.write(f"**Espécie:** {personagem_selecionado.get('species', 'Não informado')}")
st.write(f"**Casa:** {personagem_selecionado.get('house', 'Não informado')}")
st.write(f"**Gênero:** {personagem_selecionado.get('gender', 'Não informado')}")
st.write(f"**Ancestralidade:** {personagem_selecionado.get('ancestry', 'Não informado')}")
st.write(f"**Ano de nascimento:** {personagem_selecionado.get('yearOfBirth', 'Não informado')}")
st.write(f"**Patrono:** {personagem_selecionado.get('patronus', 'Não informado')}")
st.write(f"**Ator/Atriz:** {personagem_selecionado.get('actor', 'Não informado')}")



# Informações da varinha
varinha = personagem_selecionado.get("wand", {})
st.write("**Varinha:**")
st.write(f"- Madeira: {personagem['wand']['wood']}")
st.write(f"- Núcleo: {personagem['wand']['core']}")
st.write(f"- Tamanho: {personagem['wand']['length']} polegadas")


st.write(f"**Patrono:** {personagem['patronus']}")
st.write(f"**Ator/Atriz:** {personagem['actor']}")


# Mostra se está vivo
st.subheader("Status")
if personagem_selecionado.get("alive"):
    st.success("✅ Está vivo")
else:
    st.error("❌ Faleceu")