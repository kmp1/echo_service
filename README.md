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
    
    cd echo_service/
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

If you want to deploy to Heroku, this should do the trick:

    heroku login
    heroku create
    git push heroku master

To test it out locally before pusing do this:

    heroku local

You can also run it without Heroku by just doing:

    python application.py

Finally, I have already deployed it here that you can have a look at too:

    https://translate-echo-service.herokuapp.com

Doing this would provide you with a translation:

    https://translate-echo-service.herokuapp.com/language/translate/v2?key=YOUR_API_KEY&q=hello world&source=en&target=de
