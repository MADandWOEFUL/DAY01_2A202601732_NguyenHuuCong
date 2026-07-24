from dotenv import load_dotenv
load_dotenv(override=True)
import os
os.environ["LAB_MODEL"] = "gpt-4o-mini"
import template
template.OPENAI_MODEL = "gpt-4o-mini"
from template import chat_with_system_prompt, run_assistant

print("=== THÍ NGHIỆM 4.1: CHỈNH SỬA SYSTEM PROMPT ===")
prompt_full = "Bạn là trợ giảng thân thiện của khóa AI, trả lời ngắn gọn bằng tiếng Việt."
prompt_no_friendly = "Bạn là trợ giảng của khóa AI, trả lời ngắn gọn bằng tiếng Việt."
prompt_no_short = "Bạn là trợ giảng thân thiện của khóa AI, trả lời bằng tiếng Việt."

user_q = "Machine learning là gì?"

print("\n1. BẢN GỐC (Thân thiện + Ngắn gọn):")
print(chat_with_system_prompt(prompt_full, user_q)[0])

print("\n2. BỎ CHỮ 'THÂN THIỆN':")
print(chat_with_system_prompt(prompt_no_friendly, user_q)[0])

print("\n3. BỎ CHỮ 'NGẮN GỌN':")
print(chat_with_system_prompt(prompt_no_short, user_q)[0])


print("\n\n=== THÍ NGHIỆM 4.2: TRÀN BỘ NHỚ (HISTORY) ===")
inputs = [
    "Xin chào, tên tôi là An. Rất vui được gặp bạn!",
    "Bóng đá là môn thể thao tôi thích nhất.",
    "Hôm nay thời tiết ở Hà Nội có vẻ nóng.",
    "Bạn nghĩ Python có khó học không?",
    "Tôi vừa ăn một bát phở bò rất ngon.",
    "Bạn nghĩ AI có thay thế lập trình viên không?",
    "À quên mất, nãy giờ nói chuyện, bạn còn nhớ tôi tên gì không?"
]

input_idx = 0
def mock_input():
    global input_idx
    if input_idx < len(inputs):
        msg = inputs[input_idx]
        print(f"\n[Người dùng]: {msg}")
        input_idx += 1
        return msg
    return "quit"

# Chạy trợ lý với mock_input để tự động gõ tin nhắn
run_assistant(persona=prompt_full, get_input=mock_input)
