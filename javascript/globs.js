//define functions and global variables here...
var siteloc = "http://localhost/ExpoRepo";
var scriptloc = "/scripts/"

function getOutput(inp)
{
  $.ajax({
      url: siteloc + scriptloc + "expo.py",
      data: {inp:$("#input").val(), pow:inp},
      dataType: 'json',
      success: function (res) {
                  console.log(res);
                  if(res[0][0] != "None")
                  {
			out = "&nbsp;" + res[0];             
$("#target").html(out); 
				  } // end if
              }
    });
}

