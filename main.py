import uvicorn
from src.routes.routes import app
from pathlib import Path

# if __name__ == '__main__':
#     #f"{Path(__file__).stem}
#     uvicorn.run("main:app",
#                 host="127.0.0.1",
#                 port=9000,
#                 log_level='info',
#                 reload=True
#                 )
