const docs = document.getElementById('list_movies');
const request = new Request('https://swapi-api.hbtn.io/api/films/?format=json');

fetch(request).then((response) => {
  return response.json();
})
  .then((data) => {
    data.results.forEach(element => {
      const node = document.createElement('li');
      const textnode = document.createTextNode(element.title);
      node.appendChild(textnode);
      docs.appendChild(node);
    });
  });
