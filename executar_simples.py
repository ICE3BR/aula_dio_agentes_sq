import os
import subprocess
import sys

# Função simples para verificar/criar o arquivo prompt.json
def verificar_prompt_json():
    # Verifica se o diretório protocolos existe
    if not os.path.exists("protocolos"):
        print("Criando diretório 'protocolos'...")
        os.makedirs("protocolos")
    
    # Verifica se o arquivo prompt.json existe
    if not os.path.exists("protocolos/prompt.json"):
        print("Criando arquivo 'prompt.json'...")
        conteudo = '''{
    "system_name": "dioBank SQL Agent",
    "model_role": "Você é um agente inteligente de geração de SQL para consultas, inserções, atualizações e deleções de dados bancários, sem nunca excluir o banco de dados.",
    "user_profile": {
        "tipo_usuario": "analista",
        "nivel_experiencia": "avançado",
        "objetivo": "obter e manipular informações bancárias com SQL"
    },
    "restricoes": [
        "Evitar respostas longas",
        "Nunca gerar comandos para deletar ou recriar o banco de dados",
        "Evitar Inserts, Updates e Deletes"
    ],
    "instrucoes_sql": [
        "A base possui tabelas como 'clientes', 'movimentacoes', 'pagamentos' e 'enderecos'",
        "A coluna 'valor' representa o valor das transações",
        "Para calcular o saldo total de um cliente, considere a soma de valores das tabelas 'movimentacoes' e 'pagamentos', atribuindo valores negativos às saídas",
        "Evite erros relacionados a GROUP BY e verifique a compatibilidade com sql_mode=ONLY_FULL_GROUP_BY",
        "Retorne o SQL necessário para executar a tarefa requisitada, podendo incluir múltiplas queries quando necessário, como em inserções seguidas de visualização",
        "Caso queira incluir explicações, use apenas comentários no padrão SQL com '--'",
        "A resposta gerada deve ser uma consulta SQL que retorna o cliente que fez a maior movimentação de dinheiro no menor tempo, considerando a movimentação mais recente com maior valor",
        "Evite qualquer inferência textual fora da query, pois o sistema Streamlit só deve exibir o SQL no painel principal",
        "Nunca gere comandos como DROP DATABASE ou CREATE DATABASE",
        "Se usuario pedir insert, delete ou um update, gere um commentario -- informando que nao é possivel e que você realiza apenas CONSULTAS",
        "Permita comandos UPDATE apenas com cláusulas WHERE bem definidas",
        "Aprenda com contextos, mantenha seu histórico."
    ]
    }'''
        
        with open("protocolos/prompt.json", "w", encoding="utf-8") as f:
            f.write(conteudo)
        
        print("Arquivo 'prompt.json' criado com sucesso.")

# Função principal
def main():
    print("=== Iniciando DioBank SQL Agent ===")
    
    # Verifica e cria o prompt.json se necessário
    verificar_prompt_json()
    
    # Executa o Streamlit
    arquivo_streamlit = "Python/Projetos/aula_dio_agentes_sq/agente/scripts/streamlit_agent.py"
    if os.path.exists(arquivo_streamlit):
        print(f"Executando {arquivo_streamlit}...")
        try:
            # Usa sys.executable para garantir que usamos o Python correto
            comando = ["streamlit", "run", arquivo_streamlit]
            subprocess.run(comando)
        except Exception as e:
            print(f"Erro ao executar Streamlit: {e}")
            print("Tentando método alternativo...")
            try:
                comando_alt = [sys.executable, "-m", "streamlit", "run", arquivo_streamlit]
                subprocess.run(comando_alt)
            except Exception as e:
                print(f"Erro no método alternativo: {e}")
                print("Por favor, execute manualmente: streamlit run agente/scripts/streamlit_agent.py")
    else:
        print(f"Erro: Arquivo {arquivo_streamlit} não encontrado!")
        print("Verifique se você está executando este script da raiz do projeto.")

if __name__ == "__main__":
    main()