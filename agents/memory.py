chat_history = []

def save_chat(user, bot):
    chat_history.append({
        "user": user,
        "bot": bot
    })

def get_history():
    return chat_history
