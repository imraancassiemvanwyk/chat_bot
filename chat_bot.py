from llama import init_llama_model, generate_response
from google_api import authenticate_google, send_email
from database import init_db, add_reminder, get_reminders
from scheduler import start_scheduler
from weather import get_weather
from news import  get_news
from utility import detect_intent


import threading


def chatbot_main():
    tokenizer, model = init_llama_model()
    creds = authenticate_google()
    init_db()

    # Start the scheduler in a background thread
    scheduler_thread = threading.Thread(target=start_scheduler, daemon=True)
    scheduler_thread.start()

    print("Welcome to your Personal Assistant Chatbot!")
    while True:
        user_input = input("You: ")
        intent = detect_intent(user_input)

        if intent == "email":
            recipient = input("Enter recipient email: ")
            subject = input("Enter subject: ")
            body = input("Enter email body: ")
            send_email(creds, recipient, subject, body)
            print("Email sent successfully!")

        elif intent == "reminder":
            print("What's the reminder about?")
            title = input("You: ")
            print(f"When should I remind you about '{title}'? (YYYY-MM-DD HH:MM)")
            datetime = input("You: ")
            add_reminder(title, datetime)
            print(f"Got it! I'll remind you about '{title}' on {datetime}.")

        elif intent == "weather":
            city = input("Enter your city: ")
            print(get_weather(city))

        elif intent == "news":
            print(get_news())

        elif intent == "quit":
            print("Goodbye!")
            break

        else:
            prompt = f"The user said: {user_input}. Respond appropriately."
            response = generate_response(tokenizer, model, prompt)
            print(f"Assistant: {response}")


if __name__ == "__main__":
    chatbot_main()
