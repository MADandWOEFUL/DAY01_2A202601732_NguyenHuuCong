# K4 — Ngày 1: Bài Tập & Phản Ánh
## Khám Phá LLM API | Phiếu Thực Hành

**Thời lượng:** 14h00–18h00
**Cách làm:** Trả lời từng câu ngay sau khi hoàn thành block tương ứng —
đừng để dồn hết về cuối buổi. Thay dòng `*Câu trả lời của bạn*` bằng câu
trả lời thật (chấm tự động sẽ đếm số câu đã trả lời).

---

## Block 1 — API Cơ Bản (trả lời sau Checkpoint 1)

### Câu 1.1 — Độ nhạy của temperature
Gọi `call_openai` với temperature 0.0, 0.7, 1.2 và 1.8 dùng prompt
**"Hãy kể cho tôi một sự thật thú vị về Hà Nội."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi? Ở mức nào phản hồi bắt đầu
kém mạch lạc?** (2–3 câu)
> *Với câu hỏi về sự thật lịch sử Hà Nội, em nhận thấy ở temperature 0.0, phản hồi mang tính chuẩn mực và luôn lặp lại. Ở 0.7, văn phong mềm mại và tự nhiên hơn. Đáng ngạc nhiên là khi tăng lên 1.2 và thậm chí 1.8, văn bản trở nên đa dạng, cách dùng từ có phần lạ hơn nhưng vẫn giữ được độ mạch lạc khá tốt và không bị "ảo giác" (hallucination) nghiêm trọng. Điều này cho thấy các model mạnh hiện nay (gpt-4o) có khả năng chống sụp đổ ngôn ngữ và kiểm soát sự thật rất tốt ngay cả ở nhiệt độ cực cao, khác hẳn với các thế hệ model cũ.*

### Câu 1.2 — Chọn temperature cho sản phẩm
**Bạn sẽ đặt temperature bao nhiêu cho trợ lý soạn thảo hợp đồng pháp lý,
và bao nhiêu cho trợ lý viết slogan quảng cáo? Giải thích khác biệt.**
> *Đối với trợ lý soạn thảo hợp đồng pháp lý, em sẽ đặt temperature ở mức rất thấp (khoảng 0.0 đến 0.2). Lý do là vì văn bản pháp luật đòi hỏi sự chính xác tuyệt đối, ngôn từ chặt chẽ, nhất quán và không được phép có rủi ro bịa đặt (ảo giác). Ngược lại, đối với trợ lý viết slogan quảng cáo, em sẽ đặt temperature cao hơn (khoảng 0.7 đến 0.9). Công việc này cần sự phá cách, ý tưởng đa dạng, không đụng hàng và ngôn từ bay bổng để thu hút khách hàng, nên việc cho phép AI sáng tạo là rất cần thiết.*

### Câu 1.3 — Đánh đổi chi phí
Kịch bản: 20.000 người dùng hoạt động mỗi ngày, mỗi người gọi API 2 lần,
mỗi lần trung bình ~500 token đầu ra.

**Ước tính chi phí mỗi ngày của model lớn so với model nhỏ cho workload này
(dựa trên bảng giá trong template). Nêu một trường hợp model lớn xứng đáng
với chi phí và một trường hợp model nhỏ là lựa chọn đúng:**
> *Tổng số token đầu ra mỗi ngày là 20.000.000 token. Dựa vào bảng giá, chi phí sử dụng model lớn (gpt-4o) sẽ rơi vào khoảng 200 USD/ngày. Trong khi đó, dùng model nhỏ (gpt-4o-mini) chỉ tốn khoảng 12 USD/ngày (rẻ hơn gần 17 lần).*
> 
> *Model lớn sẽ xứng đáng với mức giá cao khi ứng dụng đòi hỏi khả năng tư duy logic cực phức tạp, ví dụ: phân tích dữ liệu tài chính chuyên sâu, lập trình phần mềm phức tạp, hoặc làm trợ lý y khoa. Ngược lại, model nhỏ là lựa chọn đúng đắn cho các ứng dụng có lượng truy cập khổng lồ nhưng chỉ làm các tác vụ đơn giản như: phân loại cảm xúc bình luận, tóm tắt tin tức ngắn, hoặc chatbot hỗ trợ khách hàng cơ bản.*

---

## Block 2 — System Prompt & Token (trả lời sau Checkpoint 2)

