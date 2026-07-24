from template import count_tokens

text2 = (
    "Trí tuệ nhân tạo (AI) đang tạo ra một cuộc cách mạng trong hầu hết các lĩnh vực "
    "của đời sống con người, từ y tế, giáo dục cho đến giao thông vận tải và giải trí. "
    "Tuy nhiên, sự phát triển bùng nổ của các mô hình ngôn ngữ lớn (LLMs) như GPT-4 "
    "cũng dấy lên nhiều lo ngại về quyền riêng tư, an ninh mạng và đạo đức. "
    "Việc các hệ thống này có thể tạo ra văn bản, mã lập trình, hoặc hình ảnh "
    "giống hệt như con người làm mờ đi ranh giới giữa thực và ảo. Nhiều chuyên gia "
    "cảnh báo rằng nếu không có những khuôn khổ pháp lý và quy định chặt chẽ, "
    "AI có thể bị lạm dụng để lan truyền tin giả, thao túng dư luận hoặc gây ra "
    "những tác động tiêu cực không lường trước được đối với xã hội. Do đó, "
    "trách nhiệm của các nhà phát triển và các nhà hoạch định chính sách là phải "
    "hợp tác để xây dựng một tương lai nơi AI phục vụ lợi ích chung của nhân loại."
)

word_count = len(text2.split())
rough_estimate = word_count / 0.75
actual_tokens = count_tokens(text2)

print(f"Words: {word_count}")
print(f"Rough Estimate (words/0.75): {rough_estimate:.2f}")
print(f"Actual Tokens: {actual_tokens}")
print(f"Ratio (Tokens/Word): {actual_tokens / word_count:.2f}")
