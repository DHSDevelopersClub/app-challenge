var list = {"verbs": ['fun', 'creative', 'new', 'active', 'awesome', 'new', 'great', 'super', 'similar', 'athletic', 'smart']}

var $adjective = document.querySelector('#adjective');

function printRandom(data) {
  'use strict';
  var i = Math.floor((Math.random() * list.verbs.length));
  $adjective.textContent = 'An app for finding ' + list.verbs[i] + ' friends.';
}

window.setInterval("printRandom()", 900);
