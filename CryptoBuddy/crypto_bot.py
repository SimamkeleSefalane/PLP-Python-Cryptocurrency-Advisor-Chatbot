#Predefined Crypto Data

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}


#Chatbot Logic

def chatbot():
    print("👋 Hey! I'm CryptoBuddy – your AI-powered crypto sidekick! 💰")
    print("Ask me about trending coins, sustainable investments, or long-term growth advice.")
    print("Type 'exit' to quit.\n")
    
    while True:
        user_query = input("You: ").lower()
        
        if "exit" in user_query:
            print("CryptoBuddy: 🚪 Exiting... Remember, crypto is risky—always DYOR (Do Your Own Research)!")
            break

        elif "sustainable" in user_query or "eco" in user_query:
            recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
            print(f"CryptoBuddy: 🌱 Invest in {recommend}! It's eco-friendly and has long-term potential!")

        elif "trending" in user_query or "rising" in user_query:
            trending_coins = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
            print(f"CryptoBuddy: 📈 These cryptos are on the rise: {', '.join(trending_coins)}")

        elif "long-term" in user_query or "growth" in user_query:
            candidates = []
            for coin, data in crypto_db.items():
                if data["price_trend"] == "rising" and data["sustainability_score"] >= 7:
                    candidates.append(coin)
            if candidates:
                print(f"CryptoBuddy: 🚀 {candidates[0]} is trending up and has a top-tier sustainability score!")
            else:
                print("CryptoBuddy: 🤔 I can't find a perfect match for long-term and sustainable growth.")

        elif "best" in user_query or "recommend" in user_query:
            coin = "Cardano"
            print(f"CryptoBuddy: 💡 Based on current trends, I recommend {coin} – it's rising and eco-friendly!")

        else:
            print("CryptoBuddy: 🤖 Hmm... I didn’t catch that. Try asking about trending, sustainable, or long-term crypto!")

if __name__ == "__main__":
    chatbot()
