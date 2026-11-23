from database.db import create_table, save_data


def get_ai_tools():

    tools = [
        {
            "name": "ChatGPT",
            "category": "AI Assistant",
            "url": "https://chatgpt.com"
        },
        {
            "name": "Claude",
            "category": "AI Assistant",
            "url": "https://claude.ai"
        },
        {
            "name": "Gemini",
            "category": "AI Assistant",
            "url": "https://gemini.google.com"
        },
        {
            "name": "Perplexity",
            "category": "AI Search",
            "url": "https://www.perplexity.ai"
        },
        {
            "name": "Canva",
            "category": "AI Design",
            "url": "https://www.canva.com"
        },
        {
            "name": "GitHub Copilot",
            "category": "AI Coding",
            "url": "https://github.com/features/copilot"
        }
    ]

    return tools


if __name__ == "__main__":

    create_table()

    results = get_ai_tools()

    save_data("tools", results)

    print("AI tools saved successfully!")