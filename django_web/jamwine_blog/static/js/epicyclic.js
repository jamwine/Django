// set the dimensions and margins of the graph
var width = 500;
var height = 500;
var margin = 50;

// append the svg object to the body of the page
var svg = d3
  .select("#epicyclic-graph")
  .append("svg")
  .attr("width", width + margin * 2)
  .attr("height", height + margin * 2)
  .append("g")
  .attr("transform", "translate(" + margin + "," + margin + ")");

// create scales
var x = d3.scaleLinear().domain([-2, 2]).range([0, width]);

var y = d3.scaleLinear().domain([-2, 2]).range([height, 0]);

// create data
var numPoints = 400;
var data = d3.range(numPoints).map(function (i) {
  var t = (2 * Math.PI * i) / numPoints;
  return {
    x: Math.cos(5 * t) + Math.cos(10 * t) / 2,
    y: Math.sin(5 * t) + Math.sin(10 * t) / 2,
  };
});

// draw circles
var circles = svg
  .selectAll("circle")
  .data(data)
  .enter()
  .append("circle")
  .attr("cx", function (d) {
    return x(d.x);
  })
  .attr("cy", function (d) {
    return y(d.y);
  })
  .attr("r", 2)
  .attr("fill", "blue");

// add axes
svg
  .append("g")
  .attr("transform", "translate(0," + height / 2 + ")")
  .call(d3.axisBottom(x));

svg
  .append("g")
  .attr("transform", "translate(" + width / 2 + ",0)")
  .call(d3.axisLeft(y));
