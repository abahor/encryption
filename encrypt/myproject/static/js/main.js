var myid = document.getElementById('getmyid')
var connectid = document.getElementById('putid')
var token = document.getElementById('token')
myid.addEventListener('click',myidclicked())



function myidclicked() {
    var d = new XMLHttpRequest()
    var myid = document.getElementById('getmyid')
    d.open('POST','https://server.com/myid?token='+token)
    d.onreadystatechange = function(){ if (this.readyState == 4 && this.status == 200) {
       // Typical action to be performed when the document is ready:

       document.getElementById("mycontactid").value = xhttp.responseText;}
       else if (this.status == 404 ){
            window.location.replace("/logout");
            }
       }
}


function contactid() {
    var d = new XMLHttpRequest();
    var connectid = document.getElementById('putid')
    if(Object.keys(connectid).length < 16){
        alert('please put a valid contact id')
    }
    else{

    d.open('POST','http://webserver.com/seeifconnected?token=' + token + '&hisid='+ connectid); // url on the server to check the availablity of the user
    d.onreadystatechange = function(){ if (this.readyState == 4 && this.status == 200) {
       // Typical action to be performed when the document is ready:
       if (this.responseText== 'success'){
       window.location.replace('/got_connected?peerid='+connectid + '&token=' + token)
     } else if (this.responseText == "don't exist"){
        window.location.replace('/logout')
     }
     }
     d.send()
 }

}
