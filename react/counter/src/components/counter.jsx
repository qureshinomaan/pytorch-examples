import React, { Component } from 'react';

class Counter extends Component {
	state = {
		count:this.props.value,
		imageUrl : 'https://picsum.photos/200', 
		tags : ['tag1', 'tag2']
	}; 

	// constructor(){
	// 	super();
	// 	this.handleIncrement = this.handleIncrement.bind(this);
	// }

	styles = {
		fontSize : 25, 
		fontWeight : "bold"
	}

	render() { 

		return (
			<React.Fragment>
				<img src={this.state.imageUrl}></img>
				{this.props.children}
				<btn onClick={() => this.props.onIncrement(this.props.counter)} style={this.styles} className="btn btn-secondary m-2">Increment </btn>
				<span style={{fontSize:30}} className={this.getClassBadges()}>{this.props.value}</span>
				<button onClick={() => this.props.onDel(this.props.id )} className="btn btn-danger btn-sm m-2">Delete</button>
				<ul>
					{this.state.tags.map(tag =><li>{tag }</li>)}
				</ul>
				{this.state.tags.length === 0 && "Please Create a new list"}
			</React.Fragment>);
	}

	// handleIncrement = (product) =>{
	// 	console.log(product)
	// 	if(this.state.count < 20){
	// 		this.setState({count : this.state.count+1});
	// 	}
	// 	console.log(this.state.count)
	// }

	formatCount(){
		const { count } = this.state;
		return count == 0 ? 'Zero' : count
	}

	getClassBadges(){
		let classes = "badge m-2 badge-";
		if(this.props.value === 0){
			classes += "warning";
		}
		else {
			classes += "primary";
		}
		return classes;
	}
}
 
export default Counter;