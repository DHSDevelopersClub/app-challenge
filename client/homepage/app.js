var list = {
    "description": "A list of English verbs.",
    "verbs": [
        {
            "present": "hike",
            "past": "accepted"
        },
        {
            "present": "surf",
            "past": "added"
        },
        {
            "present": "snowboard",
            "past": "admired"
        },
        {
            "present": "climb",
            "past": "admitted"
        },
        {
            "present": "bike",
            "past": "advised"
        },
        {
            "present": "skate",
            "past": "afforded"
        },
        {
            "present": "scooter",
            "past": "agreed"
        },
        {
            "present": "run",
            "past": "alerted"
        },
        {
            "present": "read",
            "past": "allowed"
        },
        {
            "present": "bake",
            "past": "amused"
        },
        {
            "present": "cook",
            "past": "analysed"
        },
        {
            "present": "play",
            "past": "announced"
        },
        {
            "present": "skydive",
            "past": "annoyed"
        },
        {
            "present": "longboard",
            "past": "answered"
        },
        {
            "present": "bmx",
            "past": "apologised"
        },
        {
            "present": "sing",
            "past": "appeared"
        },
        {
            "present": "dance",
            "past": "applauded"
        },
        {
            "present": "swim",
            "past": "appreciated"
        },
        {
            "present": "skimboard",
            "past": "approved"
        }
    ]
}

var $verb = document.querySelector('#verb');

function printRandom(data) {
  'use strict';
  var i = Math.floor((Math.random() * list.verbs.length));
  $verb.textContent = "Let's " + list.verbs[i].present;
}

window.setInterval("printRandom()", 900);
