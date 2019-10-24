var myid = document.getElementById('getmyid')
var connectid = document.getElementById('putid')

myid.addEventListener('click',myidclicked())



function myidclicked() {
    var d = new XMLHttpRequest()
    d.open('GET','https://server.com/myid')
    d.onreadystatechange = function(){ if (this.readyState == 4 && this.status == 200) {
       // Typical action to be performed when the document is ready:
       document.getElementById("mycontactid").value = xhttp.responseText;}}
}

function myidclicked() {
    var d = new XMLHttpRequest()
    d.open('GET','https://server.com/myid')
    d.onreadystatechange = function(){ if (this.readyState == 4 && this.status == 200) {
       // Typical action to be performed when the document is ready:
       document.getElementById("mycontactid").value = xhttp.responseText;}}
}

function myidclicked() {
    var d = new XMLHttpRequest();
    d.open('GET','http://127.0.0.1:5000/xml');// url on the server to get user current id
    d.onreadystatechange = function(){ if (this.readyState == 4 && this.status == 200) {
       // Typical action to be performed when the document is ready:
       document.getElementById('mycontactid').value = this.responseText;
     } else {

      window.location.replace("/logout");
     }
     }
     d.send()
}

function contactid() {
    var d = new XMLHttpRequest();
    d.open('GET','http://127.0.0.1:5000/xml'); // url on the server to check the availablity of the user
    d.onreadystatechange = function(){ if (this.readyState == 4 && this.status == 200) {
       // Typical action to be performed when the document is ready:
       document.getElementById('contactid').value = this.responseText;
     } else {
       $('.alert').alert()
     }
     }
     d.send()
}
