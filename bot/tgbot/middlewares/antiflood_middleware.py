from telebot.asyncio_handler_backends import BaseMiddleware
from telebot.async_telebot import CancelUpdate


class AntiFloodMiddleware(BaseMiddleware):
    def __init__(self, limit, bot) -> None:
        self.last_time = {}
        self.limit = limit
        self.update_types = ['message']
        self.bot = bot

    async def pre_process(self, message, data):
        if message.text != '/spam':
            return
        if not message.from_user.id in self.last_time:
            self.last_time[message.from_user.id] = message.date
            return
        if message.date - self.last_time[message.from_user.id] < self.limit:
            await self.bot.send_message(message.chat.id,
                                        'You are making request too often')
            return CancelUpdate()
        self.last_time[message.from_user.id] = message.date

    async def post_process(self, message, data, exception):
        pass
