import React from 'react';

const AddUser = (props) => {
    return(
        <form onSubmit={(event) => props.addUser(event)}>
            <div className="field">
                <input name="username"
                       className="input is-large"
                       type="text"
                       placeholder="Insert a username"
                       required
                       value={props.username}
                       onChange={props.handleChange}
                />
            </div>
            <div className="field">
                <input name="email"
                       className="input is-large"
                       type="email"
                       placeholder="Enter a email"
                       required
                       value={props.email}
                       onChange={props.handleChange}
                />
            </div>
            <input 
                type="submit"
                className="button is-link is-fullwidth"
                value="Enviar"
            />
        </form>
    )
};

export default AddUser;