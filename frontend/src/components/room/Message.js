import React, {useEffect} from 'react'

export const Message = ({messages}) => {


  return (
    <>
    {
        messages.map( (item, index) => (
            <div key={index}>
                <h1>{item.user}</h1>
                <p>{item.value}</p>
            </div>
        ))
    }
    </>
  )
}
