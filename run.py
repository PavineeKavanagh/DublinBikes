from app import app

# Run application from terminal using 'flask run'
def main():
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
