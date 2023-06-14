#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
    console.error('Movie ID is required');
    process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
    if (error) {
	console.error('Error:', error);
	process.exit(1);
    }

    if (response.statusCode !== 200) {
	console.error('API request failed with status code:', response.statusCode);
	process.exit(1);
    }

    const movieData = JSON.parse(body);
    const characterPromises = movieData.characters.map((characterUrl) => {
	return new Promise((resolve, reject) => {
	    request.get(characterUrl, (error, response, body) => {
		if (error) {
		    reject(error);
		} else if (response.statusCode === 200) {
		    const characterData = JSON.parse(body);
		    resolve(characterData.name);
		} else {
		    reject(new Error(`API request failed with status code: ${response.statusCode}`));
		}
	    });
	});
    });

    Promise.all(characterPromises)
	.then((characterNames) => {
	    characterNames.forEach((name) => {
		console.log(name);
	    });
	})
	.catch((error) => {
	    console.error('Error:', error);
	    process.exit(1);
	});
});
