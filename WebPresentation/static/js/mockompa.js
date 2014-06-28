

function ompaCurrent(){
  var scores, scoresList, scoreStr;
  
  scores = {
    OCC:3992,
    SH:2919,
    MEAD:3094,
    PARK:2777,
    MCC:2643,
    MRSC:2074,
    MIRA:1276,
    MVP:1611,
    CCC:993
  };
  
  scoresList = Object.keys(scores).sort( function(a,b){
    return scores[b] - scores[a];
  });
  
  scoresList.forEach( function(element,index,array){
    scoreStr = ['<li>',element,'&emsp;',scores[element],'</li>'];
    scoreStr = scoreStr.join("");
    
    $("#mockompa").append(scoreStr);
  });
  
}

function ompaPerSwimmer(){
  var scores, scoresList, scoreStr;
  
  scores = {
    OCC: 13.58,
    SH: 11.23,
    MEAD: 12.09,
    PARK: 10.72,
    MCC: 8.34,
    MRSC: 11.15,
    MIRA: 6.96,
    MVP: 10.26,
    CCC: 6.9
  };
  
  scoresList = Object.keys(scores).sort( function(a,b){
    return scores[b] - scores[a];
  });
  
  scoresList.forEach( function(element,index,array){
    scoreStr = ['<li>',element,'&emsp;',scores[element],'</li>'];
    scoreStr = scoreStr.join("");
    
    $("#mockompaperswimmer").append(scoreStr);
  });
  
}


/// mock ompa chart

var data = {
  labels: ["8/4/13 OMPA","1/30/14 Age-Up","6/13/14","6/22/14"],
  datasets: [
    {
      team: "OCC",
      fillColor: "transparent",
      strokeColor: '#83F52C',
      pointColor: '#83F52C',
      pointStrokeColor: "#fff",
      data: [3319,3312,4145,3992]
    },
    
    {
      team: "SH",
      fillColor: "transparent",
      strokeColor: '#0000cd',
      pointColor: '#0000cd',
      pointStrokeColor: "#fff",
      data: [3032,3233,2940,2919]
    },
    
    {
      team: "MEAD",
      fillColor: "transparent",
      strokeColor: 'pink',
      pointColor: 'pink',
      pointStrokeColor: "#fff",
      data: [2813,2404,2768,3094]
    },

    {
      team: "MCC",
      fillColor: "transparent",
      strokeColor: '#228b22',
      pointColor: '#228b22',
      pointStrokeColor: "#fff",
      data: [1898,1908,2080,2643]
    },

    {
      team: "PARK",
      fillColor: "transparent",
      strokeColor: '#9400d3',
      pointColor: '#9400d3',
      pointStrokeColor: "#fff",
      data: [1897,2140,2403,2777]
    },

    {
      team: "MVP",
      fillColor: "transparent",
      strokeColor: '#ffff00',
      pointColor: '#ffff00',
      pointStrokeColor: "#fff",
      data: [1264,1187,444,1611]
    },
    
    {
      team: "MRSC",
      fillColor: "transparent",
      strokeColor: '#00ffff',
      pointColor: '#00ffff',
      pointStrokeColor: "#fff",
      data: [1261,1667,1566,2074]
    },
    
    {
      team: "CCC",
      fillColor: "transparent",
      strokeColor: '#ff8c00',
      pointColor: '#ff8c00',
      pointStrokeColor: "#fff",
      data: [1103,968,386,993]
    },
    
    {
      team: "MIRA",
      fillColor: "transparent",
      strokeColor: '#98fb98',
      pointColor: '#98fb98',
      pointStrokeColor: "#fff",
      data: [868,821,920,1267]
    }
  ]
};

var options = {
				
	//Boolean - If we show the scale above the chart data			
	scaleOverlay : true,
	
	//Boolean - If we want to override with a hard coded scale
	scaleOverride : false,
	
	//** Required if scaleOverride is true **
	//Number - The number of steps in a hard coded scale
	scaleSteps : null,
	//Number - The value jump in the hard coded scale
	scaleStepWidth : null,
	//Number - The scale starting value
	scaleStartValue : null,

	//String - Colour of the scale line	
	scaleLineColor : "rgba(255,255,255,.5)",
	
	//Number - Pixel width of the scale line	
	scaleLineWidth : 1,

	//Boolean - Whether to show labels on the scale	
	scaleShowLabels : true,
	
	//Interpolated JS string - can access value
	scaleLabel : "<%=value%>",
	
	//String - Scale label font declaration for the scale label
	scaleFontFamily : "'Arial'",
	
	//Number - Scale label font size in pixels	
	scaleFontSize : 16,
	
	//String - Scale label font weight style	
	scaleFontStyle : "normal",
	
	//String - Scale label font colour	
	scaleFontColor : "#fff",	
	
	///Boolean - Whether grid lines are shown across the chart
	scaleShowGridLines : true,
	
	//String - Colour of the grid lines
	scaleGridLineColor : "rgba(255,255,255,.2)",
	
	//Number - Width of the grid lines
	scaleGridLineWidth : 1,	
	
	//Boolean - Whether the line is curved between points
	bezierCurve : true,
	
	//Boolean - Whether to show a dot for each point
	pointDot : true,
	
	//Number - Radius of each point dot in pixels
	pointDotRadius : 3,
	
	//Number - Pixel width of point dot stroke
	pointDotStrokeWidth : 1,
	
	//Boolean - Whether to show a stroke for datasets
	datasetStroke : true,
	
	//Number - Pixel width of dataset stroke
	datasetStrokeWidth : 2,
	
	//Boolean - Whether to fill the dataset with a colour
	datasetFill : true,
	
	//Boolean - Whether to animate the chart
	animation : true,

	//Number - Number of animation steps
	animationSteps : 60,
	
	//String - Animation easing effect
	animationEasing : "easeOutQuart",

	//Function - Fires when the animation is complete
	onAnimationComplete : null
	
};

function ompaChart(data,options){
  var chartHeight, chartWidth, ctx;
  
	ctx = document.getElementById('mockompachart').getContext('2d');
  chartHeight = 400;
  chartWidth = document.documentElement.clientWidth - 20;
  $('#mockompachart').html(chartWidth);
	ctx.canvas.width = chartWidth;
	ctx.canvas.height = 400;
	new Chart(ctx).Line(data,options);
}

function ompaChartLegend(data){
  var team,color,legend,str = "";

  for (var i = 0; i < data.datasets.length; i++){
    team = data.datasets[i].team;
    color = data.datasets[i].strokeColor;
    str += "<span style='color:" + color + ";'> ";
    str += team + " </span>"; 
  }
  
  legend = document.getElementById('mockompalegend');
  legend.innerHTML = str;

}

////////////////////
/// Mock OMPA /////
if (document.getElementById('mockompa')){
  var chartHeight, chartWidth;
  
  ompaCurrent();
  ompaPerSwimmer();
  ompaChart(data,options);
  ompaChartLegend(data);

}
