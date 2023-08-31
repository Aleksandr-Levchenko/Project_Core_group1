import requests


class Connection:
    def get_json(self, url):
        raise NotImplementedError


class Request(Connection):
    def __init__(self, reqest: requests):
        self.reqest = reqest

    def get_json(self, url):
        response = self.reqest.get(url)
        return response.json()


class NewReqest(Connection):
    def get_json(self, url):
        return super().get_json(url)


# 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11'


class ApiClient:
    def __init__(self, fetch: Connection):
        self.fetch = fetch

    def get_json(self, url):
        return self.fetch.get_json(url)


def pretty_view(data: list[dict]):
    pattern = "|{:^10}|{:^10}|{:^10}|"
    print(pattern.format("currency", "sale", "buy"))
    for el in data:
        currency, *_ = el.keys()
        buy = el.get(currency).get("buy")
        sale = el.get(currency).get("sale")
        print(pattern.format(currency, sale, buy))


def data_adapter(data: dict) -> list[dict]:
    return [
        {
            f"{el.get('ccy')}": {
                "buy": float(el.get("buy")),
                "sale": float(el.get("sale")),
            }
        }
        for el in data
    ]


if __name__ == "__main__":
    client = ApiClient(Request(requests))
    data = client.get_json(
        "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11"
    )
    pretty_view(data_adapter(data))
import requests


class Connection:
    def get_json(self, url):
        raise NotImplementedError


class Request(Connection):
    def __init__(self, reqest: requests):
        self.reqest = reqest

    def get_json(self, url):
        response = self.reqest.get(url)
        return response.json()


class NewReqest(Connection):
    def get_json(self, url):
        return super().get_json(url)


# 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11'


class ApiClient:
    def __init__(self, fetch: Connection):
        self.fetch = fetch

    def get_json(self, url):
        return self.fetch.get_json(url)


def pretty_view(data: list[dict]):
    pattern = "|{:^10}|{:^10}|{:^10}|"
    print(pattern.format("currency", "sale", "buy"))
    for el in data:
        currency, *_ = el.keys()
        buy = el.get(currency).get("buy")
        sale = el.get(currency).get("sale")
        print(pattern.format(currency, sale, buy))
    return "Currency values ​​for today"


def data_adapter(data: dict) -> list[dict]:
    return [
        {
            f"{el.get('ccy')}": {
                "buy": float(el.get("buy")),
                "sale": float(el.get("sale")),
            }
        }
        for el in data
    ]

def get_currency():
    client = ApiClient(Request(requests))
    data = client.get_json(
        "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11"
    )
    return pretty_view(data_adapter(data))

if __name__ == "__main__":
    client = ApiClient(Request(requests))
    data = client.get_json(
        "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11"
    )
    pretty_view(data_adapter(data))