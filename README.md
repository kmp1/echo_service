# echo_service

This service copies the Google Translate REST API and simply returns what it has been asked to translate prefixed with some information about what it has been translated to and from, for example:

    http://0.0.0.0:5000/language/translate/v2?key=YOUR_API_KEY&q=hello%20world&source=en&target=de

    {
      "data": {
        "translations": [
          {
            "translatedText": "\"[from en to de] hello world\""
          }
        ]
      }
    }

It is implemented in Python using Flask and has the various gubbins needed for easy deployment to Heroku.  For example:
   
    git clone https://github.com/kmp1/echo_service.git
    
    cd echo_service
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

    heroku login
    heroku create
    git push heroku master

To test it out locally, replace the last command with:

    heroku local
