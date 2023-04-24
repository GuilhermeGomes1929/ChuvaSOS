import firebase_admin
from firebase_admin import credentials, messaging

def subscribe_to_topic(token):
    topic = "warning"

    response = messaging.subscribe_to_topic(token, topic)

    if response.failure_count > 0:
        print(f'Houve um erro ao registrar o token no tópico. Erros: {list(map(lambda e: e.reason, response.errors))}')
    else:
        print("Token registrado com sucesso")


def send_notification_to_topic(title, body):
    topic = "warning"

    message = messaging.Message(
                notification = messaging.Notification(
                        title=title,
                        body=body
                    ),
                topic=topic
            )
    messaging.send(message)
    print("Notificação enviada com sucesso")


firebase_cred = credentials.Certificate("/home/guilherme/Projetos/ChuvaSOS/firebase_settings/credentials.json")

firebase_app = firebase_admin.initialize_app(firebase_cred)
while True:
    print("Menu de opções:")
    print("1 - Registrar token no tópico 'Alerta de chuva'")
    print("2 - Enviar notificação")
    print("3 - Sair")
    choice = int(input())

    if choice == 1:
        token = input("Cole o token aqui: ")
        subscribe_to_topic(token)
    if choice == 2:
        title = input("Digite o titulo da mensagem: ")
        body = input("Digite o corpo da notificação: ")
        send_notification_to_topic(title, body)
    if choice == 3:
        break
    else: 
        print("Digite uma opção válida")
    print("\n")



