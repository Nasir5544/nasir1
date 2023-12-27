
from scrapy.loader import ItemLoader

from itemloaders.processors import MapCompose,TakeFirst

class qneProductLoader(ItemLoader):
    
    
    default_output_processor= TakeFirst()
    price_in = MapCompose(lambda x : x.split("Rs.")[-1] )
    save_price = MapCompose(lambda x : x.split("Rs.")[-1] )
    description=MapCompose(lambda x : x.split("Rs.")[-1] )
    url_in=MapCompose(lambda x : 'https://qne.com.pk' + x)
    
   
    
   # save_price = MapCompose(lambda x: x.replace("Rs.", ""))

    