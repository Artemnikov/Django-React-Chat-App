import React, {useEffect, useState} from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
import style from './lobby.module.css'

export const Lobby = () => {

  const [ username, setusername ] = useState('')

  useEffect( () => {
    const queryString = window.location.search;
    setusername(queryString.split('=')[1])
  }, [])

  const enterRoom = (e) => {
    e.preventDefault()
    const formData = {
      room: room_name.value,
      username: username
    }

    axios.post('http://localhost:8000/server/checkroom/', JSON.stringify(formData))
      .then(data => 
        window.location.href = `http://localhost:8000/room/?room=${data.data.room}&name=${data.data.username}`)
  }


  return (
    <>
        <form  className={style.container}>
        <Link to='/'> Home </Link>
        <label htmlFor='room_name'> Room Name </label>
        <input type='text' id='room_name' placeholder='Room Name' required />
        <label htmlFor='user_name'> User Name </label>
        <input type='text' id='user_name' placeholder='Name' value={username.replace('_', ' ')} />
        <input onClick={enterRoom} type='submit' />
      </form>
    </>
  )
}
