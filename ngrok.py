from pyngrok import ngrok
ngrok.kill()
Auth = "1zBoQHUSj63plTXkl9SAtzNcZXy_49rPmuaR7YZmW7tCaqN6N"
ngrok.set_auth_token(Auth)
http_tunnel = ngrok.connect(8050)
print (ngrok.get_tunnels())