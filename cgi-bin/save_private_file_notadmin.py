#!/usr/bin/python
import cgi, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
# Get filename here.
fileitem = form['filename']
# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open('adithya_images\\' + fn, 'wb').write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'   
   
   htmlFilename = 'Private_Pictures_Adithya.html'
   htmlFile = open('client\\Private_Pictures_Adithya.html', 'w')
   # ... write the header
   htmlFile.write("<html>\n")
   htmlFile.write("<head>\n")
   htmlFile.write("<title> WALL-Exercising | e-Verify </title>\n")
   htmlFile.write("</head>\n")
   # ... write the body
   htmlFile.write("<body>\n")
   
   
   htmlFile.write('''<!DOCTYPE html>
<html>
<meta charset="UTF-8">
<meta name = "viewpoint" content="width=device-width, initial-scale=1.0">
<head>
  <title>WALL-Exercising | e-Verify</title>
<style>
div.header {
  position: -webkit-sticky;
  position: sticky;
  box-shadow: 0px 4px 5px gray;
  top: 0;
  padding: 25px;
  background-color: #f5f5f5;
  text-align: center;
  width: 100%;
}
body {
  font-family: "Lucida Sans Unicode", "Lucida Grande", sans-serif;
  background-color: white;
  text-align: center;
}

div.shadow {
  color: white;
  text-shadow: 1px 1px 2px black, 0 0 10px black, 0 0 5px black;
}

* {
  box-sizing: border-box;
}

/* Add padding to containers */
.container {
  padding: 15px;
  background-color: white;
}

input[type=text], input[type=password] {
  width: 50%;
  padding: 15px;
  margin: 10px 0 20px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}

input[type=text]:focus, input[type=password]:focus {
  background-color: #ddd;
  outline: none;
}

/* Overwrite default styles of hr */
hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}

/* Set a style for the submit button */
.registerbtn {
  background-color: #00008A;
  color: white;
  box-shadow: 0px 7px 5px #000049;
  padding: 16px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 7%;
  opacity: 0.9;
}

.registerbtn:hover {
  opacity: 1;
}

/* Add a blue text color to links */
a {
  color: #E6B000;
}

/* Set a grey background color and center the text of the "sign in" section */
.footer {
  background-color: black;
  text-align: center;
  width: 100%;
}
.gallery {
	margin: 10px 50px;
}
.gallery img {
	transition: 1s;
	padding: 15px;
	width: 300px;
	height: 200px;
}
.gallery img:hover {
	filter: grayscale(75%);
	transform: scale(1.1);
}

</style>
</head>
<body>
<div class = "header">
	<b>The WALL-Exercising | <a href="Sign In.html">Sign in</a> | <a href="App.html">Home</a> | <a href="Exercise app Inspiration.html">Inspiration</a> | <a href="Excercise app Research.html">Analytics</a> | <a href="Excercise app Gallary.html">Gallery</a> | <a href="Admin.html">Admin-Only</a></b>
</div>
<br/>

<center>
<div class = "shadow">
    <h1>Your Private Pictures!</h1>
	<br/><br/>
</div>


''')
   
   
   
   
   # write one line for each image in the directory
   fileNum=1
   for file in os.listdir("adithya_images\\"):
     imgLine='<a href = "..\\adithya_images\\' + file +'"><img src="..\\adithya_images\\' + file + '" alt="image' + str(fileNum) + '" width="300" height="200"><br/>' + '\n'
     removeLine='<b><a href = "../cgi-bin/delete_private_file_notadmin.py?post=..\\adithya_images\\' + file + '">Delete picture</a></b><br/><br/>' + '\n'
     htmlFile.write(imgLine)
     htmlFile.write(removeLine)
     fileNum+=1
   htmlFile.write('''<h3>Upload your own private image!</h3>
<form enctype = "multipart/form-data" action = "../cgi-bin/save_private_file_notadmin.py" method = "post">
   <p>File: <input type = "file" name = "filename" /></p>
   <p><input type = "submit" value = "Upload" class = "registerbtn"/></p>
</form>
<br/>
<!--
<b><a href="../cgi-bin/delete_private_file.py">Delete</a></b>

<form enctype = "multipart/form-data" action = "../cgi-bin/delete_private_file_notadmin.py" method = "post">
   <p>File: <input type = "file" name = "filename" /></p>
   <p><input type = "submit" value = "Delete" /></p>
</form>
-->
<br/>
</center>
<div class = "container footer" style = "color:gray">
	  <p><b>The WALL-Exercising...................Sign up today!</b><p>
	  Call me at: <a href="tel:+15167896226">+1-516-789-6226</a>
</div>''')
   htmlFile.write("</body>\n")
   htmlFile.write("</html>\n")
   htmlFile.close()  
   htmlFile = open('client\\App Image Verification.html', 'w')
   # ... write the header
   htmlFile.write("<html>\n")
   htmlFile.write("<head>\n")
   htmlFile.write("<title> WALL-Exercising | e-Verify </title>\n")
   htmlFile.write("</head>\n")
   # ... write the body
   htmlFile.write("<body>\n")
      
   htmlFile.write('''<!DOCTYPE html>
    <html>
    <meta charset="UTF-8">
    <meta name = "viewpoint" content="width=device-width, initial-scale=1.0">
    <head>
      <title>WALL-Exercising | e-Verify</title>
    <style>
    div.header {
      position: -webkit-sticky;
      position: sticky;
      box-shadow: 0px 4px 5px gray;
      top: 0;
      padding: 25px;
      background-color: #f5f5f5;
      text-align: center;
      width: 100%;
    }
    body {
      font-family: "Lucida Sans Unicode", "Lucida Grande", sans-serif;
      background-color: white;
      text-align: center;
    }

    div.shadow {
      color: white;
      text-shadow: 1px 1px 2px black, 0 0 10px black, 0 0 5px black;
    }

    * {
      box-sizing: border-box;
    }

    /* Add padding to containers */
    .container {
      padding: 15px;
      background-color: white;
    }

    input[type=text], input[type=password] {
      width: 50%;
      padding: 15px;
      margin: 10px 0 20px 0;
      display: inline-block;
      border: none;
      background: #f1f1f1;
    }

    input[type=text]:focus, input[type=password]:focus {
      background-color: #ddd;
      outline: none;
    }

    /* Overwrite default styles of hr */
    hr {
      border: 1px solid #f1f1f1;
      margin-bottom: 25px;
    }

    /* Set a style for the submit button */
    .registerbtn {
      background-color: #00008A;
      color: white;
      box-shadow: 0px 7px 5px #000049;
      padding: 16px 20px;
      margin: 8px 0;
      border: none;
      cursor: pointer;
      width: 7%;
      opacity: 0.9;
    }

    .registerbtn:hover {
      opacity: 1;
    }

    /* Add a blue text color to links */
    a {
      color: #E6B000;
    }

    /* Set a grey background color and center the text of the "sign in" section */
    .footer {
      background-color: black;
      text-align: center;
      width: 100%;
    }
    .gallery {
        margin: 10px 50px;
    }
    .gallery img {
        transition: 1s;
        padding: 15px;
        width: 300px;
        height: 200px;
    }
    .gallery img:hover {
        filter: grayscale(75%);
        transform: scale(1.1);
    }

    </style>
    </head>
    <body>
    <div class = "header">
        <b>The WALL-Exercising | <a href="Sign In.html">Sign in</a> | <a href="App.html">Home</a> | <a href="Exercise app Inspiration.html">Inspiration</a> | <a href="Excercise app Research.html">Analytics</a> | <a href="Excercise app Gallary.html">Gallery</a> | <a href="Admin.html">Admin-Only</a></b>
    </div>
    <br/>

    <center>
    <div class = "shadow">
        <h1>Adithya's Private Pictures!</h1>
        <br/><br/>
    </div>
    ''')

   fileNum = 1
   for file in os.listdir("adithya_images\\"):
       imgLine='<img src="..\\adithya_images\\' + file + '" alt="image' + str(fileNum) + '" width="300" height="200"><br/>' + '\n'
       scriptLine='''
    <script>
      var slider'''+str(fileNum)+''' = document.getElementById("myRange'''+str(fileNum)+'''");
      var output'''+str(fileNum)+'''  = document.getElementById("demo'''+str(fileNum)+'''");
      output'''+str(fileNum)+'''.innerHTML = slider'''+str(fileNum)+'''.value;
      slider'''+str(fileNum)+'''.oninput = function() {
        output'''+str(fileNum)+'''.innerHTML = this.value;
      }
      document.getElementById("mytext'''+str(fileNum)+'''").value = this.value;
    </script>
    '''
       buttonLine='''
    <form name="input" action="../cgi-bin/App test.py" method="post">
     <input type="text" name="points" id="mytext'''+str(fileNum)+'''"><br/>
     <input type="submit" value="Submit" class = "registerbtn">
    </form>'''
       htmlFile.write(imgLine)
       htmlFile.write(scriptLine)
       htmlFile.write(buttonLine)
       fileNum+=1
   htmlFile.write('''
    <br/>
    <!--
    <b><a href="../cgi-bin/delete_private_file.py">Delete</a></b>

    <form enctype = "multipart/form-data" action = "../cgi-bin/delete_private_file.py" method = "post">
       <p>File: <input type = "file" name = "filename" /></p>
       <p><input type = "submit" value = "Delete" /></p>
    </form>
    -->
    <br/>
    </center>
    <div class = "container footer" style = "color:gray">
          <p><b>The WALL-Exercising...................Sign up today!</b><p>
          Call me at: <a href="tel:+15167896226">+1-516-789-6226</a>
    </div>''')
   htmlFile.write("</body>\n")
   htmlFile.write("</html>\n")
   htmlFile.close()
   
else:
   message = 'No file was uploaded'

print("Content-Type: text/html\n")
print("<html>")
print("<body>")
print("<p>%s</p>"  % (message))
print("<h3>To go back to your private gallery, <a href=\"..\\client\\Private_Pictures_Adithya.html\">click here</a></h2>")
print("</body>")
print("</html>")