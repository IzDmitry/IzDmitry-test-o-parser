from telebot.asyncio_handler_backends import State, StatesGroup


class Register(StatesGroup):
    """
    Group of states for registering
    """
    value = State()
