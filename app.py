import streamlit as st

# Título do Sistema Interno
st.title("💼 Sistema Operacional Interno")
st.markdown("Gerenciamento de Caixa, Troco Misto e Agendamentos")

st.divider()

# Formulário para o operador digitar de forma natural
with st.form("form_atendimento"):
    st.subheader("Registrar Atendimento / Caixa")
    
    # Campo de texto livre
    texto_operador = st.text_area(
        "Descreva o atendimento:", 
        placeholder="Ex: Corte do João, R$ 80, pagou com nota de 100 em dinheiro e troco de 20 em Pix. Feito pelo Carlos."
    )
    
    botao_enviar = st.form_submit_button("Processar e Salvar no Caixa")
    
    if botao_enviar:
        if texto_operador.strip():
            st.success("Transação processada com sucesso!")
            st.json({
                "status": "sucesso",
                "mensagem_recebida": texto_operador,
                "nota": "Aqui o seu script de IA estruturará os dados e salvará no Supabase em breve!"
            })
        else:
            st.warning("Por favor, digite os detalhes do atendimento antes de enviar.")

# Área lateral
st.sidebar.header("Painel de Controle")
st.sidebar.info("Status: Configurando ambiente 🟢")
