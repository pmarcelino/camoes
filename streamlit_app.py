from langchain import LLMChain
import openai
import os
import streamlit as st
from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

_ = load_dotenv(find_dotenv())
openai.api_key = os.environ["OPENAI_API_KEY"]

question = """
«Nunca tantos de nós dirigiram o olhar maioritariamente para baixo. Um olhar focado em pequenos ecrãs que operamos com as nossas mãos e que nos tornam por vezes cada  vez mais isolados. Num mundo que é cada vez mais global, mas por vezes tão conectadamente desconectado.» 
David Sobral

Qual É o Nosso Lugar no Universo? Num texto de opinião bem estruturado, com um mínimo de duzentas e um máximo de trezentas e cinquenta palavras, defenda uma perspetiva pessoal sobre a posição assumida por David Sobral quanto ao impacto da tecnologia nas relações humanas. 

No seu texto:

- explicite, de forma clara e pertinente, o seu ponto de vista, fundamentando-o em dois argumentos, cada um deles ilustrado com um exemplo significativo;
- formule uma conclusão adequada à argumentação desenvolvida;
- utilize um discurso valorativo (juízo de valor explícito ou implícito).
"""

criteria = """
Os critérios de correção estão divididos em três parâmetros: A) Género/Formato Textual, B) Tema e Pertinência da Informação, e C) Organização e Coesão Textuais. Cada parâmetro tem uma pontuação máxima de 10 pontos.

#### Parâmetro A - Género/Formato Textual:
- Nível 4 (10 pontos): O aluno escreve um texto de opinião, explicita o seu ponto de vista, fundamenta a perspetiva adotada em pelo menos dois argumentos distintos, ilustra cada argumento com pelo menos um exemplo, formula uma conclusão adequada à argumentação desenvolvida e produz um discurso valorativo.
- Nível 3 (8 pontos): O aluno escreve um texto de opinião e fundamenta a perspetiva adotada em pelo menos dois argumentos distintos, mas ilustra apenas um deles com um exemplo, ou apresenta falhas em um ou dois dos restantes aspetos em avaliação.
- Nível 2 (5 pontos): O aluno escreve um texto de opinião, mas fundamenta a perspetiva adotada em apenas um argumento, ilustrado com um único exemplo, ou apresenta falhas em um ou dois dos restantes aspetos em avaliação.
- Nível 1 (3 pontos): O aluno escreve um texto de opinião, mas apresenta falhas no conjunto dos aspetos em avaliação, ou mistura sem critério nem intencionalidade, as marcas do género/formato solicitado com as de outros géneros/formatos.

#### Parâmetro B - Tema e Pertinência da Informação:
- Nível 4 (10 pontos): O aluno trata o tema proposto sem desvios e escreve um texto com eficácia argumentativa, mobilizando argumentos e exemplos diversificados e pertinentes, e assegurando a progressão da informação de forma coerente.
- Nível 3 (8 pontos): O aluno trata o tema proposto sem desvios, mas escreve um texto  com falhas pontuais na eficácia argumentativa, ou trata o tema proposto com desvios pouco significativos, mas escreve um texto com eficácia argumentativa.
- Nível 2 (5 pontos): O aluno trata o tema proposto com desvios pouco significativos e escreve um texto com falhas pontuais na eficácia argumentativa, ou trata o tema proposto sem desvios, mas escreve um texto com falhas significativas na eficácia argumentativa.
- Nível 1 (3 pontos): O aluno trata o tema proposto com desvios significativos e escreve um texto com reduzida eficácia argumentativa, mobilizando muito pouca informação pertinente.

#### Parâmetro C - Organização e Coesão Textuais:
- Nível 4 (10 pontos): O aluno escreve um texto bem organizado, evidenciando um bom domínio  dos mecanismos de coesão textual.
- Nível 3 (8 pontos): O aluno escreve um texto globalmente bem organizado, em que evidencia domínio dos mecanismos de coesão textual, mas apresenta falhas pontuais em um ou dois dos aspetos em avaliação.
- Nível 2 (5 pontos): O aluno escreve um texto satisfatoriamente organizado, em que evidencia um domínio suficiente dos mecanismos de coesão textual, apresentando falhas pontuais em três ou mais dos aspetos em avaliação, ou falhas significativas em um ou dois desses aspetos.
- Nível 1 (3 pontos): O aluno escreve um texto com uma organização pouco satisfatória, recorrendo a insuficientes mecanismos de coesão ou mobilizando-os de forma inadequada.
"""
st.title("Camões - Avaliador de exames de Português")

