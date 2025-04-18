from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto, InputMediaVideo
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from datetime import datetime, timedelta
import random
from flask import Flask
import threading
import os

# Configuração do Flask para manter o bot online
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot está rodando!"

def run_web():
    app.run(host="0.0.0.0", port=8080)

threading.Thread(target=run_web, daemon=True).start()

# Configuração do Bot
API_ID = 29530163
API_HASH = "6066497fd46d35ea3dac9a179e27047b"
BOT_TOKEN = "7871641813:AAHrd2CU5DXt-Tm90yFYB1R9TD7psyPEMms"
CHANNEL_ID = "@Avontzzp"

# Imagens associadas aos jogos
IMAGENS_JOGOS = {
    "Fortune Snake 🐍": "A:/garimpo digital/Figurinhas Slots/PG/8.jpg",
    "Fortune Mouse 🐹": "A:/garimpo digital/Figurinhas Slots/PG/mouse.png",
    "Fortune Tiger 🐯": "A:/garimpo digital/Figurinhas Slots/PG/iger.png",
    "Gates of Olympus ⚡": "A:/garimpo digital/Figurinhas Slots/PP/gates.png",
    "Fortune Dragon 🐉": "A:/garimpo digital/Figurinhas Slots/PG/ortunedragon.png",
    "Fortune Gems 💎": "A:/garimpo digital/Figurinhas Slots/Jili/cff409b19.jpg",
    "Fortune OX 🐂": "A:/garimpo digital/Figurinhas Slots/PG/ox.png",
    "Double Fortune 🎎": "A:/garimpo digital/Figurinhas Slots/PG/df.png",
    "Jackpot Joker 🎰🃏": "imagens/jackpot_joker.jpg",
    "Fortune Gems 2 💎": "A:/garimpo digital/Figurinhas Slots/Jili/OIP.jpg",
    "Fortune Gems 3 💎": "A:/garimpo digital/Figurinhas Slots/Jili/maxresdefault (1).jpg",
    "PartyStar 🐇": "imagens/partystar.jpg",
    "Big Bass Splash 🎣": "A:/garimpo digital/Figurinhas Slots/PP/igbasssplash.png",
    "Cash Mania": "A:/garimpo digital/Figurinhas Slots/Jili/OIP (2).jpg",
    "Wild Bandito 💀": "A:/garimpo digital/Figurinhas Slots/PG/wildbandito.png",
    "Master Joker 🃏": "A:/garimpo digital/Figurinhas Slots/PP/masterjoker.png",
    "Big Bass Hold & Spinner 🎣": "imagens/big_bass_hold_spinner.jpg",
    "Lucky Neko 😺": "A:/garimpo digital/Figurinhas Slots/PG/lukyneko.png",
    "Aztec Gems Deluxe 🍃": "imagens/aztec_gems_deluxe.jpg",
    "Rio Fantasia 🐦‍🔥": "A:/garimpo digital/Figurinhas Slots/PG/participe-das-comemoracoes-do-carnaval-com-o-rio-fantasia-da-pg-soft-2.png",
    "DevilFire 2 🔱": "imagens/devilfire2.jpg",
    "Lucky Piggy 🐷": "A:/garimpo digital/Figurinhas Slots/PG/luicky piggy.png",
    "Super Market Spree 🛒": "A:/garimpo digital/Figurinhas Slots/PG/supermarket.png",
    "Fortune Pig 🐷": "A:/garimpo digital/Figurinhas Slots/PG/OIP.jpg",
    "Wings Of !Guazu 🍀": "A:/garimpo digital/Figurinhas Slots/PG/pg-soft-faz-sucesso-com-o-lancamento-de-wings-of-iguazu.png",
    "Piggy Gold 🐷": "A:/garimpo digital/Figurinhas Slots/PG/piggygold.png",
}

# Jogos disponíveis
jogos = {
    "Fortune Snake 🐍": {"bet_min": 0.30, "bet_max": 400.0},
    "Fortune Mouse 🐹": {"bet_min": 0.50, "bet_max": 400.0},
    "Fortune Tiger 🐯": {"bet_min": 0.40, "bet_max": 5.0},
    "Gates of Olympus ⚡": {"bet_min": 0.20, "bet_max": 400.0},
    "Fortune Dragon 🐉": {"bet_min": 0.40, "bet_max": 400.0},
    "Fortune Gems 💎": {"bet_min": 0.40, "bet_max": 400.0},
    "Fortune OX 🐂": {"bet_min": 0.50, "bet_max": 400.0},
    "Double Fortune 🎎": {"bet_min": 0.30, "bet_max": 400.0},
    "Jackpot Joker 🎰🃏": {"bet_min": 0.20, "bet_max": 400.0},
    "Fortune Gems 2 💎": {"bet_min": 0.40, "bet_max": 400.0},
    "Fortune Gems 3 💎": {"bet_min": 0.40, "bet_max": 400.0},
    "PartyStar 🐇": {"bet_min": 0.40, "bet_max": 400.0},
    "Big Bass Splash 🎣": {"bet_min": 0.10, "bet_max": 400.0},
    "Cash Mania": {"bet_min": 0.50, "bet_max": 400.0},
    "Wild Bandito 💀": {"bet_min": 0.40, "bet_max": 400.0},
    "Master Joker 🃏": {"bet_min": 0.40, "bet_max": 400.0},
    "Big Bass Hold & Spinner 🎣": {"bet_min": 0.10, "bet_max": 400.0},
    "Lucky Neko 😺": {"bet_min": 0.50, "bet_max": 400.0},
    "Aztec Gems Deluxe 🍃": {"bet_min": 0.40, "bet_max": 400.0},
    "Rio Fantasia 🐦‍🔥": {"bet_min": 0.50, "bet_max": 400.0},
    "DevilFire 2 🔱": {"bet_min": 0.40, "bet_max": 400.0},
    "Lucky Piggy 🐷": {"bet_min": 0.40, "bet_max": 400.0},
    "Super Market Spree 🛒": {"bet_min": 0.40, "bet_max": 400.0},
    "Fortune Pig 🐷": {"bet_min": 0.40, "bet_max": 400.0},
    "Wings Of !Guazu 🍀": {"bet_min": 0.40, "bet_max": 400.0},
    "Piggy Gold 🐷": {"bet_min": 0.40, "bet_max": 400.0},
}

