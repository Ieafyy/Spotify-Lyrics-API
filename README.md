# Spotify-Lyrics-API
Sistema desenvolvido em Python para comunicar diretamente com o Spotify e retornar em tempo real a música e a letra que o usuário está escutando

![image](https://user-images.githubusercontent.com/70926962/173472323-6b82c053-6f0e-47d9-8ed0-9dc8f6a2bacd.png)

![image](https://user-images.githubusercontent.com/70926962/173472682-a3116578-e8af-44aa-9b3b-421e4fc5d20c.png)

O sistema (escrito em python) utiliza da lib Requests para realizar a comunicação e a autenticação com a API do Spotify. Após a conecção estabelecida, o frontend
(escrito com jquery) faz requisições do tipo GET com o backend para atualizar em tempo real o nome da música, nome do artista, duração, tempo atual, capa do
albúm e letra da música. A letra é obtida a partir da API da plataforma Vagalume.

----------------------------------

!!! O sistema possui um certo delay (devido a conecção com o servidor do Heroku), por isso, em caso de não atualizar em tempo real, por favor, atualize a página !!!

<a href="https://autolyricsspotify.herokuapp.com/">Dê uma olhada apartir deste link!</a>
