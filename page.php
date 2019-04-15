<?php

// sudo cp /home/pi/Documents/sinproject/page.php /var/www/html
// sudo service apache2 restart

$conn = mysqli_connect ('localhost', 'root', 'password', 'arduino');
?>
<html>
<head>
<title>Musée</title>
</head>
<body>
Ceci est une base de données : </br>
<?php

$resultat = mysqli_query($conn, 'SELECT * FROM valeurs ORDER BY time DESC LIMIT 1');

while($donnees = mysqli_fetch_assoc($resultat))
{
	echo $donnees['temperature'];
	echo "\n";
	echo $donnees['time'];
	echo "\n"; 
	
}
?>

</body>
</html>
