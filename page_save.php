<?php

// sudo cp /home/pi/Documents/sinproject/page.php /var/www/html
// sudo service apache2 restart

$conn = mysqli_connect ('localhost', 'root', 'password', 'arduino');
?>
<html>
	<head>
		<title>Musée</title>
		<tr>
            <th colspan="2">The table header</th>
		</tr>
	</head>
	<body>
		Ceci est une base de données : </br>

		<?php

		$resultat = mysqli_query($conn, 'SELECT * FROM valeurs ORDER BY id DESC LIMIT 0,5');

		while($donnees = mysqli_fetch_assoc($resultat))
		{
			echo "Température :";
			echo $donnees['temperature'];
			echo "</br>";
			echo "\n";
			echo "Humidité :";
			echo $donnees['humidity'];
			echo $donnees['time'];
			echo "\n"; 
			
		}
		?>

	</body>
</html>
