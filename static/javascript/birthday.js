var Alert = new CustomAlert();
function CustomAlert(){
  this.render = function(){
      //Show Modal
      let popUpBox = document.getElementById('popUpBox');
      popUpBox.style.display = "block";
      //Close Modal
      document.getElementById('closeModal').innerHTML = '<button onclick="Alert.ok()">OK</button>';
  }
this.ok = function(){
  document.getElementById('popUpBox').style.display = "none";
  document.getElementById('popUpOverlay').style.display = "none";
}
}

function checkInput()
{
  // get today's date.
  var today = new Date();
  today.setHours(0,0,0,0); // set time to start of day for comparison.

  // create a new date based on user input.
  var bdate = new Date(Date.parse( 
    document.querySelector('select[name="year"]').value + ' ' +
    document.querySelector('select[name="month"]').value + ' ' +
    document.querySelector('select[name="day"]').value
  ));
  today.setYear(0); // ignore year part of date.
  bdate.setYear(0); // ignore year part of date.

  if (today.valueOf() == bdate.valueOf())
  {
    function CustomAlert();
  }
}