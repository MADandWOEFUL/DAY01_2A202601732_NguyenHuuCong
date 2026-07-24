from dotenv import load_dotenv
load_dotenv(override=True)
import sys
from template import call_openai

prompt = "Hãy kể cho tôi một sự thật thú vị về Hà Nội."
for temp in [0.0, 0.7, 1.2, 1.8]:
    print(f'\n========== Temperature: {temp} ==========')
    try:
        _mini_answer, _ = call_openai(prompt, temperature=temp, max_tokens=200, model="gpt-4o-mini")
        _answer, __ = call_openai(prompt, temperature=temp, max_tokens=200, model="gpt-4o")
        ans = f"Mini: {_mini_answer}\n\nFull: {_answer}"
        print(ans)
    except Exception as e:
        print(f"Error: {e}")
