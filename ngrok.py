from pyngrok import ngrok
import config
ngrok.kill()
ngrok.set_auth_token(config.Auth)
http_tunnel = ngrok.connect(8050)
print (ngrok.get_tunnels())