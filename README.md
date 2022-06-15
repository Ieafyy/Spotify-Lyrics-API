# Spotify-Lyrics-API
Sistema desenvolvido em Python para comunicar diretamente com o Spotify e retornar em tempo real a música e a letra que o usuário está escutando

![image](https://user-images.githubusercontent.com/70926962/173472323-6b82c053-6f0e-47d9-8ed0-9dc8f6a2bacd.png)

![image](https://user-images.githubusercontent.com/70926962/173472682-a3116578-e8af-44aa-9b3b-421e4fc5d20c.png)

O sistema foi escrito em Python, usando a lib Flask para criação do servidor. A comunicação com a API do Spotify acontece a partir do frontend utilizando a biblioteca para JavaScript Jquery, realizando todas as requisições para validação do Token de segurança e obtenção dos valores (nome da música, artista, capa do album, duração e tempo atual). A letra foi obtida a partir da API do Vagalume e o processo também foi todo realizado pelo frontend. 

----------------------------------

<h2>DETALHE</h2>

Segundo palavras do Spotify:

<h4>
"If your app is in development mode up to 25 Spotify users can install and use your app. These users must be explicitly added under the section "Users and Access" before they can authenticate with your app. If you’d like to ship your app to a broader audience, let us know by submitting a quota extension request."
</h4>

Como o status do app é setado como "Development Mode" ("Please note that we will not grant a quota extension for home automation, school, or hobby projects", ou seja, não oficializam projetos de "hobbystas"), apenas 25 usuários podem usar o sistema simultaneamente e todos estes devem ser referenciados explicitamente no menu "Users and Access". Por isso, usuários fora dessa lista (infelizmente) não obterão nenhum resultado usando o app. 


De qualquer maneira, o sistema pode ser acessado <a href="https://autolyricsspotify.herokuapp.com/">por aqui</a>.
