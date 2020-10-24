function validateForm()
{
var x=document.forms["Contact Us"]["Firstname"].value;
var y=document.forms["Contact Us"]["Lastname"].value;
var z=document.forms["Contact Us"]["Email"].value;
var atpos=z.indexOf("@");
var dotpos=z.lastIndexOf(".");



if (x==null || x=="")
  {
  alert("First name must be filled out");
  return false;
  }
  
 else if (y==null || y=="")
  {
  alert("Last name must be filled out");
  return false;
  }

  

  
  else if(atpos<1 || dotpos<atpos+2 || dotpos+2>=z.length)
  {
  alert("Not a valid e-mail address");
  return false;
  }
  
  
  else
  {
 alert("Information received - Thank You");
 return true;
 }
  
  
}