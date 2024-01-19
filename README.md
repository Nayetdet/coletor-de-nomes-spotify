# Coletor de Nomes Spotify
Este é um script Python simples que recebe um URL do Spotify e extrai informações sobre as faixas associadas, gerando uma lista de reprodução no formato **artista - título**. O script é útil para converter links do Spotify em uma lista de faixas reproduzíveis.

## Pré-requisitos
Antes de executar o script, é necessário configurar as credenciais do Spotify. Certifique-se de ter um arquivo .env no mesmo diretório do script com as seguintes informações:

```
client_id = SEU_ID
client_secret = SEU_ID_SECRETO
```

> Você pode obter suas credenciais do Spotify aqui: https://developer.spotify.com

## Instalação e Uso
Ao colocar cada um dos arquivos desta página em alguma pasta, execute o arquivo run.bat e insira um URL do Spotify quando solicitado. O script analisará o URL e criará um arquivo de saída chamado output.txt contendo a lista de faixas.

## Notas
- O script suporta URLs de álbuns, artistas, faixas, playlists e shows, mas não oferece suporte a podcasts.
- Certifique-se de ter permissões adequadas para escrever no diretório onde o script está sendo executado.
- Este código não está completo, portanto, não possui um tratamento de erros adequado (ele é praticamente inexistente, na verdade), então muitos bugs podem ser encontrados.
