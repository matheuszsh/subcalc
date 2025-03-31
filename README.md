# 📡 Subcalc - Subnet Calculator CLI
Subcalc é uma ferramenta de linha de comando (CLI) para cálculo de sub-redes. Permite determinar máscaras de sub-rede, endereços IP válidos e outras informações úteis para administradores de redes e entusiastas de T.I.

## 📌 Características
### ✅ Cálculo automático de sub-redes com base no CIDR
### ✅ Conversão de CIDR para máscara de sub-rede
### ✅ Fácil de usar via terminal
### ✅ Suporte para Windows(Linux sem instalador)

## 🔧 Instalação

1. Baixe o repositório com o comando `git clone https://github.com/matheuszsh/subcalc`
2. Execute o arquivo `Installe-subcalc-program`(RECOMENDADO)
3. Modifique as variáveis de ambiente do sistema, e adicione o caminho de onde o programa foi instalado ao PATH(RECOMENDADO)
4. Abra o powershell ou prompt de comando e chame o programa: `subcalc`(RECOMENDADO)
  
Caso ignore os recomendados, com o python3=<* instalado na sua máquina, execute o programa no próprio diretório do arquivo principal:`python .\subcalc.py`

OBS: Essa opção é para caso você queira rodar o programa globalmente no seu ambiente de linha de comando.

## 🚀 Modo de uso

### Comando básico:
Exemplo: `subcalc -ip 192.168.0.0 -mc 24 -sc 26`

### Opções disponíveis:

```
  Subnetwork calculation tool

options:
  -h, --help            show this help message and exit
  -ip, --internet-address INTERNET_ADDRESS
                        use this option to specify the ip address.
  -mc, --main-cidr MAIN_CIDR
                        use this option to specify the main net cidr
  -sc, --sub-cidr SUB_CIDR
                        use this option to specify the subnet cidr
  -vmc, --verbose-maincidr
                        use this option to show the subnet cidr data
  -vsc, --verbose-subcidr
                        use this option to show the subnet cidr data
  -ns, --no-subnets     use this option to hidde subnet list
```
### Exemplo de uso

```
subcalc -ip 192.168.0.0 -mc 23 -sc 24 -vmc -vsc

------------MAIN NET CIDR--------

IP: 192.168.0.0/23
Netmask: 255.255.254.0
Total Ips: 512
Hosts available: 510
Network: 1
Broadcast: 1
Bits to hosts: 9

-----------SUBNET CIDR-----------

IP: 192.168.0.0/24
Netmask: 255.255.255.0
Total networks: 2
Total ip per networks: 256
Total host per networks: 254
Network: 1
Broadcast: 1
Bits to hosts: 8

<><><><><><><><>|SUBNET LIST|<><><><><><><><>

------NETWORK 1------
NETWORK: 192.168.0.0
HOST: 192.168.0.1 - 192.168.0.254
BROADCAST: 192.168.0.255

------NETWORK 2------
NETWORK: 192.168.1.0
HOST: 192.168.1.1 - 192.168.1.254
BROADCAST: 192.168.1.255
```

## 🛠 Tecnologias Utilizadas
* Python 3.x
* calcCIDR.py (Modulo personalizado para transformar CIDR em Mascara de rede)
* argparse (interpretação de argumentos de terminal)
* ipaddress (cálculo de redes IP)
* PyInstaller (geração do executável)
* Inno Setup (criador do instalador para Windows)

# 📜 Licença
Este projeto é licenciado sob a MIT License.

# 👨‍💻 Contribuição
Se quiser contribuir, siga estes passos:

* Faça um fork do repositório
* Crie um branch: git checkout -b minha-feature
* Faça suas alterações e commit: git commit -m "Nova funcionalidade"
* Envie para o GitHub: git push origin minha-feature
* Abra um Pull Request
