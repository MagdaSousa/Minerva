import uvicorn
from src.routes.routes import app, obj_connection
if __name__ == "__main__":
    config = uvicorn.Config("main:app",
                            host="127.0.0.1",
                            port=9000,
                            log_level='info',
                            reload=True
                            )
    server = uvicorn.Server(config)
    server.run()
