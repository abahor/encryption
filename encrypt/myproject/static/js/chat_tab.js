var listening = io.connect('http://127.0.0.1:5000/start_chat') // put the name and  the route of the server  //  CHECK THE TOKEN ON THE SERVER IN SOCKET CONNECTION FOR TOKEN AUTHENTICATION
var template_receive = document.getElementById('receive')
var template_sent = document.getElementById('sent')
var container = document.querySelector('.msg_container_base')
var my_key = my_key()
var his_id = his_id()
var his_public_key
// var button = document.getElementById('btn-chat')

// i need way to make multi key available
listening.on('connect',function () {
  listening.emit('my_key', {'key': my_key, 'hisid': his_id, 'token':token })
})
listening.on('exchange', function (msg) {
  his_public_key = msg;
})
// NOTE: if it doesn't work change it to io.connect('')
// make the first exchange on the number of keys the exchange the keys


listening.on('receive',function (msg) {
  var text = decrypt_message(msg['message'])
  let temp = template_receive.content.cloneNode(true)
  temp.querySelector('.subject').innerHTML = text
  temp.querySelector('.current_date').innerHTML = msg['date'] // i can do this on the server but let's do it here any way
  container.appendChild(temp)
})


function decrypt_message(msg){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function(){
    if (this.readyState == 4 && this.status == 200){
      return this.responseText;
    }
  }
  xhttp.open("GET", "/decrypt?message="+ msg);
  xhttp.send();
}


function encrypt (msg,his_public_key) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function(){
    if (this.readyState == 4 && this.status == 200){
      return this.responseText;
  }
  }
  xhttp.open("GET", "/encrypt?message="+ msg + '&hiskey='+ his_public_key);
  xhttp.send();
}

function my_key(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange()=  function() {
    if (this.readyState == 4 && this.status == 200) {

      return this.responseText;
    }
  }
  xhttp.open('GET','/get_public_key')
  xhttp.send()
}

function his_id() {
    var split = window.location.search.split('?')
    split = split[0].split('&')
    split = split[0].split('peerid=')
    return split[1];
}
function date_now() {
  var date = new Date();

  var d = ((date.getHours() > 12)? date.getHours()%12 + ' p.m. '+ date.getMinutes() +' m' : date.getHours() + ' a.m.' + date.getMinutes() +' m')

  return d
}

$(document).ready(function(){
  $('#btn-chat').on('click',function () {
    var message = encrypt($('#btn-input').val(),his_public_key)
    listening.emit('send_message',{'message': message, 'token':token,'hisid':his_id, 'date': date_now() })
    let sent = template_sent.content.cloneNode(true);
    sent.querySelector('.subject').innerHTML = $('#btn-input').val()
    sent.querySelector('.current_date').innerHTML = date_now()
    container.appendChild(sent)
  })
}
