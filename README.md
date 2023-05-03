SPRO Case
==============================

<p align='center'>
    <img src = 'imgs/spro.jpeg'>
</p>
<br>  
O case trabalhado teve como objetivo testar as habilidades de criação de dataframes, um banco em MongoDB e aggregate em js.

No arquivo create_data.py estabelece a conexão com o banco de dados MongoDB, cria as tabelas abaixo e insere nas collections indicadas conforme orientações na pasta /docs. 

|Carro| Cor | Montadora |
|-----|-------|----------|
|Onix |Prata | Chevrolet |
|Polo | Branco | Volkswagen |
|Sandero | Prata |	Renault |
|Fiesta	| Vermelho | Ford |
|City |	Preto |	Honda|

<br>

| Montadora | País |
|-----------|------|
| Chevrolet | EUA  |
| Volkswagen | Alemanha |
| Renault | Franca |
| Ford | EUA |
| Honda | Japao |

No arquivo aggregate.js executa a agregação dos dados mostrando as informações conforme imagem abaixo:
<p align='center'>
    <img src = 'imgs/contagem_montadoras.png'>
</p>

No arquivo sum_countries.js executa a agregação sumarizando a quantidade de veículos/montadora por país, conforme imagem abaixo:
<p align='center'>
    <img src = 'imgs/total_carros_paises_2.png'>
</p>
