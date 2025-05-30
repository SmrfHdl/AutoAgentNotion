# AutoAgent Notion

Hệ thống tự động tạo nội dung và lưu vào Notion sử dụng AI.

## Tính năng

- Tạo nội dung tự động sử dụng Groq API
- Tự động lưu nội dung vào Notion
- Giao diện web đơn giản với Streamlit
- API endpoints cho tích hợp
- SQLite database để lưu lịch sử

## Cài đặt

1. Clone repository và tạo môi trường ảo:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

2. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

3. Tạo file `.env` với các thông tin cần thiết:
```
GROQ_API_KEY=gsk_your_groq_api_key    # Từ https://console.groq.com
NOTION_API_KEY=secret_your_notion_key  # Từ https://www.notion.so/my-integrations
NOTION_DATABASE_ID=your_database_id    # ID của Notion database
DATABASE_URL=sqlite:///./app.db        # SQLite connection string
```

4. Khởi tạo database:
```bash
python -m app.database.init_db
```

## Chạy ứng dụng

1. Chạy FastAPI backend (mở terminal mới):
```bash
uvicorn app.main:app --reload
```

2. Chạy Streamlit frontend (mở terminal mới):
```bash
streamlit run app/frontend/streamlit_app.py
```

3. Truy cập ứng dụng tại `http://localhost:8501`

## API Endpoints

- `POST /generate`: Tạo nội dung và lưu vào Notion
  - Request body:
    ```json
    {
        "prompt": "Nội dung cần tạo",
        "title": "Tiêu đề (tùy chọn)"
    }
    ```

- `GET /history`: Xem lịch sử các nội dung đã tạo

## Cấu hình Notion

1. Tạo Notion Integration:
   - Truy cập https://www.notion.so/my-integrations
   - Click "New integration"
   - Đặt tên và chọn workspace
   - Lưu Integration Token

2. Tạo Notion Database:
   - Tạo database mới trong workspace
   - Thêm column "Name" kiểu Title
   - Share database với integration (click "..." -> "Add connections")
   - Copy Database ID từ URL (phần giữa workspace và ?)
  
## Demo 

https://github.com/user-attachments/assets/3197a226-c1bf-44ae-9893-61c64696e8a3

## Deployment

Có thể deploy lên các nền tảng:

1. Vercel: Deploy FastAPI backend
2. Streamlit Cloud: Deploy frontend
3. Railway/Render: Deploy cả hệ thống

## Lưu ý

- Groq có free tier với giới hạn hợp lý
- Notion API có giới hạn về độ dài nội dung (2000 ký tự/block)
- Kiểm tra rate limits của các API được sử dụng 
