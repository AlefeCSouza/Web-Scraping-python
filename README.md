🌤️ Web Scraper - Previsão do Tempo para São Paulo

Este projeto consiste em um **web scraper simples** escrito em Python para capturar automaticamente a temperatura atual e a descrição do clima em São Paulo, utilizando o site [Tempo.com](https://www.tempo.com/sao-paulo.htm).

---

## 🎯 Objetivo

O objetivo principal do projeto é demonstrar o uso das bibliotecas `requests` e `BeautifulSoup` para:
- Realizar **requisições HTTP** a uma página web.
- **Processar o conteúdo HTML** recebido.
- Extrair e exibir dados específicos da estrutura da página, como temperatura e descrição das condições climáticas.

Este projeto pode servir como base para outras aplicações, como:
- Alertas meteorológicos
- Dashboards climáticos
- Integração com chatbots
- Sistemas de agendamento e monitoramento automático

---

## 🛠️ Como funciona

1. O código utiliza `requests.get()` para acessar o site da previsão do tempo.
2. Com `BeautifulSoup`, ele **interpreta o HTML** e busca pelos elementos que contêm:
   - **Temperatura atual** (`<span>` com classe `dato-temperatura changeUnitT`)
   - **Descrição do clima** (`<span>` com classe `descripcion`)
3. Por fim, ele imprime essas informações no terminal.

---

## 🧑‍💻 Tecnologias utilizadas

- **Python 3.x**
- **[Requests](https://pypi.org/project/requests/)** — para fazer requisições HTTP.
- **[BeautifulSoup (bs4)](https://www.crummy.com/software/BeautifulSoup/)** — para processar e extrair dados da estrutura HTML
