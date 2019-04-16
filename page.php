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
		</br>
		<pre><b>                                                                                       Température (°C)       Humidité (%)         Timelog  </b></pre>
		</br>
		<center>
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
			</br>
			</br>
			</br>
			</br>
			<img src="image.jpg" width="50%" height="50%">
		</center>
	</body>
</html>
