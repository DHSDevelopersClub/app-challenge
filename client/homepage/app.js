gapi.load('auth2', function() {
  gapi.auth2.init();
});

function signIn() {
  var auth2 = gapi.auth2.getAuthInstance();
  auth2.signIn();
  var request = auth2.insert_user({

  })
}

function signOut() {
  var auth2 = gapi.auth2.getAuthInstance();
  auth2.signOut();
}


var list = {"verbs": ['fun', 'creative', 'new', 'active', 'awesome', 'new', 'great', 'super', 'similar', 'athletic', 'smart']}

var $adjective = document.querySelector('#adjective');

function printRandom(data) {
  'use strict';
  var i = Math.floor((Math.random() * list.verbs.length));
  $adjective.textContent = 'An app for finding ' + list.verbs[i] + ' friends.';
}

window.setInterval("printRandom()", 900);
