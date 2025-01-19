def detect_intent(user_input):
    if "email" in user_input.lower():
        return "email"
    elif "reminder" in user_input.lower():
        return "reminder"
    elif "weather" in user_input.lower():
        return "weather"
    elif "news" in user_input.lower():
        return "news"
    elif "quit" in user_input.lower():
        return "quit"
    else:
        return "chat"