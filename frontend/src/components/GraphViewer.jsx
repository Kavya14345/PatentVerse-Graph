import ForceGraph2D from "react-force-graph-2d";
function GraphViewer({data}){
const graphData={
nodes:data.nodes,
links:data.relationships.map(
r=>({
source:r.source,
target:r.target,
label:r.relationship
})
)
};
return (
<ForceGraph2D
graphData={graphData}
nodeLabel={
node=>node.label
}
nodeAutoColorBy="type"
/>
)
}
export default GraphViewer;