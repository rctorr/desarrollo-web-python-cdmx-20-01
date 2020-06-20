import scrapy

# Construir una clase hija de scrapy.Spider
class ProductoSpider(scrapy.Spider):
    # Nombre a la araña
    name = "producto"
    # Indicar la url o link de la página
    start_urls = [
        "https://www.mercadolibre.com.mx/ofertas",
    ]
    contador = 1
    
    # Definir la función o método encargado de procesar la data
    def parse(self, respuesta):
        # Vamos a iniciar la búsqueda de los datos de producto
        for producto in respuesta.css("div.promotion-item__container"):
        # Regresar sólo una producto
            yield {
                "nombre" : producto.css("p.promotion-item__title::text").get(),
            }
                
        # Navegando a la siguiente página
        pag_sig = respuesta.css("li.andes-pagination__button--next a::attr('href')").get()
        if pag_sig is not None and self.contador <= 10:
            yield respuesta.follow(pag_sig, self.parse)
            self.contador += 1