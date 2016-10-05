# Let's Go
The repo for the 2016-17 Congressional App Challenge team, Duncan Grubbs, Sebastian Boyd, Ryan McNeil, and Luke Martel.

## How to Use _with API_
- Open Terminal and navigate to the repo/client  directory.
- Type `bower install`
- Install the Google App Engine SDK for Python if you don't have it
- Then navigate to the home repo directory
- Run `dev_appserver.py .` in the terminal
- Go to `localhost:8080` in your browser
- Code!

## _Without API_
- If you have the Polymer CLI install, use `polymer serve` in `/repo/client`
- If not, type `python -m SimpleHTTPServer 8080` in `/repo/client`
- Then, go to `localhost:8080` in your browser
- Start coding

## Info
The project is built around [Polymer Starter Kit 2.0](https://www.polymer-project.org/1.0/)
but is heavily modified. The main client content holders are in /client/src. These are
the views for the app. Custom elements are in /client/elements and all CSS and most
Javascript are contained in elements. There backend is written in Python using the
[Google Cloud Endpoints](https://cloud.google.com/appengine/docs/python/endpoints/getstarted/backend/write_api)
framework. The main files for the backend are in /server.
