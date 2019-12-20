var myid = document.getElementById('getmyid')
var connect_id = document.getElementById('putid')
var token = document.getElementById('token').value
myid.addEventListener('click',myidclicked())

//connectid.addEventListener('click',check_available())


function myidclicked() {
    var d = new XMLHttpRequest()
//    var myid = document.getElementById('getmyid')
//    d.open('POST','http://127.0.0.1:5000/myid?token='+token)

    d.onreadystatechange = function(){
    if (this.readyState == 4 && this.status == 200) {
       // Typical action to be performed when the document is ready:

       document.getElementById("mycontactid").value = d.responseText;
    } else if (this.status == 404 ){
            window.location.replace("/logout");
            }
       }
      params = 'token='+token
      d.open('POST','http://127.0.0.1:5000/myid?token='+ token) // THIS MAY CHANGE IF WE GOT TO CHANGE THIS TO /myid?token=' + token
//      d.send(params)
      d.send()
}




/*
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
//    params= 'token='+token +'&hisid=' + connectid
    d.open('POST','http://127.0.0.1:5000/seeifconnected?token=' + token + '&hisid='+ connectid); // url on the server to check the availablity of the user
    d.send();
//    d.send(params);


}
}

function get_cookies() {
  var d = new XMLHttpRequest();
  d.onreadystatechange = function() {
   if (this.Response != '' && this.status == 200 ) {
      document.cookie = this.responseText;
    } else {
        window.location.replace('/logout')
    }
  }
  d.open("GET",'/send_cookies');
  d.send();
}

get_cookies()
*/



$(document).ready(function(){
  socket = io('http://127.0.0.1:5000/mainsocket')  // check for the token in server side socket
// var id = 0        ←←← ←   ←               ←
  socket.on('receive',function (msg) {
    var id = msg['hisid']
    // id = msg['hisid']  uncomment this if it's not working    ←          ←←←←←
    $('#connection_id').html('this id: '+ id  ' is trying to contact with you' )
    $('.modal').modal('show');

//     CHECK FOR THE CONNECTION IF ACCEPTED OR NOT
    $('#open_connection').on('click',function () { /// put this outside the scope of the received function if it not working
      check(id,token)
      socket.emit('accepted',{'id':id , 'token': token })
      window.open('/got_connected?peerid='+ msg['hisid'] + '&token=' + token) /// with this
    })
    $('#close_connection').on('click',function(){
       check(id,token)
       socket.emit('rejected',{'id':id , 'token': token })
    })

  })

// END OF THE FUNCTION ABOVE AND START OF ANOTHER

$("#putid").on('click',function(){

socket.emit('see_if_connected',{ 'token':token,'his_id': connect_id })


})

// END OF THE OTHER FUNCTION

// START OF FUNCTION

socket.on('accepted_of_connection', function(msg){
    var id = msg['hisid']

    window.open('/got_connected?peerid='+ id + '&token=' + token) /// with this

})

socket.on('rejected_of_connection', function(msg){
    id = msg['hisid']
    alert( id + 'refused to connect')
})






// USEFUL FUNCTION FOR CHECKING VARIABLES

function check(id,token){
if(Object.keys(id).length < 48){
//        alert('please put a valid contact id')
        $('.alert').alert()
        return ''
}
if (Object.keys(token).length < 48){
    window.location.replace('/logout')
}
}

})


function keep_alive(){
var d = new XMLHttpRequest()

d.onreadystatechange = function(){
    if(this.status_code == 200 ){

    } else if (this.status_code == 404){
        window.location.replace('/logout')
    }
}


d.open('POST','http://127.0.0.1:5000/keep_alive?token='+ token )
try {
    d.send()
}
catch {
    alert('check your internet connection')
}

}

setInterval(keep_alive(), 8000);






