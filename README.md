# Instruções para iniciar o projeto

- Instalar o docker e docker-compose dentro da máquina virtual

  - Instalar docker https://www.vivaolinux.com.br/dica/Instalacao-do-Docker-no-Linux-Mint-20
  
  - Instalar docker-compose https://docs.docker.com/compose/install/

- Navegar usando o terminal até diretório raiz do projeto (onde tem o arquivo docker-compose.yml)
- Executar o seguinte comando:
``` docker-compose up```

- Acessar no navegador: localhost:4200


### Observações
1. O frontend pega as informações em tempo real de um arquivo chamado ```dados.json```. Ele se encontra no caminho: ./accounting-viewer/src/assets/dados.json
2. Os links que coloquei para instalação do docker e docker-compose é para funcionar. Caso não de certo a instalação, dá para tentar ver a versão certinha do Mint e tentar ver algum tutorial mais expecifico
