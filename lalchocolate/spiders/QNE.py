import scrapy
import logging
from lalchocolate.items import qneProduct
from lalchocolate.itemloaders import qneProductLoader



class LalsChocolatesSpider(scrapy.Spider):
    
    name = 'qne'
    allowed_domain=['qne.com.pk']
    start_urls = ['https://qne.com.pk/']
  

    def parse(self, response):
        
        products = response.css('.product-item')
        
        #qne_item=qneProduct()
        for product in products:
            
         try:
          
                
                   productloader= qneProductLoader(item = qneProduct(), selector = product)
                   productloader.add_css('name','a.product-item__title::text'),
                   productloader.add_css ('price','span.price',re='<span class="price price--highlight">\n                <span class="visually-hidden">Sale price</span>(.*)</span>'),
                   productloader.add_css ('url','div.product-item a::attr(href)'),
                   productloader.add_css ('saveprice','span.product-label.product-label--on-sale span::text')
                  # productloader.add_css('description','div.rte.text--pull > div::text')
                  
                   

                   
                   #productloader.add_value('description', lambda x: x.get())

                   #productloader.add_css ('description','div.rte.text--pull > div::text')
                   
                   #productloader.add_css('saveprice','span.product-label',re='<span class="product-label product-label--on-sale">Save </span>(.*)</span>')
                   # productloader.add_css('saveprice','span.product-label.product-label')
                   #'saveprice':product.css('span.product-label').get().replace('<span class="product-label product-label--on-sale">Save <span>','').replace('</span>','')
                 
                   #'saveprice':product.css('span.product-label').get().replace('<span class="product-label product-label--on-sale">Save <span>','').replace('</span>','')
                

                   #print(qneProduct.get('saveprice'))
                   yield productloader.load_item()
           
         except KeyError as e:
          logging.error(f"KeyError: {e}")

                
        next_page = response.css('[rel="next"] ::attr(href)').get()

        if next_page is not None:
           next_page_url = 'https://qne.com.pk' + next_page
           yield response.follow(next_page_url, callback=self.parse_detail)
           
           
           
           
    def parse_detail(self, response):
        
      
        item = response.css['.cards']
         
        
        item_loader =qneProductLoader (item=item, selector=response)
        
        
        descriptions = response.css('div.rte.text--pull > div::text').get()
        print(descriptions)
        
          
        yield item_loader.load_item()
           
   
""" class description(scrapy.Spider):
       
     name = 'des'
     allowed_domain=['https://qne.com.pk']
     start_urls = ['https://qne.com.pk/collections/pepsico/products/slice-mango-juice-200ml-x-24pcs-case']
     
     def parse(self, response):
     
      yield{
          
            'description':response.css('div.rte.text--pull > div::text').get(),
            
          } """
      