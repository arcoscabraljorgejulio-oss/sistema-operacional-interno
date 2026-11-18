import streamlit as st
from supabase import create_client

# --- CONEXÃO COM O SUPABASE ---
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

@st.cache_resource
def init_supabase():
    return create_client(SUPABASE_URL, SUPABASE_KEY)

supabase = init_supabase()

# --- TELA DO SISTEMA ---
st.title("💼 Sistema Operacional Interno")
st.markdown("Gerenciamento de Caixa, Troco Misto e Agendamentos")

st.divider()

# Formulário para o operador digitar de forma natural
with st.form("form_atendimento"):
    st.subheader("Registrar Atendimento / Caixa")
    
    texto_operador = st.text_area(
        "Descreva o atendimento:", 
        placeholder="Ex: Corte do João, R$ 80, pagou com nota de 100 em dinheiro e troco de 20 em Pix. Feito pelo Carlos."
    )
    
    botao_enviar = st.form_submit_button("Processar e Salvar no Caixa")
    
    if botao_enviar:
        if texto_operador.strip():
            try:
                # Salvando na tabela 'cash_flow' que criamos no Supabase
                dados_para_salvar = {
                    "raw_text": texto_operador
                }
                
                resposta = supabase.table("cash_flow").insert(dados_para_salvar).execute()
                
                st.success("Transação salva com sucesso no Supabase! 🟢")
                st.json(dados_para_salvar)
                
            except Exception as e:
                st.error(f"Erro ao salvar no banco de dados: {e}")
        else:
            st.warning("Por favor, digite os detalhes do atendimento antes de enviar.")

# Área lateral
st.sidebar.header("Painel de Controle")
st.sidebar.info("Status: Conectado ao Supabase 🟢")
