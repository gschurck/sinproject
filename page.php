<?php

// sudo cp /home/pi/Documents/sinproject/page.php /var/www/html
// sudo service apache2 restart

$conn = mysqli_connect ('localhost', 'root', 'password', 'arduino');
?>
<html>
	<head>
		<link rel="stylesheet" type="text/css" href="mystyle.css">
		<title>Musée</title>
	</head>
	<body>
		<!--
		<table>
			<thead>
				<tr>
					<th colspan="2">The table header</th>
				</tr>
			</thead>
			<tbody>
				<tr>
					<td>The table body
					
					</td>
					<td>with two columns</td>
				</tr>
			</tbody>
		</table>
		-->
		</br>
		<b>Température (°C) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Humidité (%) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Timelog  </b>
		</br>
		
		<?php

		$resultat = mysqli_query($conn, 'SELECT * FROM valeurs ORDER BY id DESC LIMIT 0,5');

		while($donnees = mysqli_fetch_assoc($resultat))
		{
			echo "&nbsp;&nbsp;&nbsp;&nbsp;";
			echo $donnees['temperature'];
			echo "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
			echo $donnees['humidity'];
			echo "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
			echo $donnees['time'];
			echo "</br>";
		}
		?>
		</br>
		<img src="image01.jpg" width="50%" height="50%">
		
	</body>
</html>
