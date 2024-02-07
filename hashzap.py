# pip install flet

# título hashzap
# botão de iniciar o chat
#     popup
#         bem vindo ao hashzap
#         escreva seu nome
#         entrar no chat
# chat
#     filipe entrou no chat
#     mensagens do usuário
# campo para enviar mensagem
# batão de enviar
import flet as ft 

def main(pagina):
    titulo = ft.Text("Hashzap")

    nome_usuario = ft.TextField(label="Escreva seu nome")

    chat = ft.Column()
   
    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagen.value}" 
        pagina.pubsub.send_all(texto_campo_mensagem)
        campo_mensagen.value = ""
        pagina.update()

    campo_mensagen = ft.TextField(label="Escreva sua mensagem aqui", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_chat(evento):
        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.add(chat)
        linha_mensagem = ft.Row(
            [campo_mensagen, botao_enviar])
        pagina.add(linha_mensagem)
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)
        pagina.update()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Hashzap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Enter", on_click=entrar_chat)]
        )

    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)

    pagina.add(titulo)
    pagina.add(botao_iniciar)

# ft.app(main)
ft.app(main, view=ft.WEB_BROWSER)