import os
from typing import Optional
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

async def generate_content(prompt: str) -> str:
    """Generate content using Groq's LLM API."""
    try:
        system_prompt = """Bạn là một người viết content chuyên nghiệp.
        Hãy tạo ra nội dung chất lượng cao, dễ đọc và hấp dẫn bằng tiếng Việt.
        Đảm bảo nội dung mạch lạc, có cấu trúc rõ ràng và phù hợp với văn hóa Việt Nam.
        Hãy chia nội dung thành các đoạn ngắn, mỗi đoạn không quá 1500 ký tự."""
        
        completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            model="mistral-saba-24b",
            temperature=0.7,
            max_tokens=1500,
            top_p=0.9,
        )
        
        return completion.choices[0].message.content
        
    except Exception as e:
        raise Exception(f"Error generating content with Groq: {str(e)}") 