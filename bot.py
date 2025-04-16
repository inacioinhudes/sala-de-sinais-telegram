import os
import random
import asyncio
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

jogos = [
    "Fortune Tiger", "Fortune Rabbit", "Fortune Mouse",
    "Fortune Ox", "Fortune Gems", "Fortune Gems 2"
]

estrategias = [
    "ENTRAR APÓS 2 TIGRES", "ENTRAR APÓS 3 COELHOS",
    "ENTRAR APÓS 1 TIGRE E 1 COELHO", "SEQUÊNCIA DE GEMS = ENTRADA"
]

link_afiliado = "https://9276jogo.site/?pid=29056940"

async def enviar_sinal():
    while True:
        jogo = random.choice(jogos)
        estrategia = random.choice(estrategias)

        hora_atual = datetime.now()
        horario_entrada = hora_atual + timedelta(minutes=5)
        hora_formatada = horario_entrada.strftime("%H:%M")

        mensagem = (
            f"**NOVO SINAL ENVIADO**\n\n"
            f"JOGO: {jogo}\n"
            f"ESTRATÉGIA: {estrategia}\n"
            f"HORÁRIO DE ENTRADA: {hora_formatada}\n\n"
            f"⚠️ Aguarde confirmação antes de iniciar.\n"
        )

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("JOGUE AGORA", url=link_afiliado)]
        ])

        await bot.send_message(chat_id=CHAT_ID, text=mensagem, parse_mode="Markdown", reply_markup=keyboard)
        await asyncio.sleep(420)  # 7 minutos

async def main():
    await enviar_sinal()

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.run_polling()  # apenas pra manter o app vivo
    asyncio.run(main())