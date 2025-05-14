from fastapi import FastAPI
import random

app = FastAPI()

side_hustle = [
    "Freelancing - Start offering your skills online",
    "Dropshipping - Sell without handling inventory",
    "Stock Market - Invest and watch your money grow!",
    "Affiliate Marketing - Earn by promoting products!",
    "Crypto Trading - Buy and Sell digital assets!",
    "Online Course - Share your knowledge and earn!",
    "Print-on-Demand - Sell custom design products!",
    "Blogging - Create content and earn through ads and sponsorships!",
    "YouTube Channel - Monetize videos through ads and sponsorships!",
    "Social Media Management - Manage accounts for brands and influencers!"
    "App Development - Create mobile or web application for businesses!"
]

money_quotes = [
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Formal education will make you a living; self-education will make you a fortune.",
    "If you do not find a way to make money while you sleep, you will work until you die.",
    "Money is a terrible master but an excellent servant. - P.T Barnum",
    "You must gain contro; over your money or the lack of it will forever control you.",
    "Opportunities don't happen. You create them. - Chris Grosser",
    "Don't stay in bed unless you can make money in bed. - George Burns",
    "Money often cost too much. - Ralph Waldo Emerson",
    "Never depend on a single income. Make an investment to create a second sourse.",
    "It's not about having lots of money. It is about knowing how to manage it. - Anonymous",
    "Rich people have small TVs and big libraries, and poor people have small libraries and big TVs.",
    "A wise person should have money in their head, but not in their hearts. - Jonathan Swift",
    "Money grows on the tree of persistence. - Japanese Proverb"
]

@app.get("/side_hustles")
def get_side_hustle(apikey: str):
    """Returns a random side hustle idea"""
    if apikey !="1234567890":
        return{"error": "Invalid API key"}
    return {"side_hustle": random.choice(side_hustle)}


@app.get("/money_quotes")
def get_money_quotes(apikey:str):
    """Returns a random money quote"""
    if apikey != "123456789":
        return{"error":"Invalid API key"}
    return {"money_quote": random.choice(money_quotes)}