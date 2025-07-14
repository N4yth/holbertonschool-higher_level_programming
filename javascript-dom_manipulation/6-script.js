const docs = document.getElementById('character');
const request = new Request('https://swapi-api.hbtn.io/api/people/5/?format=json');

fetch(request).then((response) => {
  return response.json();
})
  .then((data) => {
    const name = document.createTextNode(data.name);
    docs.appendChild(name);
  });
