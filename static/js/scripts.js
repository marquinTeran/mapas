$(function (){
	if(navigator.geolocation)
	{
		navigator.geolocation.getCurrentPosition(getCoords, getError);
	} else 
	{
		initialize(0.357482, -78.11687);
	}

	function getCoords(positions)
	{
		var lat = positions.coords.latitude;
		var lng = positions.coords.longitude;

		initialize(lat, lng);
	}

	function getError(err)
	{
		initialize(0.357482, -78.11687);
	}

	function initialize(lat, lng)
	{
		var latlng = new google.maps.LatLng(lat, lng);
		var map;
		var mapSettings = {
			center: latlng,
			zoom: 15,
			mapTypeId: google.maps.MapTypeId.ROADMAP
		}
		map = new google.maps.Map($('#mapa').get(0), mapSettings);
        
        var marker = new google.maps.Marker({
          map:map,
          draggable:true,
          animation: google.maps.Animation.DROP,
          position: latlng,
          title: 'Arrastrame!!'
        });

        google.maps.event.addListener(marker, 'position_changed', function(){
        	getMarkerCoords(marker);
        });

        function getMarkerCoords(marker)
        {
        	var markerCoords = marker.getPosition();
        	$("#id_lat").val( markerCoords.lat() );
        	$("#id_lng").val( markerCoords.lng() );
        }

        $("#form_coords").submit(function(e){
        	e.preventDefault();

        	$.post('/coords/save', $(this).serialize(), function(data){
        		if(data.ok)
        		{

        		} else {
        			alert(data.msg);
        		}
        	}, 'json');
        });
	}
});