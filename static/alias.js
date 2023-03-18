window.onload = (event) => {

    send_request();
}

function send_request (){
    var xhr = new XMLHttpRequest();
        xhr.open('GET', '/alias_json', true);
        xhr.onload = function() {
            if (this.status === 200) {
                var data = JSON.parse(this.responseText);
                var tbody = document.getElementById('table-body');
                console.log('tbody',tbody);
                for (var i = 0; i < data.length; i++) {
                    var tr = document.createElement('tr');
                    var td_alias = document.createElement('td');
                    td_alias.innerText = data[i].alias;
                    tr.appendChild(td_alias);
                    var td_ip_address = document.createElement('td');
                    td_ip_address.innerText = data[i].ip_address;
                    tr.appendChild(td_ip_address);
                    var td_port = document.createElement('td');
                    td_port.innerText = data[i].port;
                    tr.appendChild(td_port);
                    tbody.appendChild(tr);
                }
            }   
        };
    xhr.send();
}