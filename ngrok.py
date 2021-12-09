from pyngrok import ngrok
ngrok.kill()
Auth = " " #colocar a autenticação do ngrok (só basta criar uma conta)
ngrok.set_auth_token(Auth)
http_tunnel = ngrok.connect(8050)
print (ngrok.get_tunnels())