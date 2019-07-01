import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import TeacherList from './components/UserList';
import AddTeacher from './components/AddTeacher';

class App extends Component{
    constructor(){
        super();
        this.state = {
            teachers: [],
            teachername: '',
            teacherlastname: '',
            teachercareer: '',
            teacherfaculty: ''
        }
        this.addU = this.addU.bind(this);
        this.handleChange = this.handleChange.bind(this);
    }

    addU(e){
        e.preventDefault();
        const data = {
            teachername: this.state.teachername,
            teacherlastname: this.state.teacherlastname,
            teachercareer: this.state.teachercareer,
            teacherfaculty: this.state.teacherfaculty
        }
        axios.post(`http://localhost:5002/teachers`, data)
        .then((res) => {
            this.getData();
            this.setState({teachername: '', teacherlastname: '', teachercareer: '', teacherfaculty: ''})
        })
        .catch((err) => {console.log(err) })
    }

    componentDidMount(){
        this.getData();
    }

    handleChange(event){
        const obj = {}
        obj[event.target.name] = event.target.value;
        this.setState(obj);
    }

    getData(){
        axios.get(`http://localhost:5002/teachers`)
        .then((res)=> {
            this.setState({
              teachers: res.data.data.teachers
            })
        })
        .catch((err) => { console.log(err) })
    }

    render(){
        return (
        <section className="section">
            <div className="container">
                <div className="columns">
                    <div className="column is-one-third">
                        <h1 className="title ls-1 ls-1">Todos los profesores</h1>
                    </div>
                    <hr/><br/>
                    <AddTeacher 
                        teachername={this.state.teachername}
                        teacherlastname={this.state.teacherlastname}
                        teachercareer={this.state.teachercareer}
                        teacherfaculty={this.state.teacherfaculty}
                        handleChange={this.handleChange}
                        addU={this.addU}></AddTeacher>
                    <br></br>
                </div>
                <TeacherList teachers={this.state.teachers}></TeacherList>
            </div>
        </section>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('root'));