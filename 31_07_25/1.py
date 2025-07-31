"""
ЗАДАЧА: Асинхронная валидация пользователей с повторными попытками

АНАЛИЗ КОДА:
Рассмотрим следующий код:

"""
async def isUserValid(self, user):
    for i in range(3):
        try:
            r = await self.request("validate", user.toJson())
            if r.ok == True:
                return True
        except Exception:
            time.sleep(0.1)