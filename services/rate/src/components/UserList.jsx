import React from 'react';
 
const TeacherList = (props) => {
  return (
	<div>
  	{
    	props.teachers.map((teach) => {
      	return (
        	<h2
          	key={teach.id}
          	className="box title is-4"
        	> { teach.name }
        	</h2>
      	)
    	})
  	}
	</div>
  )
}
 
export default TeacherList;