import React from 'react';

const AddTeacher = (props) => {
    return(
        <form onSubmit={(event) => props.addU(event)}>
            <div className="field">
                <input
                    name="teachername"
                    className="input is-large"
                    type="text"
                    placeholder="Ingrese nombre del profesor"
                    value={props.teachername}
                    onChange={props.handleChange}
                    required
                >
                </input>
            </div>
            <div className="field">
                <input
                    name="teacherlastname"
                    className="input is-large"
                    type="text"
                    placeholder="Ingrese apellido del profesor"
                    onChange={props.handleChange}
                    value={props.teacherlastname}
                >
                </input>
            </div>
            <div className="field">
                <input
                    name="teachercareer"
                    className="input is-large"
                    type="text"
                    placeholder="Ingrese Carrera Profesional"
                    onChange={props.handleChange}
                    value={props.teachercareer}
                >
                </input>
            </div>
            <div className="field">
                <input
                    name="teacherfaculty"
                    className="input is-large"
                    type="text"
                    placeholder="Ingrese Facultad"
                    onChange={props.handleChange}
                    value={props.teacherfaculty}
                >
                </input>
            </div>
            <input type="submit"
                    className="button is-link is-fullwidth"
                    value="Enviar"
                    >
            </input>
        </form>
    )
}

export default AddTeacher;