# Step 1: Define the crypto database
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

# Step 2: Define chatbot personality
def greet_user():
    print("CryptoBuddy 🤖: Hey there! Let’s find you a green and growing crypto! 🌱")

# Step 3: Define logic for user queries
def respond_to_query(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"CryptoBuddy 🤖: Invest in {recommend}! 🌿 It’s eco-friendly and has long-term potential!")

    elif "trending" in user_query or "rising" in user_query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        print(f"CryptoBuddy 🤖: These coins are trending up: {', '.join(trending)} 🚀")

    elif "long-term" in user_query or "growth" in user_query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                print(f"CryptoBuddy 🤖: {coin} is a solid pick for long-term growth! 📈")
                return
        print("CryptoBuddy 🤖: Hmm, nothing fits that perfectly right now. Want to try a different strategy?")

    else:
        print("CryptoBuddy 🤖: I didn’t quite get that. Try asking about trends or sustainability! 💡")

# Step 4: Run chatbot loop
greet_user()
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("CryptoBuddy 🤖: Catch you later! Stay green and savvy! 🌍")
        break
    respond_to_query(user_input)