# Link de afiliação
LINK_AFILIACAO = "https://9353jogo.site/?pid=29056940"

# Lista de vídeos como provas sociais
VIDEOS_PROVAS = [
    "https://t.me/SILVERCOPMTD/473",
    "https://t.me/SILVERCOPMTD/226",
    "https://t.me/SILVERCOPMTD/28",
    "https://t.me/SILVERCOPMTD/20",
    "https://t.me/SILVERCOPMTD/17",
    "https://t.me/SILVERCOPMTD/16",
    "https://t.me/SILVERCOPMTD/15",
    "https://t.me/SILVERCOPMTD/122",
    "https://t.me/SILVERCOPMTD/121",
    "https://t.me/SILVERCOPMTD/124",
    "https://t.me/SILVERCOPMTD/125",
    "https://t.me/SILVERCOPMTD/132",
    "https://t.me/SILVERCOPMTD/224",
    "https://t.me/SILVERCOPMTD/4773",
    "https://t.me/SILVERCOPMTD/6940",
    "https://t.me/SILVERCOPMTD/6960",
    "https://t.me/SILVERCOPMTD/6964",
    "https://t.me/SILVERCOPMTD/6968",
    "https://t.me/SILVERCOPMTD/6972",
    "https://t.me/SILVERCOPMTD/6983",
    "https://t.me/SILVERCOPMTD/10832",
    "https://t.me/SILVERCOPMTD/10833",
    "https://t.me/SILVERCOPMTD/10834",
    "https://t.me/SILVERCOPMTD/10835",
    "https://t.me/SILVERCOPMTD/10836",
]

# Inicialização do bot
app_bot = Client("bot_sinais",
                 api_id=API_ID,
                 api_hash=API_HASH,
                 bot_token=BOT_TOKEN)

def calcular_bet(deposito):
    if deposito >= 50:
        return 5.00
    elif deposito >= 30:
        return 2.00
    elif deposito >= 20:
        return 1.00
    elif deposito >= 10:
        return 0.40
    else:
        return 0.20

def gerar_mensagem(jogo, deposito, aposta):
    now = datetime.now()
    horario_sinal = now + timedelta(minutes=3)
    horario_formatado = horario_sinal.strftime("%H:%M")
    estrategia = "🔹 Automático 10x, Turbo ligado"
    nova_opcao = random.choice(list(jogos.keys()))
    imagem_jogo = IMAGENS_JOGOS.get(jogo, None)

    mensagem = f"""
📢 **Oportunidade de Lucro - Slots** 📢

⏰ **Hora Certa para Apostar!** Jogue **{jogo}**
🗓 **Horário recomendado**: {horario_formatado}
💰 **Depósito**: R${deposito}
🎯 **Aposta sugerida**: R${aposta}
📝 **Estratégia**: {estrategia}

💡 **Dica de Profissional**: Se os 10 giros forem positivos, aumente aos poucos. Caso não lucre, tente outro jogo como {nova_opcao}.

🔗 Clique abaixo para jogar:
"""

    botoes = InlineKeyboardMarkup([
        [InlineKeyboardButton("🍀 JOGUE AGORA  🎰", url=LINK_AFILIACAO)]
    ])

    return mensagem, imagem_jogo, botoes

# Função para envio de sinais (exemplo)
async def enviar_sinal():
    jogo = random.choice(list(jogos.keys()))
    deposito = random.choice([10, 20, 30, 50])
    aposta = calcular_bet(deposito)
    mensagem, imagem, botoes = gerar_mensagem(jogo, deposito, aposta)

    if imagem and os.path.exists(imagem):
        await app_bot.send_photo(CHANNEL_ID, photo=imagem, caption=mensagem, reply_markup=botoes, parse_mode="markdown")
    else:
        await app_bot.send_message(CHANNEL_ID, text=mensagem, reply_markup=botoes, parse_mode="markdown")

# Execução contínua do bot
async def main():
    await app_bot.start()
    while True:
        await enviar_sinal()
        await asyncio.sleep(420)  # espera 7 minutos (420 segundos)

if __name__ == "__main__":
    asyncio.run(main())
