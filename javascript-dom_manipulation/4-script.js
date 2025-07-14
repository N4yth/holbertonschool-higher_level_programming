const docs = document.querySelector('ul.my_list');

function addElement () {
  const node = document.createElement('li');
  const textnode = document.createTextNode('Item');
  node.appendChild(textnode);
  docs.appendChild(node);
}
document.getElementById('add_item').addEventListener('click', addElement);
