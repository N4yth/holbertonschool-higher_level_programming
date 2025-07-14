const docs = document.querySelector('header');

function addElement () {
  docs.textContent = 'New Header!!!';
}
document.getElementById('update_header').addEventListener('click', addElement);