### Câu 2.1 — Sức mạnh của persona
Gọi `chat_with_system_prompt` hai lần với cùng câu hỏi
**"Giải thích máy học (machine learning) là gì?"** nhưng hai system prompt
khác nhau:
- "Bạn là một nhà thơ, trả lời mọi thứ bằng hình ảnh ví von, tránh thuật ngữ."
- "Bạn là kỹ sư phần mềm senior, trả lời chính xác, có ví dụ code khi phù hợp."

**Hai phản hồi khác nhau như thế nào (giọng văn, độ dài, mức kỹ thuật)?
Từ đó rút ra system prompt điều khiển được những khía cạnh nào của phản hồi?**
(3–4 câu)
> *Dựa trên kết quả chạy thử nghiệm thực tế:*
> *1. Trợ lý Nhà Thơ: Giải thích bằng hình ảnh ẩn dụ ("khu vườn kỳ diệu", "gieo trồng hạt giống thông tin", "tưới tắm thuật toán"). Văn phong bay bổng, hoàn toàn không có gạch đầu dòng hay thuật ngữ khô khan.*
> *2. Trợ lý Kỹ Sư: Định nghĩa trực tiếp ("nhánh của AI"), sử dụng cấu trúc rõ ràng với các gạch đầu dòng (Input Data, Features, Model) và từ ngữ chuyên ngành.*
> *Qua đó, có thể thấy System Prompt giống như một "bộ điều khiển" toàn năng, cho phép chúng ta chi phối trực tiếp: Giọng điệu (tone of voice), Định dạng văn bản (chữ, thơ, bullet points) và Tính cách (persona) của AI.*

### Câu 2.2 — tiktoken vs đếm từ
Chọn một đoạn văn tiếng Việt ~150 từ. So sánh số token theo `count_tokens`
(tiktoken) với ước lượng `số từ / 0.75` mà Part 1 đã dùng.

**Hai con số chênh nhau bao nhiêu phần trăm? Nếu dùng ước lượng thô để dự
toán ngân sách API cho ứng dụng tiếng Việt, bạn sẽ dự toán thiếu hay thừa —
và vì sao?**
> *Khi chạy thí nghiệm với một đoạn văn tiếng Việt dài 174 từ:*
> *- Ước lượng thô (số từ / 0.75): khoảng 232 token.*
> *- Thực tế (dùng tiktoken cho model gpt-4o): chỉ tốn 212 token.*
> *Mức chênh lệch là khoảng 8% (thực tế RẺ HƠN ước lượng). Đây là một phát hiện rất thú vị: Bộ tokenizer mới `o200k_base` của GPT-4o đã được tối ưu cực kỳ xuất sắc cho tiếng Việt (trung bình 1 từ tiếng Việt chỉ tốn khoảng 1.2 token). Do đó, nếu dùng công thức ước lượng thô (số từ / 0.75) cho các model đời mới như GPT-4o, bạn sẽ dự toán ngân sách HƠI THỪA một chút (rất an toàn), thay vì bị thiếu hụt nghiêm trọng như ở các model đời cũ (như GPT-3.5 thường tốn 2-3 token cho 1 từ tiếng Việt).*

---

## Block 3 — Streaming & Độ Bền (trả lời sau Checkpoint 3)

### Câu 3.1 — Trải nghiệm người dùng với streaming
**Xét ba ứng dụng: (a) chatbot văn bản, (b) trợ lý giọng nói đọc to phản hồi,
(c) pipeline dịch tài liệu chạy ngầm ban đêm. Ứng dụng nào hưởng lợi nhiều
nhất từ streaming, ứng dụng nào không cần — và tại sao?** (1 đoạn văn)
> *(a) Chatbot văn bản và (b) trợ lý giọng nói là 2 ứng dụng hưởng lợi nhiều nhất từ streaming. Lý do là hai ứng dụng này tương tác trực tiếp theo thời gian thực với con người; người dùng rất thiếu kiên nhẫn. Streaming giúp giảm "Thời gian chờ phản hồi đầu tiên" (Time to First Token) xuống gần như lập tức, tạo cảm giác hệ thống phản hồi cực nhanh.*
> *(c) Pipeline dịch tài liệu chạy ngầm ban đêm thì KHÔNG cần streaming. Nó là hệ thống xử lý hàng loạt (batch processing), chỉ cần nhận cục kết quả cuối cùng để lưu vào database chứ không có người dùng nào ngồi nhìn màn hình từng chữ chạy ra cả.*

