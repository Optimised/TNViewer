$(function() {
  console.log('jquery is working!');
  createGraph();
});

var simulation;

function createGraph() {
	var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

	var color = d3.scaleOrdinal(d3.schemeCategory20);

	d3.json("/data" , function(graph) {
		// if (error) throw error;
		console.log(graph);

		

		var link = svg.append("g")
			.attr("class", "links")
			.selectAll("line")
			.data(graph.links)
			.enter().append("line")
			.attr("stroke-width", function(d) {
				return d.value; 
			})
			.attr("stroke", function(d) {
				if (d.value < 1) {
					return "orange";
				} else if (d.value >= 10) {
					return "black";
				}
				return "blue";		
			});

		var node = svg.append("g")
			.attr("class", "nodes")
			.selectAll("circle")
			.data(graph.nodes)
			.enter().append("circle")
			.attr("r", 10)
			.attr("fill", function(d) { return color(d.group); })
			.call(d3.drag()
				.on("start", dragstarted)
				.on("drag", dragged)
				.on("end", dragended));
		
		var text = svg.selectAll("text")
			.data(graph.nodes)
			.enter()
			.append("text")

		text
			.attr("x", function(d) { return d.cx; })
			.attr("y", function(d) { return d.cy; })
			.text(function(d) { return d.id; })
			.attr("font-family", "sans-serif")
			.attr("font-size", "20px")
			.attr("fill", "red");
	
		simulation = d3.forceSimulation()
			.force("charge", d3.forceManyBody().strength(-2000))
		    // .force("link", d3.forceLink(graph.links).distance(200))
		 //    .force("center", d3.forceCenter(width / 2, height / 2))
		    .force("x", d3.forceX())
		    .force("y", d3.forceY())
		    .force("link", d3.forceLink().id(function(d) { return d.id; }))
	    	// .force("charge", d3.forceManyBody())
	    	.force("center", d3.forceCenter(width / 2, height / 2))

		simulation
			.nodes(graph.nodes)
			.on("tick", ticked);

		simulation.force("link")
			.links(graph.links);

		function ticked() {
			link
				.attr("x1", function(d) { return d.source.x; })
				.attr("y1", function(d) { return d.source.y; })
				.attr("x2", function(d) { return d.target.x; })
				.attr("y2", function(d) { return d.target.y; });

			node
				.attr("cx", function(d) { return d.x; })
				.attr("cy", function(d) { return d.y; });
		}


	});

		
	
	   

}

function dragstarted(d) {
  if (!d3.event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}

function dragged(d) {
  d.fx = d3.event.x;
  d.fy = d3.event.y;
}

function dragended(d) {
  if (!d3.event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}
