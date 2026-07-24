from dotenv import load_dotenv
load_dotenv(override=True)
from template import chat_with_system_prompt, count_tokens

with open("experiment_results.md", "w", encoding="utf-8") as f:
    f.write("# KẾT QUẢ THÍ NGHIỆM\n\n")

    # Thí nghiệm 2.1
    f.write("## Thí nghiệm 2.1 - System Prompt\n")
    user_prompt = "Giải thích máy học (machine learning) là gì?"
    system_poet = "Bạn là một nhà thơ, trả lời mọi thứ bằng hình ảnh ví von, tránh thuật ngữ."
    system_eng = "Bạn là kỹ sư phần mềm senior, trả lời chính xác, có ví dụ code khi phù hợp."
    
    try:
        ans_poet, _ = chat_with_system_prompt(system_poet, user_prompt)
        f.write("### Trợ lý Nhà Thơ\n")
        f.write(ans_poet + "\n\n")
        
        ans_eng, _ = chat_with_system_prompt(system_eng, user_prompt)
        f.write("### Trợ lý Kỹ Sư\n")
        f.write(ans_eng + "\n\n")
    except Exception as e:
        f.write(f"Lỗi: {e}\n\n")

    # Thí nghiệm 2.2
    f.write("## Thí nghiệm 2.2 - Tiktoken vs Đếm từ\n")
    text_vn = (
        "Hà Nội là thủ đô, đồng thời là thành phố đứng đầu Việt Nam về diện tích tự nhiên "
        "và đứng thứ hai về quy mô dân số với 8,5 triệu người, sau Thành phố Hồ Chí Minh. "
        "Nằm giữa đồng bằng sông Hồng trù phú, nơi đây đã sớm trở thành một trung tâm chính "
        "trị, kinh tế và văn hóa ngay từ những buổi đầu của lịch sử Việt Nam. "
        "Với vai trò thủ đô, Hà Nội là nơi tập trung nhiều viện nghiên cứu, trường đại học, "
        "bệnh viện hàng đầu, cũng như các trung tâm văn hóa, giải trí lớn nhất cả nước. "
        "Tuy nhiên, sự phát triển kinh tế nhanh chóng cũng đem lại cho thành phố nhiều "
        "thách thức về giao thông, ô nhiễm môi trường, quy hoạch đô thị. Hà Nội ngày nay "
        "không chỉ nỗ lực hiện đại hóa mà còn cố gắng bảo tồn những di sản văn hóa truyền thống, "
        "những khu phố cổ rêu phong và những làng nghề hàng trăm năm tuổi."
    )
    word_count = len(text_vn.split())
    rough_estimate = word_count / 0.75
    try:
        actual_tokens = count_tokens(text_vn)
        f.write(f"Đoạn văn mẫu (tiếng Việt) có {word_count} từ.\n")
        f.write(f"Số token ước lượng (từ / 0.75): {rough_estimate:.2f}\n")
        f.write(f"Số token thực tế (tiktoken gpt-4o): {actual_tokens}\n")
        diff_percent = ((actual_tokens - rough_estimate) / rough_estimate) * 100
        f.write(f"Chênh lệch phần trăm: {diff_percent:.2f}%\n\n")
    except Exception as e:
        f.write(f"Lỗi: {e}\n\n")

print("Hoàn thành thí nghiệm, đã ghi vào experiment_results.md")
