# chatbot
# 🤖 CryptoBuddy – Your Green Crypto Assistant 🌱

CryptoBuddy is a simple command-line chatbot that helps users discover cryptocurrencies with rising trends and strong sustainability profiles. Whether you're eco-conscious or just curious about what's trending, CryptoBuddy has your back!

---

## 🌟 Features

- 🔍 Recommends trending (rising) cryptocurrencies
- 🌿 Highlights the most sustainable crypto options
- 📈 Suggests long-term growth candidates
- 💬 Friendly and interactive chatbot interface
- ♻️ Promotes eco-conscious investing

---

## 🧠 How It Works

CryptoBuddy uses a small in-memory database of select cryptocurrencies (`Bitcoin`, `Ethereum`, `Cardano`) with attributes like:

- `price_trend`: Is the coin currently rising, stable, or not?
- `market_cap`: Relative size of the cryptocurrency
- `energy_use`: High, medium, or low energy consumption
- `sustainability_score`: A rating out of 10 for environmental sustainability

The bot responds to user queries by analyzing this data and providing helpful, eco-friendly advice.

---

## 🖥️ Getting Started

### Prerequisites

- Python 3.x

### Run the Bot

```bash
python cryptobuddy.py
