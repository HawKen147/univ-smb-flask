window.onload = (event) => {
    alert('ca marche');
    read_json();
}

function read_json(){
    
    fetch('/static/alias.json')
  .then(response => response.json())
  .then(data => {
    // Do something with the parsed JSON data
    console.log(data);
  })
  .catch(error => console.error(error));
}

    

