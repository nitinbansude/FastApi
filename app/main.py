import uvicorn
from app.views import app


if __name__ == '__main__':
    print("--------- Starting Server ---------")
    uvicorn.run(app, host='0.0.0.0', port = 8000, reload= True)
