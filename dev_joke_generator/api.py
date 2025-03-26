from fastapi import FastAPI
import random

app = FastAPI()

# Jokes categorized         
jokes = {
    "frontend": [
        {"setup": "Why did the React developer break up with Vue?", "punchline": "Because Vue was too reactive!"},
        {"setup": "Why do frontend developers love tea?", "punchline": "Because they hate CoffeeScript!"},
        {"setup": "Why do frontend developers prefer CSS?", "punchline": "Because they like things to be well-styled!"},
    ],
    "backend": [
        {"setup": "Why do backend developers make bad DJs?", "punchline": "Because they always keep things in the background!"},
        {"setup": "Why do backend devs love REST APIs?", "punchline": "Because they always need a break!"},
        {"setup": "Why was the SQL query sad?", "punchline": "It had too many joins but still felt lonely!"},
    ],
    "javascript": [
        {"setup": "Why did the JavaScript developer go broke?", "punchline": "Because he kept using `null` as his value!"},
        {"setup": "Why do JS devs never trust numbers?", "punchline": "Because `0 == false`, but `0 !== false`!"},
        {"setup": "How do JavaScript devs like their burgers?", "punchline": "With extra `this`!"},
    ],
    "python": [
        {"setup": "Why did the Python developer bring a ladder to work?", "punchline": "Because he wanted to reach the high-level syntax!"},
        {"setup": "What’s a Python developer’s favorite type of music?", "punchline": "Loops and Conditions!"},
        {"setup": "Why did the Python developer get promoted?", "punchline": "Because he handled exceptions like a pro!"},
    ],
    "pakistani_dev": [
        {"setup": "Why do Pakistani developers always bring chai to meetings?", "punchline": "Because caffeine is their only debugger! ☕"},
        {"setup": "What happens when a Pakistani developer pushes code on Friday?", "punchline": "Monday becomes a disaster recovery drill!"},
        {"setup": "Why don’t Pakistani devs use Stack Overflow at work?", "punchline": "Because they already overflow with bugs! 🐛"},
    ]
}

# API route to get a random joke
@app.get("/random_joke")
def get_joke(category: str = "general"):
    if category in jokes:
        return random.choice(jokes[category])
    else:
        all_jokes = sum(jokes.values(), [])  # Flatten list
        return random.choice(all_jokes)

# Server run karne ka method
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
