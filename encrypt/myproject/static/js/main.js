var myid = document.getElementById('getmyid')
var connectid = document.getElementById('putid')
var token = document.getElementById('token').value
myid.addEventListener('click',myidclicked())
connectid.addEventListener('click',check_available())


function myidclicked() {
    var d = new XMLHttpRequest()
//    var myid = document.getElementById('getmyid')
//    d.open('POST','http://127.0.0.1:5000/myid?token='+token)

    d.onreadystatechange = function(){ if (this.readyState == 4 && this.status == 200) {
       // Typical action to be performed when the document is ready:

       document.getElementById("mycontactid").value = xhttp.responseText;
       } else if (this.status == 404 ){
            window.location.replace("/logout");
            }
       }
      params = 'token='+token
      d.open('POST','http://127.0.0.1:5000/myid') // THIS MAY CHANGE IF WE GOT TO CHANGE THIS TO /myid?token=' + token
      d.send(params)
}


function check_available() {

    var connectid = document.getElementById('contactid')
    if(Object.keys(connectid).length < 48){
//        alert('please put a valid contact id')
        $('.alert').alert()
        return ''
    }
    else{
    var d = new XMLHttpRequest();
    d.onreadystatechange = function(){
    if (this.readyState == 4 && this.status == 200) {
        // Typical action to be performed when the document is ready:
        if (this.responseText== 'success'){
            //       window.location.replace('/got_connected?peerid='+connectid + '&token=' + token)
            window.open('/got_connected?peerid='+ connectid + '&token=' + token)
       } else if (this.responseText == "don't exist"){
          window.location.replace('/logout')
          }
       }
    }
    params= 'token='+token +'&hisid=' + connectid
    d.open('POST','http://127.0.0.1:5000/seeifconnected?token=' + token + '&hisid='+ connectid); // url on the server to check the availablity of the user
    d.send();
    # d.send(params);


}
}

//function get_cookies() {
//  var d = new XMLHttpRequest();
//  d.onreadystatechange = function() {
//    if (this.Response != '' && this.status == 200 ) {
//      document.cookie = this.responseText;
//    } else {
//        window.location.replace('/logout')
//    }
//  }
//  d.open("GET",'/send_cookies');
//  d.send();
//}
//
//get_cookies()


$(document).ready(function(){
  socket = io('http://127.0.0.1:5000/mainsocket')  // check for the token in server side socket
// var id = 0        ←←← ←   ←               ←
  socket.on('receive',function (msg) {
    var id = msg['hisid']
    // id = msg['hisid']  uncomment this if it's not working    ←          ←←←←←
    $('#connection_id').html('this id: '+ id  ' is trying to contact with you' )
    $('.modal').modal('show');
    $('#open_connection').on('click',function () { /// put this outside the scope of the recevidefunction if it not working
      window.open('/got_connected?peerid='+ msg['hisid'] + '&token=' + token) /// with this
    })

  })



})


function keep_alive(){
var d = new XMLHttpRequest()

d.onreadystatechange = function(){
    if(this.status_code == 200 ){

    }
}
else{
    alert('check your internet connection')
}
d.open('POST','http://127.0.0.1:5000/keep_alive?token='+ token )
d.send()
}

setInterval(keep_alive(), 3000);
