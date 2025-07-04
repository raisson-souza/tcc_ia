# Para workflow com interpretação ONTOPSICOLÓGICA por critério (pausada)

import requests

url = 'http://localhost:5678/webhook-test/criteria-ontopsicologia'

USER_DREAM = "Estava dirigindo um carro completamente desgovernado sem controle nenhum, mexer o volante não funcionava."
DREAM_CONTEXT = "Eu não tenho carro nem carteira de motorista, não sei dirigir."
USER_CONTEXT = "O paciente está sobrecarregado com TCC da faculdade, ele estuda e trabalha muito."

body = {
    "user_dream": USER_DREAM,
    "dream_context": DREAM_CONTEXT,
    "user_context": USER_CONTEXT,
}

response = requests.post(url, json=body)

print("Status:", response.status_code)
print(response.json())