<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script type="text/javascript" src="https://code.jquery.com/jquery-3.4.1.js"></script>
<script type="text/javascript">


$(function(){

	$.getJSON("http://localhost:8585/crawling", function(data){
		console.log(data.movies)
		
		$.each(data, function(key, val){
			if(key == 'movies'){
				val.sort(function(a, b){
					return b.star - a.star;
				})
				for(var i=0;i<val.length;i++){
					 var $tr = $("<tr>");
                     
                     for(var j in val[i]) {
                        $tr.append($("<td>").html(val[i][j]));
                     }
                     
                     $("tbody").append($tr);
                }
			}
		})
		$("#tbody").append(data)
	})
})
</script>

</head>
<body>
	<table border=1>
		<thead>
			<tr>
				<th>TITLE</th>
				<th>STAR</th>
			</tr>
		</thead>
		<tbody id="tbody">
		</tbody>
	</table>
</body>
</html>