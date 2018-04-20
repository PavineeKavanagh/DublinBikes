from app import app

# Run application from terminal using 'flask run'
def main():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