### Câu 3.2 — Vì sao backoff theo cấp số nhân?
**Khi API quá tải và hàng nghìn client cùng retry, exponential backoff giúp
gì so với delay cố định? Tra cứu thêm: kỹ thuật "jitter" (thêm độ trễ ngẫu
nhiên) giải quyết vấn đề gì còn sót lại?**
> *Exponential backoff giúp các lượt retry được giãn cách rải rác theo thời gian (0.1s, 0.2s, 0.4s...) thay vì dồn dập vào cùng một lúc (delay cố định). Việc này làm giảm mạnh áp lực lên server đang bị quá tải, giúp nó có thời gian để phục hồi.*
> *Tuy nhiên, nếu 1000 client cùng bị lỗi ở đúng 1 giây, chúng sẽ cùng đếm giờ và retry lại vào đúng các mốc thời gian hệt nhau. Kỹ thuật "jitter" (cộng thêm một lượng thời gian nhiễu ngẫu nhiên nhỏ vào mỗi nhịp delay) giúp phá vỡ sự đồng bộ này, phân tán hoàn toàn các request ra xung quanh, giải quyết triệt để hiện tượng "thundering herd" (hiệu ứng bầy đàn).*

---

## Block 4 — Mini-Project (trả lời sau Checkpoint 4)

### Câu 4.1 — Thiết kế persona
**Viết lại system prompt bạn dùng cho trợ lý của mình. Chỉ ra 2 chỗ trong
prompt mà nếu xóa đi, hành vi trợ lý sẽ thay đổi rõ rệt — và mô tả thay đổi
đó:**
> *System prompt em đã dùng: "Bạn là trợ giảng thân thiện của khóa AI, trả lời ngắn gọn bằng tiếng Việt."*
> *1. Nếu xóa chữ "thân thiện": Hành vi của trợ lý sẽ trở nên khô khan, cộc lốc hoặc giống như rô bốt hỏi gì đáp nấy, thiếu đi sự tương tác xã giao.*
> *2. Nếu xóa chữ "ngắn gọn": Trợ lý có thể sẽ bị bệnh "trình bày", lôi cả những kiến thức ngoài lề dài dòng lê thê vào để giải thích cho một câu hỏi vốn dĩ rất đơn giản, gây loãng thông tin.*

### Câu 4.2 — Hạn chế & cải thiện
**Trợ lý của bạn giữ history 4 lượt cuối. Hãy mô tả một tình huống hội thoại
cụ thể mà giới hạn này khiến trợ lý trả lời sai/mất ngữ cảnh, và đề xuất một
cách khắc phục (ví dụ: tóm tắt các lượt cũ, tăng giới hạn có chọn lọc...):**
> *Tình huống: Người dùng nói "Tên tôi là An" ở Lượt 1. Sau đó họ tiếp tục thảo luận về bóng đá, thời tiết, lập trình... trong 5 lượt tiếp theo. Đến Lượt 7, họ đột nhiên hỏi "Tôi tên gì?". Trợ lý sẽ không thể trả lời vì bộ nhớ (history) đã chặt bỏ Lượt 1 để giữ giới hạn 4 lượt gần nhất.*
> *Đề xuất khắc phục: Sử dụng cơ chế "Tóm tắt bộ nhớ" (Memory Summarization). Mỗi khi history sắp bị tràn, ta gọi một mô hình nhỏ (vd: gpt-4o-mini) chạy ngầm để tóm tắt các ý chính của các lượt cũ (vd: "Người dùng tên An") và nhét phần tóm tắt này vào một phần đặc biệt của System Prompt. Nhờ vậy, AI vẫn giữ được các thông tin cốt lõi xuyên suốt mà không làm phình to số token.*

---

## Danh Sách Kiểm Tra Nộp Bài

- [ ] `python grade.py` — xem điểm tự động, mục tiêu ≥ 75/100
- [ ] Cả 4 checkpoint pytest đều pass
- [ ] Tất cả 9 câu trong file này đã được trả lời
- [ ] Đã copy bài làm vào folder `solution/`, push lên GitHub cá nhân và nộp link repo vào vlearn (theo hướng dẫn README)
