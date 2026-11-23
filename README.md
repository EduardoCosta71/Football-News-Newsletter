# Football News Newsletter

Sistema de automação de notícias de futebol desenvolvido com Python e Flask, integrado a APIs externas e Inteligência Artificial para coletar, processar e resumir notícias esportivas.

## Sobre o projeto

O Football News Newsletter tem como objetivo automatizar a coleta de notícias sobre futebol, utilizando APIs externas para obter informações atualizadas e Inteligência Artificial para gerar resumos que podem ser utilizados em uma newsletter.

A aplicação também permite que usuários realizem inscrições para receber conteúdos relacionados ao futebol.

## Tecnologias utilizadas

- **Python:** linguagem principal do projeto.
- **Flask:** desenvolvimento da aplicação web.
- **SQL Server:** armazenamento de usuários inscritos e notícias.
- **HTML e CSS:** estrutura e estilização das páginas.
- **JavaScript:** funcionalidades da interface.
- **n8n:** automação dos processos de coleta e processamento de notícias.
- **Google Gemini:** geração de resumos utilizando Inteligência Artificial.
- **GNews API:** obtenção de notícias esportivas.
- **Football-Data.org API:** consulta de informações sobre competições e partidas.

## Funcionalidades

- Consulta de notícias esportivas por meio de APIs externas.
- Exibição de informações sobre competições e partidas.
- Cadastro de usuários interessados na newsletter.
- Armazenamento de informações utilizando SQL Server.
- Automação da coleta e do processamento de notícias.
- Geração de resumos de notícias com Inteligência Artificial.

## Estrutura do projeto

```text
Football-News-Newsletter/
│
├── app/
│   ├── services/
│   │   └── football_api.py
│   ├── templates/
│   │   ├── index.html
│   │   └── inscricao.html
│   └── static/
│
├── run.py
├── requirements.txt
└── README.md
```

## Configuração do ambiente

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta:

```bash
cd Football-News-Newsletter
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure as variáveis de ambiente no arquivo `.env`, utilizando suas próprias chaves de API e configurações de banco de dados.

Execute a aplicação:

```bash
python run.py
```

## Status do projeto

Em desenvolvimento.

A aplicação web e as integrações com APIs estão sendo desenvolvidas. A automação com n8n e a integração com Inteligência Artificial estão em fase de implementação.

## Autor

**Eduardo Costa Borges**

Desenvolvedor Backend | Python | Flask | SQL Server | APIs REST