st.subheader("Pergunta")
st.write(question)

st.subheader("Critérios de correção")
if st.checkbox('Ver critérios de correção'):
    st.write(criteria)
    
st.subheader('Resposta')
answer = st.text_area("Colocar a resposta do aluno:", height=200)
clicked = st.button("Avaliar")

@st.cache(show_spinner=False)
def evaluate_answer(answer):
    llm=ChatOpenAI(model="gpt-4", max_tokens=2048, temperature=0, top_p=1, frequency_penalty=0, presence_penalty=0)
    
    # Verify if it answers the question
    template = """
    Tu és um professor de Português do ensino secundário português. A tua tarefa é classificar as respostas de alunos, com base nos critérios de correção que te forem dados. És extremamente exigente, muito rigoroso e inflexível na tua avaliação. Dás sempre a pontuação mais baixa possível e escreves em português europeu.
    
    A informação inicial vai-te ser dada da seguinte forma:
    
    [PERGUNTA]: (a pergunta a que o aluno tem de responder)
    [CRITÉRIOS DE CORREÇÃO]: (os critérios de correção a que tu tens de obedecer)
    [RESPOSTA]: (a resposta do aluno)
    """
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    
    human_template = """
    [PERGUNTA]: {question}
    [CRITÉRIOS DE CORREÇÃO]: {criteria}
    [RESPOSTA]: {answer}
    
    ---
    
    Verifica se a resposta do aluno responde à pergunta. Se respondeu, diz "True". Se não respondeu, diz "False".
    """
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    chain = LLMChain(
        llm=llm,
        prompt=chat_prompt
    )
    
    answers_question = eval(chain.run({"question":question, "criteria":criteria, "answer":answer}))
    
    if not answers_question:
        evaluation = "A resposta não responde à pergunta. A classificação é 0 pontos."
        return evaluation
    
    # Verify if it's a coherent answer
    human_template = """
    [PERGUNTA]: {question}
    [CRITÉRIOS DE CORREÇÃO]: {criteria}
    [RESPOSTA]: {answer}
    
    ---
    
    Verifica se a resposta do aluno é coerente (e.g., os argumentos são concordantes com as conclusões). Se sim, diz "True". Se não, diz "False".
    """
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    chain = LLMChain(
        llm=llm,
        prompt=chat_prompt
    )
    
    is_coherent = eval(chain.run({"question":question, "criteria":criteria, "answer":answer}))
    
    if is_coherent:
        human_template = """
        [PERGUNTA]: {question}
        [CRITÉRIOS DE CORREÇÃO]: {criteria}
        [RESPOSTA]: {answer}
        
        ---
        
        Avalia a resposta do aluno. Explica o teu raciocínio de avaliação, passo-a-passo. No final, atribui uma classificação à resposta. Sê extremamente rigoroso, altamente exigente e muito inflexível.
        """
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
        
        chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
        chain = LLMChain(
            llm=llm,
            prompt=chat_prompt
        )
        
        evaluation = chain.run({"question":question, "criteria":criteria, "answer":answer})
    
    else:
        human_template = """
        [PERGUNTA]: {question}
        [CRITÉRIOS DE CORREÇÃO]: {criteria}
        [RESPOSTA]: {answer}
        
        ---
        
        Avalia a resposta do aluno. Explica o teu raciocínio de avaliação, passo-a-passo. No final, atribui uma classificação à resposta. Sê extremamente rigoroso, altamente exigente e muito inflexível. Como a resposta do aluno não é coerente, sê ainda mais penalizador na tua classificação.
        """
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
        
        chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
        chain = LLMChain(
            llm=llm,
            prompt=chat_prompt
        )
        
        evaluation = chain.run({"question":question, "criteria":criteria, "answer":answer})
    
    return evaluation
    
if clicked:
    evaluation_state = st.text("A avaliar a resposta... Pode demorar alguns minutos.")
    evaluation = evaluate_answer(answer)
    evaluation_state.write(f"{evaluation}")
