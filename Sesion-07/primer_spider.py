import scrapy

# Construir una clase hija de scrapy.Spider
class CitasSpider(scrapy.Spider):
    # Nombre a la araña
    name = "citas"
    # Indicar la url o link de la página
    start_urls = [
        "http://quotes.toscrape.com/",
    ]
    
    # Definir la función o método encargado de procesar la data
    def parse(self, respuesta):
        # Vamos a iniciar la búsqueda de las citas
        # <div class="quote" ...>...</div>
        for cita in respuesta.css("div.quote"):
            # Regresar sólo una cita
            yield {
                "texto" : cita.css("span.text::text").get(),
                "autor" : cita.xpath("span/small/text()").get(),
            }
            