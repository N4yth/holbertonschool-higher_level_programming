
document.addEventListener('DOMContentLoaded', function () {
  const docs = document.getElementById('hello');
  const request = new Request('https://hellosalut.stefanbohacek.dev/?lang=fr');
  fetch(request).then((response) => {
    return response.json();
  })
    .then((data) => {
      docs.textContent = data.hello;
    });
});
