import React, { Component } from 'react';
import Counter from './counter';


class Counters extends Component {
    state = {
        counters : [
            {id: 1, value:4},
            {id: 2, value:0},
            {id: 3, value:0},
            {id: 4, value:0}
        ]
     }

    handleReset = () =>{
        const counters = this.state.counters.map(c=>{
            c.value = 0;
            return c;
        });
        this.setState({ counters : counters })
    };

    handleDelete = (counterId) =>{
        console.log("Handle Delete Called!");
        const counter = this.state.counters.filter(c => c.id !== counterId)
        this.setState({counters : counter});
    };

    handleIncrement = counter => {
    console.log("in handleincrement")
       const counters = [...this.state.counters];
       const index = counters.indexOf(counter);
       counters[index] = {...counter};
       counters[index].value += 1;
       this.setState({ counters : counters });
    }

    render() {
        return (
            <div>
                <button onClick={this.handleReset} className="btn-danger">Reset</button>
                {this.state.counters.map(counter => <Counter key = {counter.id} value ={counter.value} id={counter.id} onDel={this.handleDelete} onIncrement={this.handleIncrement} counter = {counter}>
                    <h4>Counter #{counter.id}</h4>
                </Counter>)}
            </div>
         );
    }
}
 


export default Counters;
