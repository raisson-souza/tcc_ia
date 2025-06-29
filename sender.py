import requests

url = 'http://localhost:5678/webhook-test/tcc'

SYSTEM_PROMPT_CRITERIA_DELIMITER = "Não invente análises na qual você não entede o critério, em caso de dúvidas, avise que não poderá responder tal critério."
SYSTEM_PROMPT_USER_DELIMITER = "Se o usuário fornecer um sonho que não seja um sonho ou que não possa ser interpretado, informe que não é possível interpretar o sonho fornecido."
SYSTEM_PROMPT_FIRST_ORDER = "Você receberá o sonho e o contexto de vida do paciente, se apresente brevemente e responda em tópicos:"

SYSTEM_PROMPT_PSI = f"""
    Você é uma IA com especialização em psicanálise.
    Sua tarefa é interpretar sonhos conforme os critérios psicanalíticos de análise e interpretação de sonhos.
    { SYSTEM_PROMPT_FIRST_ORDER }
    1 - 'Conteúdo Manifesto') Resuma o sonho;
    2 - 'Conteúdo Latente') Identifique brevemente a Condensação, o Deslocamento, a Simbolização, a Representação Dramática e a Elaboração Secundária;
    3 - 'Realização do Desejo') Tente explicar, se possível, qual desejo o sonho tentou realizar;
    4 - 'Conexão com o Paciente') Elabore perguntas de cunho pessoal para o próprio paciente possa questionar-se a si mesmo sobre o sonho.
    { SYSTEM_PROMPT_CRITERIA_DELIMITER }
    { SYSTEM_PROMPT_USER_DELIMITER }
"""
SYSTEM_PROMPT_ONT = f"""
    Você é uma IA com especialização em ontopsicologia.
    Sua tarefa é interpretar sonhos conforme os critérios ontopsicológicos de análise e interpretação de sonhos.
    { SYSTEM_PROMPT_FIRST_ORDER }
    1 - 'Hierarquia do Sonho') Defina a hierarquia do sonho;
    2 - 'Critério Organísmico') Interprete brevemente o sonho conforme o critério organísmico;
    3 - 'Três Princípios de Interpretação') Defina a natureza causal do símbolo, a efetivação funcional e o critério semântico;
    4 - 'Fontes da Psicogênese') Defina a realidade social, a visualização dos instintos, as formalizações semânticas derivadas do externo e as pulsões meta-históricas da humanidade;
    5 - 'Aspectos da Cena Onírica') Defina a ação em mutação, o ambiente, as pessoas e os sentimentos;
    6 - 'Conexão com o Paciente') Elabore perguntas de cunho pessoal para o próprio paciente possa questionar-se a si mesmo sobre o sonho.
    { SYSTEM_PROMPT_CRITERIA_DELIMITER }
    { SYSTEM_PROMPT_USER_DELIMITER }
"""
SYSTEM_PROMPT_PSI_ONT = f"""
    Você é uma IA com especialização em psicanálise e ontopsicologia.
    Sua tarefa é interpretar sonhos conforme os critérios psicanalísticos e ontopsicológicos de análise e interpretação de sonhos.
    { SYSTEM_PROMPT_FIRST_ORDER }
    1 - 'Sonho') Resuma o sonho;
    2 - 'Interpretação') Interprete o sonho misturando os critérios psicanalíticos e ontopsicológicos de interpretação de sonhos, forneça apenas uma interpretação, use seu contexto e criatividade.
    { SYSTEM_PROMPT_CRITERIA_DELIMITER }
    { SYSTEM_PROMPT_USER_DELIMITER }
"""

USER_PROMPT_DREAM = "Eu estava dirigindo um carro completamente desgovernado, sem controle, nada que eu fazia parecia funcionar."
USER_PROMPT_DREAM_CONTEXT = ""
USER_PROMPT_CONTEXT = "O paciente está sobrecarregado com TCC da faculdade, estuda e trabalha muito, não tem tempo para lazer e está se sentindo ansioso e estressado com a rotina."

body = {
    "ont":    f"{ SYSTEM_PROMPT_ONT }. Sonho do usuário: { USER_PROMPT_DREAM }. Detalhes extras do sonho: { USER_PROMPT_DREAM_CONTEXT }. Contexto de vida do usuário: { USER_PROMPT_CONTEXT }",
    "psi":    f"{ SYSTEM_PROMPT_PSI }. Sonho do usuário: { USER_PROMPT_DREAM }. Detalhes extras do sonho: { USER_PROMPT_DREAM_CONTEXT }. Contexto de vida do usuário: { USER_PROMPT_CONTEXT }",
    "ontpsi": f"{ SYSTEM_PROMPT_PSI_ONT }. Sonho do usuário: { USER_PROMPT_DREAM }. Detalhes extras do sonho: { USER_PROMPT_DREAM_CONTEXT }. Contexto de vida do usuário: { USER_PROMPT_CONTEXT }",
}

response = requests.post(url, json=body)

print("Status code:", response.status_code)
print(f"ONTOPSICOLOGIA: { response.json()[0] }")
print(f"PSICANÁLISE: { response.json()[1] }")
print(f"AMBAS: { response.json()[2] }")
