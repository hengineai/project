import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def generate_sentiment_graph(token_name: str = "ZAP"):
    times = pd.date_range(end=pd.Timestamp.now(), periods=48, freq='30T')
    twitter = np.random.rand(48) * 100
    telegram = np.random.rand(48) * 80
    discord = np.random.rand(48) * 60
    combined = (twitter + telegram + discord) / 3 + np.random.normal(0, 5, 48)

    plt.figure(figsize=(12, 6))
    plt.plot(times, twitter, label="Twitter")
    plt.plot(times, telegram, label="Telegram")
    plt.plot(times, discord, label="Discord")
    plt.fill_between(times, combined, alpha=0.3, label="On-chain Overlay")
    plt.title(f"Sentiment Spike Graph for ${token_name}")
    plt.xlabel("Time")
    plt.ylabel("Mentions / Score")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"sentiment_graph_{token_name}.png")