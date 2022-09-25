from bs4 import BeautifulSoup
import httpx

from src.dao.kafka import KafkaHandler
from src.app.container_controller import ContainerController
from src.config.config import Config


class LamodaParser:
    def __init__(
            self,
            kafka: KafkaHandler,
            config: Config,
            container_controller: ContainerController
    ):
        self._kafka: KafkaHandler = kafka
        self._config: Config = config
        self._container_controller = container_controller

    @property
    def config(self):
        return self._config

    @property
    def container_controller(self):
        return self._container_controller

    @property
    def kafka(self):
        return self._kafka

    async def parse_products(self, url, base_data):
        page_number = 1
        prod_list = []
        while True:
            url += str(page_number)
            async with httpx.AsyncClient() as client:
                request = await client.get(url)
            soup = BeautifulSoup(request.text)
            product_div_list = soup.findAll('div', class_='x-product-card__card')

            page_number += 1

            if len(product_div_list) == 0:
                return prod_list

            for product_div in product_div_list:
                data = {}
                price = product_div.find('span', class_='x-product-card-description__price-WEB8507_price_no_bold')
                data['price'] = price.text
                brand = product_div.find('div', class_='x-product-card-description__brand-name')
                data['brand'] = brand.text
                desc = product_div.find('div', class_='x-product-card-description__product-name')
                data['description'] = desc.text
                data = {**data, **base_data}
                prod_list.append(data)
                # self.container_controller.lamoda.create(data=data)

    async def lamoda_parse(self):
        list1 = await self.parse_products(
            url=self.config.lamoda_urls.women_clothes_url,
            base_data={
                'sex': 'women',
                'type': 'clothes'
            }
        )

        list2 = await self.parse_products(
            url=self.config.lamoda_urls.men_clothes_url,
            base_data={
                'sex': 'men',
                'type': 'clothes'
            }
        )
        await self.container_controller.lamoda.create_list(list1)
        await self.container_controller.lamoda.create_list(list2)
