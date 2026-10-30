from app.services.news_api import search_news, format_news

noticias = search_news()

noticias_formatadas = format_news(noticias)

for noticia in noticias_formatadas:

    print("Título:", noticia["titulo"])
    print("Fonte:", noticia["fonte"])
    print("Descrição:", noticia["descricao"])
    print("Link:", noticia["link"])