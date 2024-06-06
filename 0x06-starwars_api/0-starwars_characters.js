#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;
  const names = [];

  characters.forEach((characterUrl, index) => {
    request(characterUrl, function (charError, charResponse, charBody) {
      if (charError) {
        console.error(charError);
        return;
      }

      const character = JSON.parse(charBody);
      names[index] = character.name;

      if (names.filter(name => name !== undefined).length === characters.length) {
        names.forEach(name => console.log(name));
      }
    });
  });
});
