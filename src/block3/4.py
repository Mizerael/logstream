import asyncio


class Payment_service:
    def __init__(self, name: str):
        self.name = name

    def check_active_operations(self) -> int:
        return 1

    async def create_operations(self) -> int:
        return 1

    async def confirm_operations(self) -> int:
        return 1


class Wallet:
    def __init__(self, name: str, val: str = "USD"):
        if not self.check_val(val):
            raise ValueError("Неверная валюта")
        self._balance: float = 0.0
        self.name: str = name
        self._val: str = val.upper()
        self._payment_service: Payment_service = None

    def _get_val_list(self) -> list[str]:
        return ["USD", "RUB", "GBR"]

    def check_val(self, val: str) -> bool:
        return val.upper() in self._get_val_list()

    def _check_unfinished_operations(self) -> int:
        if self._payment_service.check_active_operations():
            return 0
        return 1

    def change_payment(self, new_pay_service: Payment_service) -> (int, str):
        if self._payment_service is None:
            self._payment_service = new_pay_service
            return (1, "Система оплаты изменена успешно")
        if self._check_unfinished_operations():
            self._payment_service = new_pay_service
            return (1, "Система оплаты изменена успешно")
        else:
            return (0, "Невозможно выполнить операцию в данный момент")

    def get_balance(self) -> str:
        return f"Остаток на счете: {self._balance:.04f} {self._val.lower()}."

    def __del__(self) -> None:
        self._payment_service = None
        print(f"Кошелек {self.name} удален")

    async def top_up(self, amount: float) -> (int, str):
        if amount <= 0:
            return (2, "Отрицательное пополнение")
        resp = await self._payment_service.create_operations()
        if resp == 0:
            return (0, "Операция не создана")
        resp = await self._payment_service.confirm_operations()
        if resp == 0:
            return (3, "Операция не выполнена")
        self._balance += amount
        return (1, f"Пополнение на {amount:.04f} {self._val} выполнена")

    async def pay(self, amount: float) -> (int, str):
        if amount <= 0:
            return (2, "Отрицательная оплата")
        if amount > self._balance:
            return (3, "Операция превышает доступный баланс")
        resp = await self._payment_service.create_operations()
        if resp == 0:
            return (0, "Операция не создана")
        resp = await self._payment_service.confirm_operations()
        if resp == 0:
            return (0, "Операция не выполнена")
        self._balance -= amount
        return (1, f"Оплата на {amount:.04f} {self._val} выполнена")


class CryptoWallet(Wallet):
    def __init__(self, name: str, coin: str = "BTC"):
        if not self.__check_coin(coin):
            raise ValueError("Неверный коин")
        super().__init__(name)
        self._coin = coin.upper()

    def get_coin_rate_in_usd(self) -> dict:
        return {"BTC": 72000, "ETH": 3500}

    def __check_coin(self, coin: str) -> bool:
        return coin.upper() in self.get_coin_rate_in_usd().keys()

    def __convert_coins_to_usd(self) -> float:
        return self._balance * self.get_coin_rate_in_usd().get(self._coin)

    def get_usd_balance(self) -> str:
        return f"Остаток {self.__convert_coins_to_usd():.04f} {self._val}."

    def get_balance(self) -> str:
        return f"Остаток {self._balance:.04f} {self._coin}."

    async def top_up(self, coins: float) -> (int, str):
        if coins <= 0:
            return (2, "Отрицательное пополнение")
        resp = await self._payment_service.create_operations()
        if resp == 0:
            return (0, "Операция не создана")
        resp = await self._payment_service.confirm_operations()
        if resp == 0:
            return (3, "Операция не выполнена")
        self._balance += coins
        return (1, f"Пополнение на {coins:.04f} {self._coin} выполнена")

    async def pay(self, coins: float) -> (int, str):
        if coins <= 0:
            return (2, "Отрицательная оплата")
        if coins > self._balance:
            return (3, "Операция превышает доступный баланс")
        resp = await self._payment_service.create_operations()
        if resp == 0:
            return (0, "Операция не создана")
        resp = await self._payment_service.confirm_operations()
        if resp == 0:
            return (0, "Операция не выполнена")
        self._balance -= coins
        return (1, f"Оплата на {coins:.04f} {self._coin} выполнена")


async def task4() -> None:
    pay = Payment_service("abbobba")
    new_wallet = Wallet("aboba", "rub")
    print(new_wallet.change_payment(pay))
    print(new_wallet.get_balance())
    status = await new_wallet.top_up(400)
    print(status, new_wallet.get_balance())
    status = await new_wallet.pay(500)
    print(status, new_wallet.get_balance())
    status = await new_wallet.pay(200)
    print(status, new_wallet.get_balance())
    del new_wallet

    new_crypto_wallet = CryptoWallet("crypto_aboba", "ETH")
    print(new_crypto_wallet.change_payment(pay))
    print(new_crypto_wallet.get_balance())
    status = await new_crypto_wallet.top_up(2)
    print(status, new_crypto_wallet.get_balance())
    status = await new_crypto_wallet.pay(2.3)
    print(
        status,
        new_crypto_wallet.get_balance(),
        new_crypto_wallet.get_usd_balance(),
    )
    status = await new_crypto_wallet.pay(1.9)
    print(
        status,
        new_crypto_wallet.get_balance(),
        new_crypto_wallet.get_usd_balance(),
    )
    del new_crypto_wallet


if __name__ == "__main__":
    asyncio.run(task4())
