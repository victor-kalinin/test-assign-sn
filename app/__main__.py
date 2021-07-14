from uvicorn import run

if __name__ == '__main__':
    run("app.main:app", port=3000, reload=True)
