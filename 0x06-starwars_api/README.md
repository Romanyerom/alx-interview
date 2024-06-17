Explanation of the Script

    Import the request module:

    javascript

const request = require('request');

Get the movie ID from command-line arguments:

javascript

const movieId = process.argv[2];

Construct the API URL using the movie ID:

javascript

const apiUrl = ;

Make an HTTP GET request to fetch movie details:

javascript

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

Parse the movie details and extract the character URLs:

javascript

const filmData = JSON.parse(body);
const characters = filmData.characters;

For each character URL, make an HTTP GET request to fetch character details and print the name:

javascript

characters.forEach((characterUrl) => {
  request(characterUrl, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    const characterData = JSON.parse(body);
    console.log(characterData.name);
  });
});
