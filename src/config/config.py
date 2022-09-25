from pydantic import BaseSettings


CONFIG_PREFIX = 'FASTAPI_SERVICE_'


class Service(BaseSettings):
    port: int
    host: str
    reload: bool = True

    class Config:
        env_prefix = CONFIG_PREFIX
        env_file = '.env'


class Mongo(BaseSettings):
    username: str
    password: str
    host: str
    port: int

    class Config:
        env_prefix = CONFIG_PREFIX + "MONGO_"
        env_file = '.env'


class Kafka(BaseSettings):
    host: str
    port: int

    class Config:
        env_prefix = CONFIG_PREFIX + 'KAFKA_'
        env_file = '.env'


class LamodaUrls(BaseSettings):
    women_clothes_url = 'https://www.lamoda.by/c/355/clothes-zhenskaya-odezhda/?sitelink=topmenuW&l=2&page='
    # women_shoes_url = 'https://www.lamoda.by/c/15/shoes-women/?sitelink=topmenuW&l=3&page='
    # women_accessories_url = 'https://www.lamoda.by/c/557/accs-zhenskieaksessuary/?sitelink=topmenuW&l=4&page='

    men_clothes_url = 'https://www.lamoda.by/c/477/clothes-muzhskaya-odezhda/?sitelink=topmenuM&l=2&page='
    # men_shoes_url = 'https://www.lamoda.by/c/17/shoes-men/?sitelink=topmenuM&l=3&page='
    # men_accessories_url = 'https://www.lamoda.by/c/559/accs-muzhskieaksessuary/?sitelink=topmenuM&l=4&page='
    #
    # girls_clothes_url = 'https://www.lamoda.by/c/1590/clothes-dlia-devochek/?page='
    # girls_shoes_url = 'https://www.lamoda.by/c/203/shoes-girls/?page='
    # girls_accessories_url = 'https://www.lamoda.by/c/561/accs-detskieaksessuary/?page='
    #
    # boys_clothes_url = 'https://www.lamoda.by/c/1589/clothes-dlia-malchikov/?page='
    # boys_shoes_url = 'https://www.lamoda.by/c/205/shoes-boys/?page='
    # boys_accessories_url = 'https://www.lamoda.by/c/5381/default-aksydlyamalchikov/?page='
    #
    # newborns_clothes_url = 'https://www.lamoda.by/c/5598/clothes-newbornclothes/?page='
    # newborns_shoes_url = 'https://www.lamoda.by/c/5599/shoes-kidsnewborn/?page='
    # newborns_accessories_url = 'https://www.lamoda.by/c/5600/accs-newbornaccs/?page='


class Config:
    service: Service = Service()
    mongo: Mongo = Mongo()
    kafka: Kafka = Kafka()
    lamoda_urls: LamodaUrls = LamodaUrls()
