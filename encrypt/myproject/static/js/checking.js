setInterval(function(){
    d.open('POST','http://127.0.0.1:5000/seeifconnected?token=' + token + '&hisid='+ connectid); // url on the server to check the availablity of the user
    d.onreadystatechange = function(){ if (this.readyState == 4 && this.status == 200) {
       // Typical action to be performed when the document is ready:
     if (this.responseText== 'success'){
       window.location.replace('/got_connected?peerid='+connectid + '&token=' + token)
     } else if (this.responseText == "don't exist"){
        window.location.replace('/logout')
     }
     } }}, 3000);