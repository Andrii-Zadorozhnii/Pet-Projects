import requests
from typing import Dict
from API_KEYS import CURRENCY_EXCHANGE_API

API_URL = f"https://v6.exchangerate-api.com/v6/{CURRENCY_EXCHANGE_API}/latest/USD"


def get_exchange_rates(base_currency: str) -> Dict[str, float]:
    """Получает курсы обмена для указанной валюты."""
    url = API_URL.format(CURRENCY_EXCHANGE_API, "USD")
    response = requests.get(url)
    data = response.json()

    # print("API response:", data)

    if "error" in data:
        raise ValueError(f"Ошибка API: {data['error-type']}")

    return data.get("conversion_rates", {})


def convert_currency(amount: float,
                     from_currency: str,
                     to_currency: str) -> float:
    """Конвертирует сумму из одной валюты в другую."""
    rates = get_exchange_rates(from_currency)

    if to_currency not in rates:
        raise ValueError(f"Неверный код валюты: {to_currency}")

    return amount * rates[to_currency]


if __name__ == "__main__":
    from_currency = "USD"
    to_currency = "EUR"
    amount = 100

    try:
        converted_amount = convert_currency(amount,
                                            from_currency,
                                            to_currency)
        print(
            f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
        )
    except ValueError as e:
        print("Ошибка:", e)