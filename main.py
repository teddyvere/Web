from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    
# try to convert the sqlite database to mysql using sqlalchemy-migrate