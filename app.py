from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)
class ENGSM:
    ISO_639_1 = 'en_core_web_sm'
english_bot = ChatBot("Chatterbot", 
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    tagger_language = ENGSM)
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "Never gonna give you up",
    "Never gonna let you down"
]
trainer = ListTrainer(english_bot)
trainer.train(conversation)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
