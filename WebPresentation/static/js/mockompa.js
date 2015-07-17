
var currentScores = {
  OCC:4066,
  SH:3003,
  MEAD:2985,
  PARK:2405,
  MCC:2737,
  MRSC:1440,
  MIRA:1647,
  MVP:2098,
  CCC:1004
};

var currentSwimmers = {
  OCC: 245,
  SH: 235,
  MEAD: 235,
  PARK: 245,
  MCC: 255,
  MRSC: 159,
  MIRA: 175,
  MVP: 161,
  CCC: 125
}

function ompaCurrent(){
  var scoresList, scoreStr;
  
  scoresList = Object.keys(currentScores).sort( function(a,b){
    return scores[b] - scores[a];
  });
  
  scoresList.forEach( function(element,index,array){
    scoreStr = ['<li>',element,'&emsp;',scores[element],'</li>'];
    scoreStr = scoreStr.join("");
    
    $("#mockompa").append(scoreStr);
  });
  
}

function cleanRound(points,swimmers){
  return Math.round((points / swimmers)*100)/100;
}

function ompaPerSwimmer(){
  var scores, scoresList, scoreStr;
  // second parameter is taken from meet program ie number of swimmers
  scores = {};

  for (var key in currentScores){
    scores[key] = cleanRound(currentScores[key], currentSwimmers[key]);
  }
  
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
  labels: [
  "8/4/13 OMPA",
  "1/30/14 Age-Up",
  "6/22/14",
  "8/5/14",
  "8/13/14 OMPA",

  "7/16/15"
  ],
  datasets: [
    {
      team: "OCC",
      fillColor: "transparent",
      strokeColor: '#83F52C',
      pointColor: '#83F52C',
      pointStrokeColor: "#fff",
      data: [3319,3312,3992,3837,3961, 4066]
    },
    
    {
      team: "SH",
      fillColor: "transparent",
      strokeColor: '#0000cd',
      pointColor: '#0000cd',
      pointStrokeColor: "#fff",
      data: [3032,3233,2919,3080,3254, 3003]
    },
    
    {
      team: "MEAD",
      fillColor: "transparent",
      strokeColor: 'pink',
      pointColor: 'pink',
      pointStrokeColor: "#fff",
      data: [2813,2404,3094,2955,2855, 2985]
    },

    {
      team: "MCC",
      fillColor: "transparent",
      strokeColor: '#228b22',
      pointColor: '#228b22',
      pointStrokeColor: "#fff",
      data: [1898,1908,2643,2524,2732, 2737]
    },

    {
      team: "PARK",
      fillColor: "transparent",
      strokeColor: '#9400d3',
      pointColor: '#9400d3',
      pointStrokeColor: "#fff",
      data: [1897,2140,2777,2880,2657, 2405]
    },

    {
      team: "MVP",
      fillColor: "transparent",
      strokeColor: '#ffff00',
      pointColor: '#ffff00',
      pointStrokeColor: "#fff",
      data: [1264,1187,1611,1798,1782, 2098]
    },
    
    {
      team: "MRSC",
      fillColor: "transparent",
      strokeColor: '#00ffff',
      pointColor: '#00ffff',
      pointStrokeColor: "#fff",
      data: [1261,1667,2074,1817,1735, 1440]
    },
    
    {
      team: "CCC",
      fillColor: "transparent",
      strokeColor: '#ff8c00',
      pointColor: '#ff8c00',
      pointStrokeColor: "#fff",
      data: [1103,968,993,1118,1073, 1004]
    },
    
    {
      team: "MIRA",
      fillColor: "transparent",
      strokeColor: '#98fb98',
      pointColor: '#98fb98',
      pointStrokeColor: "#fff",
      data: [868,821,1267,1383,1347, 1647]
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
