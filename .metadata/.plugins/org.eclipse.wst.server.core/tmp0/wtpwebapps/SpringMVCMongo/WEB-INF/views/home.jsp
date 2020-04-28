<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ page session="false" %>
<html>
<head>
	<title>Home</title>
</head>
<body>
<h1>
	Hello world!  
</h1>

<P>  The time on the server is ${serverTime}. </P>
<table border="1">

<c:forEach var="dto" items="${list }">
	
	<tr>
		<td>
			${dto }
		</td>
	</tr>
</c:forEach>
</table>
</body>
</html>
